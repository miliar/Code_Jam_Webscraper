#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector> 
#include <fstream>
#include <string>
#include <map>


using namespace std;

int main() {
    
	//Opens file and prints to cout whether it succeeded/failed	
    string fName = "in.txt"; // **** INPUT FILE NAME HERE **** 		
    ifstream musicFile( fName.c_str() );	
    if (musicFile.fail() ) 
    {
	    //cout << "File not found" << endl;
	}
	//else cout << "Got the file" << endl << endl;
	
	string sLine;
	
	int nCases;
	int currentCase = 1;
	int sCount;
	int qCount;
	int switchCount = 0;
	int mapTot = 0;
	int i;
	
	ofstream myfile;
    myfile.open ("1_A_small_b.txt");

	
	
		getline(musicFile, sLine); //reads in file line by line
		nCases = atoi(sLine.c_str());
        //cout << nCases << " cases" << endl;
        
        for (int z = 0; z <nCases;z++) {
            cout << "Case #" << z+1 << ": ";
            myfile << "Case #" << z+1 << ": ";
            getline(musicFile, sLine);
            sCount = atoi(sLine.c_str());
            //getchar();
            //cout << sCount << " engines" << endl;   
           
            map<string,int> engMap;
            map<string,int>::iterator it;

            for (int y = 0; y < sCount; y++) {
                getline(musicFile, sLine);
                engMap[sLine] = 0;
            }
           // getchar();
            
            getline(musicFile, sLine);
            qCount = atoi(sLine.c_str());
            //cout << qCount << " queries" << endl;
            for (int y = 0; y < qCount; y++) {
               // cout << "query " << y << ": " << endl;
                getline(musicFile, sLine);
                
                if(engMap[sLine] == 0) {
                   // cout << sLine << " not searched yet " << endl;
                    engMap[sLine] = 1; 
                    
                    mapTot = 0;                 
                    for ( it=engMap.begin() ; it != engMap.end(); it++ ) {
                       // cout << (*it).first << " => " << (*it).second << endl;
                        mapTot +=(*it).second;
                    }
                    
                    
                    
                   // cout << "mapTot = " << mapTot << endl;
                    
                    if (mapTot == sCount) { //switch
                    
                               switchCount++;
                              // cout << "total switch = " << switchCount << endl;
                               for ( it=engMap.begin() ; it != engMap.end(); it++ ) {
                                   (*it).second = 0;
                               }
                               engMap[sLine] = 1;
                    }
                                             
                    //getchar();
                }
               // else cout << sLine << " already used" << endl;
                    
            }
            cout << switchCount << endl;
            myfile << switchCount << endl;
            switchCount = 0;
            engMap.clear();
                                          
		//getchar();
    }
	
	
    
    getchar();


    myfile.close();

    return 0;
}
