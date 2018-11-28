// zero.lin`s google_codejam.cpp 
//

/*
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
*/

#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const int inf=1<<28;
const double eps=1e-11;
int miss[2050];
int price[2050];
int mem[2050][12];
int len;
int go(int n,int m)
{
	if(n>=1<<len)
		return miss[n-(1<<len)]>=m?0:inf;
	int& res=mem[n][m];
	if(res!=-1)
		return res;
	res=inf;
	res=min(res,go(2*n,m+1)+go(2*n+1,m+1));
	res=min(res,go(2*n,m)+go(2*n+1,m)+price[n]);
	return res;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d",&testcase);
	
	rep(caseID,testcase)
	{
		int P;
		scanf("%d",&P);
		rep(i,1<<P)
			scanf("%d",&miss[i]);
		int now=1<<P;
		for(int i=P-1;i>=0;--i)
		{
			int begin=now-(1<<i);
			rep(j,1<<i)
			{
				scanf("%d",&price[begin++]);
			}
			now-=1<<i;
		}
		rep(i,1<<P)
			rep(j,P+1)
				mem[i][j]=-1;
		len=P;
		int ans=go(1,0);
		printf("Case #%d: %d\n",caseID+1,ans);		
	}
	
	return 0;
}

