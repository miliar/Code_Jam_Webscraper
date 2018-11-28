// GC1A_game.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++) 
#define FOR(i,s,e) for(int i = s; i < e; i++) 
#define FORD(i,e,s) for(int i = e; i > s; i--) 
#define ALL(x) x.begin(), x.end() 
#define OUT(x) cout<<#x<<" = "<<x<<endl; 
#define PB push_back 
typedef long long ll; 

int T[101];


bool possible(double czas, int N, int D)
{
	double last = -10000000;
			bool ok = true;
			REP(i,N)
			{
				double x = T[i];
				if(last + D > x+czas)
				{
					ok = false;
					break;
				}
				last = max(last+D, x-czas);
			}
			if(ok)
			{
				return true;
			}
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin>>t;
	REP(petla,t)
	{
		
		int C, D, N;
		N = 0;
		cin>>C>>D;
		REP(i,C)
		{
			int P, V;
			cin>>P>>V;
			REP(j, V)
				T[N++] = P;
		}
		sort(T, T+N);
		
		double a = 0.0;
		double b = 100*D;

		int licz = 0;
		while(licz++<100)
		{
			double x = (a+b)/2;
			bool ok = possible(x, N, D);
			if(ok)
				b = x;
			else
				a = x;
		}
		cout<<"Case #"<<petla+1<<": "<<(a+b)/2<<endl;
	}

	return 0;
}

