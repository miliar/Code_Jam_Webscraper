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

using namespace std;

typedef long long ityp;

#define MAXN 500000 + 1
#define MD 1000000007

ityp n, m, x, y, z;
ityp a[MAXN];
ityp sl[MAXN];
ityp cm[MAXN];
char cl[MAXN];

ityp getComb(const int& cn)
{
	if(cl[cn])
	{
		return cm[cn];
	}
	else
	{
		ityp pc = 1;
		for(int nn = cn + 1; nn < n; nn++)
		{
			if(sl[nn] > sl[cn])
			{
				pc += getComb(nn);
				pc %= MD;
			}
		}

		cl[cn] = 1;
		cm[cn] = pc;
		return cm[cn];
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
        char tBuf[100];

		memset(cl, 0, sizeof(cl));
        
        inFile >> n;
        inFile >> m;
        inFile >> x;
        inFile >> y;
        inFile >> z;
		for(int i = 0; i < m; i++)
		{
			inFile >> a[i];
		}
		for(int i = 0; i < n; i++)
		{
			sl[i] = a[i % m];
			a[i %m] = (x * a[i % m] + y * (i + 1)) % z;
		}

		ityp res = 0;
		for(int cn = 0; cn < n; cn++)
		{
			res += getComb(cn);
			res %= MD;
		}

		outFile << "Case #" << (t+1) << ": " << res << endl;
		inFile.getline(tBuf, 100);
	}

	return 0;
}

