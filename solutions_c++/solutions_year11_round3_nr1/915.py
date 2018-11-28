// GC1C_1.cpp : Defines the entry point for the console application.
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

char T[100][100];
int R, C;

bool ok()
{
	REP(i, R)
		REP(j, C)
	{
		if(T[i][j] == '#')
		{
			if(j+1 >= C || i+1 >= R)
				return false;
			if(T[i][j+1] != '#')
				return false;
			if(T[i][j+1] != '#')
				return false;
			if(T[i+1][j+1] != '#')
				return false;
			T[i][j] = '/';
			T[i+1][j+1] = '/';
			T[i+1][j] = '\\';
			T[i][j+1] = '\\';			
		}
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin>>t;
	REP(petla,t)
	{
		cin>>R>>C;
		REP(i, R)
			REP(j, C)
				cin>>T[i][j];
		cout<<"Case #"<<petla+1<<":"<<endl;
		if(ok())
		{
			REP(i,R)
			{
				REP(j, C)
					cout<<T[i][j];
				cout<<endl;
			}
		}
		else
			cout<<"Impossible"<<endl;

	}
	return 0;
}

