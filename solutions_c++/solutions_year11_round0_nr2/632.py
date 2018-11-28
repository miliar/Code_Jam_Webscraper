// ProblemB.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;

int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);
	int T;
	char Ch;
	cin >> T;
	for(int cur=1;cur<=T;cur++)
	{
		char comb[40][3];
		char opos[30][2];
		char inv[101];
		int C;
		cin >> C;
		for(int c=0;c<C;c++)
		{
			cin >> comb[c][0] >> comb[c][1] >> comb[c][2];
		}
		int D;
		cin >> D;
		for (int d=0;d<D;d++)
		{
			cin >> opos[d][0] >> opos[d][1];
		}
		int N;
		cin >> N;
		int k = 0;
		for (int n=0; n<N; n++)
		{
			cin >> inv[k];
			if (k>0)
			{
				for (int c=0;c<C;c++)
				{
					if ((comb[c][0]==inv[k] && comb[c][1]==inv[k-1]) || (comb[c][1]==inv[k] && comb[c][0]==inv[k-1]))
					{
						k--;
						inv[k]=comb[c][2];
						goto next;
					}
				}
				for (int d=0;d<D;d++)
				{
					for (int i=0; i<k; i++)
					{
						if ((opos[d][0]==inv[k] && opos[d][1]==inv[i]) || (opos[d][1]==inv[k] && opos[d][0]==inv[i]))
						{
							k=-1;
							goto next;
						}
					}
				}
			}
			next:k++;
		}
		cout << "Case #" << cur << ": [";
		if (k>0)
		{
			cout << inv[0];
			for (int i=1; i<k; i++)
			{
				cout << ", " << inv[i];
			}
		}
		cout << "]" << endl;
	}
	return 0;

}
