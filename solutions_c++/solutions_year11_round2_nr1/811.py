// GC1A_game.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

#define REP(i,n) for(int i = 0; i < n; i++) 
#define FOR(i,s,e) for(int i = s; i < e; i++) 
#define FORD(i,e,s) for(int i = e; i > s; i--) 
#define ALL(x) x.begin(), x.end() 
#define OUT(x) cout<<#x<<" = "<<x<<endl; 
#define PB push_back 
typedef long long ll; 

char T[101][101];

double WP[101][101];
double OWP[101];

double fWP(int n, int me, int without)
{
	if(WP[me][without] != -1.0)
		return WP[me][without];
	int res=0;
	int all = 0;
	REP(i,n)
		if(i != without && i!=me)
		{
			res += T[me][i] == '1';
			all += T[me][i] != '.';
		}
	return WP[me][without] = (double)res/all;
}


double fOWP(int n, int me)
{
	if(OWP[me] != -1.0)
		return OWP[me];
	double res = 0;
	int ile=0;
	REP(i,n)
		if(T[me][i] != '.')
		{
			res += fWP(n, i, me);
			ile++;
		}
	return OWP[me] = res/ile;
}



int _tmain(int argc, _TCHAR* argv[])
{
	int t;
	cin>>t;
	REP(petla,t)
	{
		
		int n;
		cin>>n;
		REP(i,n)
			REP(j,n)
			cin>>T[i][j];

			
		cout<<"Case #"<<petla+1<<":"<<endl;

		REP(i,n)
		{
			REP(j,n)
				WP[i][j] = -1.0;
			OWP[i] = -1.0;
		}

		REP(team, n)
		{
			double res = 0.0;
			double WP, OWP, OOWP;
			WP = OWP = OOWP = 0.0;

			int ile=0;
			REP(i,n)
				if(i!=team)
					if(T[team][i] != '.')
					OOWP += fOWP(n, i), ile++;
			OOWP /= ile;

			res = fWP(n,team, team) * 0.25 + fOWP(n,team) * 0.5 + OOWP * 0.25;
			cout<<res<<endl;
		}



	}

	return 0;
}

