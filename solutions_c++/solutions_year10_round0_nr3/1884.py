// C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

#define ull unsigned long long

void solve()
{
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		ull R,k,N;
		cin >> R >> k >> N;
		vector<ull> q(N);
		for (int i=0;i<N;i++)
			cin >> q[i];
		vector<ull> qmoney(N,0);
		vector<ull> qnext(N,0);
		for (int i=0;i<N;i++)
		{
			ull sum = 0;
			ull p = i;
			ull op = p;
			while (sum+q[p]<=k)
			{
				sum += q[p];
				p = (1+p)%N;
				if (p==op) break;
			}
			qmoney[i] = sum;
			qnext[i] = p;
		}
		ull money = 0;
		ull r = 0;
		ull p = 0;
		while (r<R)
		{
			//if (vride[p]>-1 && r-vride[p]+r<R)
			//{
			//	money += 

			//}
			//else
			{
				money += qmoney[p];
				//vride[p] = r;
				//vsum[p] = money;
				p = qnext[p];
				r++;
			}
		}
		cout << "Case #" << (t+1) << ": " << money << endl;
		

	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

