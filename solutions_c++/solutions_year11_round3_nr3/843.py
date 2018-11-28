// GC1C_2.cpp : Defines the entry point for the console application.
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

ll T[10000];

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin>>t;
	REP(petla,t)
	{
		ll N, L, H;
		cin>>N>>L>>H;
		REP(i, N)
			cin>>T[i];

		ll s;
		for(s = L; s<=H; s++)
		{
			bool ok = true;
			REP(i, N)
				if(max(T[i], s) % min(T[i], s) != 0)
				{
					ok = false;
					break;
				}
			if(ok)
			{
				cout<<"Case #"<<petla+1<<": "<<s<<endl;
				break;
			}
		}
		if(s>H)
			cout<<"Case #"<<petla+1<<": NO"<<endl;

	}
	return 0;
}

