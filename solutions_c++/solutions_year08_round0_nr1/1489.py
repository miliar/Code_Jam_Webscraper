#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <iostream>

using namespace std;

FILE *fp = NULL ;
fstream inputFile;
ofstream outputFile;

bool GetNumberofCases(int *TotalNoCases)
{
    string s1;
    inputFile.getline((char*)s1.c_str(),80);
    *TotalNoCases = atoi(s1.c_str());
    return true;
}

bool GetNumSE(int *SE)
{
    string s1;
    inputFile.getline((char*)s1.c_str(),80);
    *SE = atoi(s1.c_str());
    return true;
}

bool GetNumIQ(int *IQ)
{
    string s1;
    inputFile.getline((char*)s1.c_str(),80);
    *IQ = atoi(s1.c_str());
    return true;
}


void main(int argc, char*argv[])
{
    string SE[100] ;
    int TotalNoCases = 0;
    int TotalSearchEngines = 0;
    string IQ[1000];
    int TotalQueries = 0;
    
    int totalUsedSE = 0 ;
    string CurrentSE;
    bool UsedSE[100];

    inputFile.open(argv[1]);
    GetNumberofCases(&TotalNoCases);
    printf("Total # Test Cases = %d\n",TotalNoCases);

    outputFile.open(argv[2]);
    char s[1024];
    int SwitchesNeeded = 0;
    
    for(int TC = 1; TC <= TotalNoCases; TC++ )
    {

        SwitchesNeeded = 0;
        totalUsedSE = 0;
        CurrentSE.empty();
        GetNumSE(&TotalSearchEngines);
        cout << "CASE " << TC << " : \nTotal Search Engines = " << TotalSearchEngines << endl ;

        for(int i = 0; i < TotalSearchEngines; i++ )
        {
//            inputFile.getline((char*)SE[i].c_str(),1024 );
            
            inputFile.getline(s,1024 );
            SE[i] = s;
            cout << SE[i].c_str() << endl ;
        }

        GetNumIQ(&TotalQueries);
        printf("Total Queries = %d\n", TotalQueries);

        for(int i = 0; i < TotalQueries; i++ )
        {
//            inputFile.getline((char*)IQ[i].c_str(),256, '\n');
                        inputFile.getline(s,1024 );
 //           strcpy(IQ[i].c_str(),s);
                        IQ[i] = s;
            cout << IQ[i].c_str() << endl ;
        }

        for(int i = 0; i < TotalSearchEngines; i++)
        {
            UsedSE[i] = false;
        }

        int CheckQuery = 0;
        int SEIndex = 0;
        for(CheckQuery = 0; CheckQuery < TotalQueries; CheckQuery++)
        {
            for(SEIndex = 0; SEIndex < TotalSearchEngines; SEIndex++)
            {
                if( 0 == strcmp(SE[SEIndex].c_str(),IQ[CheckQuery].c_str()) )
                {
                    if(false == UsedSE[SEIndex])
                    {
                        totalUsedSE++ ;
                        UsedSE[SEIndex] = true;
                        if(totalUsedSE == TotalSearchEngines)
                        {
                            printf("SE Used = %s\n",SE[SEIndex].c_str());
                            CurrentSE = SE[SEIndex];
                            
                            for(int i = 0; i < TotalSearchEngines; i++)
                            {
                                UsedSE[i] = false;
                            }

                            UsedSE[SEIndex] = true;
                            SwitchesNeeded++;
                            totalUsedSE = 1;
                        }
                    }
                    break;
                }
            }
        }

        outputFile << "Case #" << TC << ": " << SwitchesNeeded << endl ;
        
    }

    inputFile.close();
    outputFile.close();

}