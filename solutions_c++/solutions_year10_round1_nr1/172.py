// google codejam.cpp : Defines the entry point for the console application.
//

// BEGIN CUT HERE
#include "stdafx.h"
// END CUT HERE
#include <iostream>
#include <cstdio>

#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>
#include <cctype>
#include <cmath>

using namespace std;

#define REP(i,n) for(int i=0;i<n;++i)
#define VI vector<int>
#define VII vector<VI>
#define ALL(n) n.begin(),n.end()
#define LL long long
#define SIZE(o) o.size()

int dx4[]={0,0,-1,1};
int dy4[]={-1,1,0,0};


int main()
{
	freopen("in","r",stdin);freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	int i,j,k;
	int caseID;
	
	char map[51][51];
	REP(caseID,testcase)
	{
		int N,K;
		char last;
		scanf("%d%d%c",&N,&K,&last);
		
		REP(i,N)
			cin.getline(map[i],N+1,'\n');
		vector<vector<char>> v;
		REP(i,N)
			v.push_back(vector<char>());
		REP(i,N)
		{	
			REP(j,N)
			{
				if(map[i][j]!='.')
					v[i].push_back(map[i][j]);
			}
			v[i].insert(v[i].begin(),N-SIZE(v[i]),'.');
		}
		bool okr=false,okb=false;
		REP(i,N)
		{
			REP(j,SIZE(v[i]))
			{
				int c=0;
				int x=i,y=j;
				char now=v[i][j];
				
				if(now=='.')
					continue;
				while(x<N && v[x][y]==now)
				{
					c++;
					x++;
				}
				if(c>=K)
				{
					if(now=='R')
						okr=true;
					else
						okb=true;
					continue;
				}
				x=i;y=j;
				c=0;
				while(y<N && v[x][y]==now)
				{
					c++;
					y++;
				}
				if(c>=K)
				{
					if(now=='R')
						okr=true;
					else
						okb=true;
					continue;
				}
				x=i;y=j;
				c=0;
				while(y<N && x<N && v[x][y]==now)
				{
					c++;
					y++;
					x++;
				}
				if(c>=K)
				{
					if(now=='R')
						okr=true;
					else
						okb=true;
					continue;
				}
				x=i;y=j;
				c=0;
				while(y>=0 && x<N && v[x][y]==now)
				{
					c++;
					y--;
					x++;
				}
				if(c>=K)
				{
					if(now=='R')
						okr=true;
					else
						okb=true;
					continue;
				}
			}
		}
		
		printf("Case #%d: ",caseID+1);
		if(okr && okb)
			cout<<"Both"<<endl;
		else if(okr)
			cout<<"Red"<<endl;
		else if(okb)
			cout<<"Blue"<<endl;
		else 
			cout<<"Neither"<<endl;
		
	}
	
	
	return 0;
}

