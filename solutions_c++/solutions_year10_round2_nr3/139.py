#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <numeric>
#include <functional>
#include <iterator>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <ctime>
using namespace std;
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MEM(a,q) memset(a,q,sizeof(a))
#define FOR(i,s,n) for(i=s;i<n;i++)
#define PI acos(-1.0)
#define in(x) scanf("%d",&x)
#define out(x) printf("%d",x)
#define ins(x) scanf("%s",&x)
#define ind(x) scanf("%lf",&x)
#define outd(x) printf("%lf",x)
#define outs(x) printf("%s",x)
#define put puts("")
#define pc(x) putchar(x)
/*
话说当年有个小盆友偷看我代码。。。
后来他死了。。。。
*/
#ifndef _DEBUG
typedef long long int64;
typedef unsigned long long int64u;
#define inl(x) scanf("%lld",&x)
#define outl(x) printf("%lld",x)
#else
typedef __int64 int64;
typedef unsigned __int64 int64u;
#define inl(x) scanf("%I64d",&x)
#define outl(x) printf("%I64d",x)
#endif


int a[501][501];

int c[501][501];

int A(int x,int y)
{
	if(a[x][y]!=-1) return a[x][y];
	if(x==1) return a[x][y]=1;
	a[x][y]=0;
	int i;
	for(i=1;i<x;i++)
	{
		if(y-x-1>=x-i-1)
		{
			int64 tmp =A(i,x);
			tmp*=c[y-x-1][x-i-1];
			tmp%=100003;
			a[x][y]+=tmp;
			a[x][y]%=100003;
		}
	}
	return a[x][y];
}

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int ca,t,n,b,k,ti,m,ans,i,j;
	in(t);
	c[0][0]=1;
	for(i=1;i<=500;i++)
	{
		c[i][0]=1;
		c[i][i]=1;
		for(j=1;j<i;j++)
		{
			c[i][j]=c[i-1][j-1]+c[i-1][j];
			c[i][j]%=100003;
		}
	}
	FOR(ca,1,t+1)
	{
		in(n);
		MEM(a,-1);
		ans=0;
		for(i=1;i<=n-1;i++)
		{
			ans+=A(i,n);
			ans%=100003;
		}
		printf("Case #%d: ",ca);
		out(ans);
		put;
	}
	return 0;
}