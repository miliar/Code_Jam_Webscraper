// aUniv.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

#define MAX_SENAME  100
#define MAX_SENO    100
#define MAX_QRYNO   1000

int tbc[MAX_QRYNO][MAX_SENO];
int noS;
int noQ;
int noC;
int bnC;

void swNext(const int& pos)
{
    for(int s = 0; s < noS; s++)
    {   //try all non matching SE
        const int &cst = tbc[pos][s];
        if(cst != -1)
        {
            if(cst == 0)
            {   //with this engine we can do all the remaining queries -> solution found!
                bnC = noC;
                return;
            }
            else
                if(noC < bnC -1)   //if can do better than best solution so far (by at least solving it in next depth/change)...
                {   //try switching to SE s, which will do the next cst queries...
                    noC++;
                    swNext(pos + cst); 
                    noC--;
                }
        }
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
    string ifName = "input.txt";
    string ofName = "output.txt";
    
    ifstream inFile(ifName.c_str());
    if(!inFile)
    {
        cout << "Error opening input file: " << ifName << endl;
        return -1;
    }

    ofstream outFile(ofName.c_str());
    if(!outFile)
    {
        cout << "Error opening output file: " << ofName << endl;
        return -1;
    }

    int noT;

    inFile >> noT;
    for(int t = 0; t < noT; t++)
    {
        char tBuf[MAX_SENAME+2];
        
        inFile >> noS;
        inFile.getline(tBuf, 110);
        
        map<string, int> mapSI;
        for(int s = 0; s < noS; s++)
        {
            inFile.getline(tBuf, MAX_SENAME+1);
            mapSI[tBuf] = s;
        }

        inFile >> noQ;
        inFile.getline(tBuf, 110);

        int qrs[MAX_QRYNO];
        int sch[MAX_QRYNO];
        for(int q = 0; q < noQ; q++)
        {
            inFile.getline(tBuf, 110);
            qrs[q] = mapSI[tBuf];
            sch[q] = 0;
        }

        for(int s = 0; s < noS; s++)
        {
            int cnt = 0;
            for(int q = noQ-1; q >= 0; q--)
            {
                if(qrs[q] == s)
                {
                    cnt = 1;
                    tbc[q][s] = -1;
                }
                else
                {
                    tbc[q][s] = cnt;
                    if(cnt)
                    {
                        cnt++;
                    }
                }

                if(tbc[q][sch[q]] == -1 || 
                    (tbc[q][sch[q]] != 0 && (tbc[q][sch[q]] < tbc[q][s] || tbc[q][s] == 0)))
                {
                    sch[q] = s;
                }
            }
        }

//        noC = 0;
//        bnC = MAX_QRYNO;
//        swNext(0);

        int pos = 0;
        bnC = 0;
        if(noQ)
        {
            while(tbc[pos][sch[pos]] != 0)
            {
                bnC++;
                pos += tbc[pos][sch[pos]];
            }
        }

        outFile << "Case #" << (t+1) << ": " << bnC << endl;
    }


	return 0;
}

