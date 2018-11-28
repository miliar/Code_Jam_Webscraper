// r1p1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#include <string>
#include <set>
#include <map>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ityp;

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

//	int frq[1001];
    for(int t = 0; t < noT; t++)
    {
        char tBuf[100];
        
		int p, k, l;
        inFile >> p;
        inFile >> k;
        inFile >> l;
		inFile.getline(tBuf, 100);
		vector<ityp> frq;
		for(int i = 0; i < l; i++)
		{
			ityp fr;
			inFile >> fr;
			frq.push_back(fr);
		}
		inFile.getline(tBuf, 100);

		int li = 0;
		int cc = 1;
		ityp cost = 0;
		sort(frq.begin(), frq.end());
		for(vector<ityp>::reverse_iterator it = frq.rbegin(); it != frq.rend(); it++, li++)
		{
			if(li == k)
			{
				li = 0;
				cc++;
			}
			cost += (cc * (*it));
		}

		outFile << "Case #" << (t+1) << ": " << cost << endl;
	}

	return 0;
}

