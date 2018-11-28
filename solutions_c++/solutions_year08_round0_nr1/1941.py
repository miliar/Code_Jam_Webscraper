/* 
 * Saving the universe!
 * Author: Coder Cynik to the rescue!
 *
 * Created on 17 July, 2008, 7:19 PM
 */

#include <iostream>
#include <fstream>

bool chkEngine (char* query, char ** engines, int upto) {
    bool fFound = false; char tmpStr[100]; int i;
    for (i=0; i<upto && !fFound; i++) if (strcmp(query, engines[i]) == 0) fFound = true;
    i--;
    
    if (fFound) { 
        strcpy(tmpStr, engines[i]);
        strcpy(engines[i], engines[upto - 1]);
        strcpy(engines[upto-1], tmpStr);
    }
    
    return fFound;
}

int main(int argc, char** argv) {
    
    std::ifstream inputFile("/home/kunal/Desktop/input.txt");
    std::ofstream outputFile("/home/kunal/Desktop/output.txt");
    
    int nEngines, nQueries, i, nSwitches, upto, nCases, K=0;
    char** engines; char tmpEngine[100];
    char currQuery[100];
    char nEnginesTxt[5], nQueriesTxt[5], nCasesTxt[5];
    
    nCases = 0;
    inputFile.getline(nCasesTxt, 5);
    for (int k=0; k<strlen(nCasesTxt); k++)
        nCases = (nCases*10) + nCasesTxt[k] - 48;
    
    while (K < nCases) {
            
    nEngines = 0;
    inputFile.getline(nEnginesTxt, 4);
    for (int k=0; k<strlen(nEnginesTxt); k++) 
        nEngines = (nEngines*10) + nEnginesTxt[k] - 48;
    engines = new char*[nEngines];
    for (i=0; i<nEngines; i++) {
        engines[i] = new char[101];
        inputFile.getline(engines[i], 100);
    }
    
    
    nQueries = 0;
    inputFile.getline(nQueriesTxt, 5);
    for (int k=0; k<strlen(nQueriesTxt); k++) 
        nQueries = (nQueries*10) + nQueriesTxt[k] - 48;
     
    nSwitches = 0; upto = nEngines;
    for (i=0; i<nQueries; i++) {
        inputFile.getline(currQuery, 100);
        
        if (chkEngine(currQuery, engines, upto)) upto--;
        
        if (upto == 0) { 
            nSwitches++; 
            upto = nEngines; 
            if (chkEngine(currQuery, engines, upto)) upto--;
        }
    }
    
    std::cout<<"Case #"<<K+1<<": "<<nSwitches<<"\n";
    outputFile<<"Case #"<<K+1<<": "<<nSwitches<<"\n";
    
    for (i=0; i<nEngines; i++) delete[] engines[i];
    delete[] engines;
   
    K++;
    }
    
    inputFile.close();
    outputFile.close();
    
    return (EXIT_SUCCESS);
}

