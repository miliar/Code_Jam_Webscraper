#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;
//task - global variables
int  testCases, curCase, engineCount, queryCount, curEngine, curQuery;
int  optimalEngine, nextStartQuery;
char    engine[101][100];
char    query[1001][100]; 

//
void findOptimalEngine(int startQuery)
{
    int     engineHit[101];    
    int     maxElement = 0;
    int     maxIndex = 1;
    ;
    for(curEngine = 1; curEngine <= engineCount; curEngine++)
    {

        for(curQuery = startQuery; curQuery <= queryCount; curQuery++)
        {                       
            engineHit[curEngine] = 99999;
            if(strcmp(engine[curEngine], query[curQuery]) == 0)       
            {         
                engineHit[curEngine] = curQuery;
                break;
            }    
        }    
    }     
    for(curEngine = 1; curEngine <= engineCount; curEngine++)
    {
        if(engineHit[curEngine] > maxElement)
        {
            maxElement = engineHit[curEngine];
            maxIndex   = curEngine;         
        }        
    }
    optimalEngine  = maxIndex;        
    nextStartQuery = maxElement;
    //cout<<"OptimalEngine = "<<engine[optimalEngine]<<" startQuery = " <<nextStartQuery<<endl;    
}

int main()
{
    //input output declarations
    char inLine[256];
    char outLine[256];    
    ifstream inFile("file.in");
    ofstream outFile("file.out");
    //other declarations
    int switches;
    //end of declarations
    
    //code begins here
    
    inFile.getline(inLine, 256);
    sscanf(inLine, "%i", &testCases);
    cout<<"testCases = "<<testCases<<endl;
    for(curCase = 1; curCase <= testCases; curCase++)
    {//loop through cases
        cout<<"Case = "<<curCase<<endl;
        inFile.getline(inLine, 256);
        sscanf(inLine, "%i", &engineCount);
        cout<<"Engines = "<<engineCount<<endl;    
        if(engineCount)
        {            
            for(curEngine = 1; curEngine <= engineCount; curEngine++)
            {//read in engines
                inFile.getline(inLine, 256,'\n');
                //cout<<inLine<<endl;
                strcpy(engine[curEngine], inLine);
                //sscanf(inLine, "%s\n", engine[curEngine]); 
                cout<<"Engine["<<curEngine<<"] = "<<engine[curEngine]<<endl;                                               
            }    
        }       
        inFile.getline(inLine, 256);
        sscanf(inLine, "%i", &queryCount);
        cout<<"Queries = "<<queryCount<<endl;                                
        if(queryCount)
        {
            for(curQuery = 1; curQuery <= queryCount; curQuery++)
            {//read in engines
                inFile.getline(inLine, 256, '\n');
                //cout<<inLine<<endl;
                //sscanf(inLine, "%s\n", query[curQuery]);    
                strcpy(query[curQuery], inLine);
                cout<<"Query["<<curQuery<<"] = "<<query[curQuery]<<endl;                                               
            } 
        } 
        switches       = 0; 
        if(engineCount && queryCount)
        {
        switches       = 0; 
        nextStartQuery = 1;       
        findOptimalEngine(nextStartQuery);
        while(nextStartQuery != 99999)
        {
            switches++;            
            //cout<<"Switch = "<<switches<<endl;
            findOptimalEngine(nextStartQuery);
         
        }
        sprintf(outLine, "Case #%i: %i\n", curCase, switches);
        outFile.write(outLine, strlen(outLine));                                           
        }
        else
        {
            sprintf(outLine, "Case #%i: %i\n", curCase, switches);
            outFile.write(outLine, strlen(outLine));                                           
        }
    }
    cin>>switches;           
    return 0;
}    
    
