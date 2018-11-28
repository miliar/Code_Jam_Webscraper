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

int value[102];
int mem[102][256];
int len;
int inf=1<<25;
int D,I,M;
int count(int n,int v)
{
	if(n>=len-1)
		return 0;
	int& res=mem[n][v];
	if(res!=-1)
		return res;
	res=inf;
	int next=value[n+1];
	
	
	for(int i=max(0,v-M);i<=min(255,v+M);++i)
	{	
		res=min(res,count(n+1,i)+abs(i-next));
		res=min(res,count(n,i)+I);
	}
	res=min(res,count(n+1,v)+D);
	return res;

}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	int i,j,k;
	int caseID;
	
	
	REP(caseID,testcase)
	{
		int N;
		
		scanf("%d%d%d%d",&D,&I,&M,&N);
		REP(i,N)
			scanf("%d",&value[i]);
		len=N;
		REP(i,N)
		{
			REP(j,256)
				mem[i][j]=-1;
		}
		int ans=inf;
		REP(i,N)
		{
			REP(j,256)
				ans=min(ans,count(i,j)+i*D+abs(j-value[i]));
		}
		printf("Case #%d: %d\n",caseID+1,ans);
		
		
	}
	
	
	return 0;
}

