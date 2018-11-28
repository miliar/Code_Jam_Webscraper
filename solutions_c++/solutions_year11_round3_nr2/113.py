// A.cpp : Defines the entry poull for the console application.
//

#include "stdafx.h"

#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ull;

void solve(string sFileIn, string sFileOut)
{
	ull N, T, L, t, C;
	ifstream fi(sFileIn.c_str());
	ofstream fo(sFileOut.c_str());
	fi >> T;
	for (ull i=0;i<T;i++)
	{
		fi >> L >> t >> N >> C;
		vector<ull> a(C);
		for (ull j=0;j<C;j++)
		{
			fi >> a[j];
		}
		vector<ull> sorta = a;
		sort(sorta.begin(), sorta.end());
		vector<ull> dist(N+1);
		for (ull j=0;j<N;j++)
		{
			dist[j] = a[j%C];
		}
		ull tim = 0;
		ull atj = 0;
		for (ull j=0;j<=N;j++)
		{
			ull tnext = dist[j]*2;
			if (tim+tnext>t)
			{
				atj = j;
				break;
			}
			tim += tnext;
			atj = j;
		}
		if (atj==N)
		{
			fo << "Case #" << (i+1) << ": " << tim << endl;
		}
		else
		{
			ull part = dist[atj]*2 - (t-tim);
			vector<char> boo(N, 0);
			for (ull sz=C-1;sz>=0;sz--)
			{
				if (L==0) break;
				if (boo[atj]==0)
				{
					if (part>=sorta[sz]*2)
					{
						boo[atj] = 1;
						L--;
					}
				}
				for (ull j=atj+1;j<N;j++)
				if (boo[j]==0 && dist[j]==sorta[sz] && L>0)
				{
					boo[j] = 1;
					L--;
				}
			}
			tim += (t-tim);
			if (boo[atj]==1)
				tim += part/2;
			else
				tim += part;
			for (ull j=atj+1;j<N;j++)
			{
				ull tnext = dist[j];
				if (boo[j]==0)
					tnext = tnext*2;
				tim += tnext;
			}
			fo << "Case #" << (i+1) << ": " << tim << endl;
		}
	}
	fi.close();
	fo.close();


}

int _tmain(ull argc, _TCHAR* argv[])
{
	//solve("test.in", "test.out");
	//solve("B0.in", "B0.out");
	solve("B1.in", "B1.out");

	return 0;
}

