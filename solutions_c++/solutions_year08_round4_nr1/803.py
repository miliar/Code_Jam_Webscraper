// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <hash_map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

const int inf = 1000000;
const double pi = atan(1.0)*4.0;
const double eps = 1e-9;




int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;

	for(int t=0; t<T; t++)
	{
		int M, V;
		cin >> M >> V;
		int X = V^1;
		vi val(M);
		vi gate(M);
		vi chan(M);
		vi cost(M);

		for(int i=0; i<(M-1)/2; i++)
		{
			int G, C;
			cin >> G >> C;
			chan[i]=C;
			gate[i]=G^X;
		}
		for(int i=(M-1)/2; i<M; i++)
		{
			int I;
			cin >> I;
			val[i] = I^X;
		}
		for(int i=M-1; i>=0; i--)
		{
			if (i<(M-1)/2)
				val[i] = gate[i] ? val[2*i+1]&val[2*i+2] : val[2*i+1]|val[2*i+2];

			int costi = 0;

			if (val[i]==1)
				costi = 0;
			else if (i>=(M-1)/2)
				costi = inf;
			else if (gate[i]==0) //OR
				costi = min(cost[2*i+1], cost[2*i+2]);
			//AND
			else if (!chan[i])
			{
				if (val[2*i+1]==0)
					costi+= cost[2*i+1];
				if (val[2*i+2]==0)
					costi+= cost[2*i+2];
			}
			//changeable
			else if (val[2*i+1]||val[2*i+2])
				costi = 1;
			else {
				costi = 1 + min(cost[2*i+1], cost[2*i+2]);
			}
			if (cost[i]<inf)
				cost[i]=costi;
			else
				cost[i]=inf;
		}
		
		cout << "Case #" << t+1 <<": ";
		if (cost[0]<inf) 
			cout<< cost[0] << endl;
		else
			cout<< "IMPOSSIBLE" <<endl;
	}

	return 0;
}

