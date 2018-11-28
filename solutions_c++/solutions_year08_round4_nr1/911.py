#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define F0(i,n) for (int i=0; i<n; ++i)
#define F1(i,n) for (int i=1; i<=n; ++i)
#define mems(d,v) memset(d,v,sizeof(d))
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SZ(x) (int)x.size()


LL m,V;
int x[20000],g[20000],c[20000],dp[2][20000],v[20000];

int doit(int in,int val)
{
	int r=1000000;
	if(dp[val][in]!=-1)return dp[val][in];
	
	if(in>=(m-1)/2)
	{
		if(v[in]==val)r=0;
		return dp[val][in]=r;
	}
	if(val==0)
	{
		if(c[in]==1)
	{
		if(g[in]==1)
		{
			r=min( r , doit(2*in+1,0) + doit(2*in+2,0));
			r=min( r, doit(2*in+1,1)+doit(2*in+2,0));
			r=min( r, doit(2*in+1,0)+doit(2*in+2,1));
		}
		else if(g[in]==0)
		{
			r=min( r , doit(2*in+1,0) + doit(2*in+2,0));
			r=min( r, 1+doit(2*in+1,1)+doit(2*in+2,0));
			r=min( r, 1+doit(2*in+1,0)+doit(2*in+2,1));
		}
		
	}
	else
	{
		if(g[in]==1)
		{
			r=min( r , doit(2*in+1,0) + doit(2*in+2,0));
			r=min( r, doit(2*in+1,1)+doit(2*in+2,0));
			r=min( r, doit(2*in+1,0)+doit(2*in+2,1));
		}
		else if(g[in]==0)
		{
			r=min( r , doit(2*in+1,0) + doit(2*in+2,0));
			
		}
	}
	}

	if(val==1)
	{
	if(c[in]==1)
	{
		if(g[in]==1)
		{
			r=min( r , doit(2*in+1,1) + doit(2*in+2,1));
			r=min( r, 1 + doit(2*in+1,1)+doit(2*in+2,0));
			r=min( r, 1 + doit(2*in+1,0)+doit(2*in+2,1));
		}
		else if(g[in]==0)
		{
			r=min( r , doit(2*in+1,1) + doit(2*in+2,1));
			r=min( r, doit(2*in+1,1)+doit(2*in+2,0));
			r=min( r, doit(2*in+1,0)+doit(2*in+2,1));
		}
		
	}
	else
	{
		if(g[in]==1)
		{
			r=min( r , doit(2*in+1,1) + doit(2*in+2,1));
		}
		else if(g[in]==0)
		{
			r=min( r , doit(2*in+1,1) + doit(2*in+2,1));
			r=min( r, doit(2*in+1,1)+doit(2*in+2,0));
			r=min( r, doit(2*in+1,0)+doit(2*in+2,1));
		}
	}
	}
	return dp[val][in]=r;
}


void main()
{
	int probnum,numtest;
	string ins;
	cin>>numtest;
	for(probnum=0;probnum<numtest;probnum++)
	{
		int i,j,k;

		printf("Case #%d: ",probnum+1);
		cin>>m>>V;
		mems(dp,-1);
		mems(g,0);mems(c,0);mems(v,0);
		F0(i,(m-1)/2)
		{
			cin>>g[i]>>c[i];
		}
		for(i=(m-1)/2,j=0;j<(m+1)/2;i++,j++)
		{
			cin>>v[i];
		}

		int t=doit(0,V);

		if(t >10000)cout<<"IMPOSSIBLE"<<endl;
		
		else cout<<t<<endl;
		
	}
}