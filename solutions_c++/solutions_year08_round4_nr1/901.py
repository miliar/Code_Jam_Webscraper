#if 1
// r1p1.cpp : Defines the entry point for the console application
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

struct node
{
	int	 noc[2];
	bool and;
	bool chg;
};


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
		ityp res = 0;
		node tree[10000];
		int m, v;

		inFile >> m;
		inFile >> v;
		inFile.getline(tBuf, 100);
		for(int i = 0; i < m/2; i++)
		{
			int g, c;
			inFile >> g;
			inFile >> c;
			inFile.getline(tBuf, 100);
			tree[i].and = (g == 1);
			tree[i].chg = (c == 1);
			tree[i].noc[0] = tree[i].noc[1] = 0;
		}

		for(int i = m/2; i < m; i++)
		{
			tree[i].chg = false;
			tree[i].noc[0] = tree[i].noc[1] = -1;
			int cv;
			inFile >> cv;
			tree[i].noc[cv] = 0;
		}

		for(int i = (m/2) - 1; i >= 0; i--)
		{
			node& c = tree[i];
			node& l = tree[2*(i+1)-1];
			node& r = tree[2*(i+1)];
			int onoc[2], anoc[2];
			//or target 0: both 0
			if(l.noc[0] == -1 || r.noc[0] == -1)
			{
				onoc[0] = -1;
			}
			else
			{
				onoc[0] = l.noc[0] + r.noc[0];
			}

			//or target 1: any 1
			if(l.noc[1] == -1 && r.noc[1] == -1)
			{
				onoc[1] = -1;
			}
			else
			{
				if(l.noc[1] != -1 && r.noc[1] != -1)
				{
					onoc[1] = min(l.noc[1], r.noc[1]);
				}
				else
				{
					onoc[1] = max(l.noc[1], r.noc[1]);
				}
			}

			//and target 0: at least one 0
			if(l.noc[0] != -1 || r.noc[0] != -1)
			{
				if(l.noc[0] != -1 && r.noc[0] != -1)
				{
					anoc[0] = min(l.noc[0], r.noc[0]);
				}
				else
				{
					anoc[0] = max(l.noc[0], r.noc[0]);
				}
			}
			else
			{
				anoc[0] = -1;
			}

			//and target 1: both 1
			if(l.noc[1] == -1 || r.noc[1] == -1)
			{
				anoc[1] = -1;
			}
			else
			{
				anoc[1] = l.noc[1] + r.noc[1];
			}
			
			if(c.and)
			{
				c.noc[0] = anoc[0];
				c.noc[1] = anoc[1];
			}
			else
			{
				c.noc[0] = onoc[0];
				c.noc[1] = onoc[1];
			}

			if(c.chg)
			{
				int *pNoc = c.and ? onoc : anoc;
				for(int j = 0; j < 2; j++)
				{
					if(pNoc[j] != -1 && (c.noc[j] == -1 || c.noc[j] > (pNoc[j] + 1)))
					{
						c.noc[j] = pNoc[j] + 1;
					}
				}
			}
		}

		if(tree[0].noc[v] == -1)
		{
			outFile << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
			cout << "Case #" << (t+1) << ": IMPOSSIBLE" << endl;
		}
		else
		{
			outFile << "Case #" << (t+1) << ": " << tree[0].noc[v] << endl;
			cout << "Case #" << (t+1) << ": " << tree[0].noc[v] << endl;
		}
	}

	return 0;
}

#endif