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
struct memo
{
	bool count;
	bool v;
};
const int len=10000;
memo mem[len][len];
bool gcd(LL a,LL b)
{
	if(b>=a*2)
		return true;
	if(b<=a+a/2)
		return false;
	if(a<len && b<len )
	{
		if(mem[a][b].count)
			return mem[a][b].v;
		mem[a][b].count=true;
		return mem[a][b].v=!gcd(b-a,a);
	}
	return !gcd(b-a,a);
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	
	int caseID;
	
	for(int k=0;k<len;++k)
		for(int l=0;l<len;++l)
			mem[k][l].count=false;
	REP(caseID,testcase)
	{
		LL a1,a2,b1,b2;
		scanf("%lld%lld%lld%lld",&a1,&a2,&b1,&b2);
		LL ans=0;
		LL i,j;
		for(i=a1;i<=a2;++i)
		{
			ans+=max(0ll,b2-max(i*2,b1)+1);
			for(j=max(b1,i+i/2+1);j<i*2 && j<=b2;++j)
			{
				if(gcd(i,j))
					ans++;
			}
		}
		for(i=b1;i<=b2;++i)
		{
			ans+=max(0ll,a2-max(i*2,a1)+1);
			for(j=max(a1,i+i/2+1);j<i*2 && j<=a2;++j)
			{
				if(gcd(i,j))
					ans++;
			}
		}
		printf("Case #%d: %d\n",caseID+1,ans);
		
		
	}
	
	
	return 0;
}

