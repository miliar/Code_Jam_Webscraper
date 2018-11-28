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


int x[100],v[100];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	
	int ca,t,n,b,k,ti,m,ans,i;
	in(t);
	FOR(ca,1,t+1)
	{
		in(n);
		in(k);
		in(b);
		in(ti);
		for(i=0;i<n;i++)
		{
			in(x[i]);
		}
		for(i=0;i<n;i++)
		{
			in(v[i]);
		}
		printf("Case #%d: ",ca);
		if(k==0){ puts("0");continue;}
		ans=0;
		for(i=n-1;i>=0;i--)
		{
			if(k==0) break;
			if(x[i]+ti*v[i]>=b){ k--;continue;}
			else ans+=k;
		}
		if(k) puts("IMPOSSIBLE");
		else
		{
			out(ans);
			put;
		}
	}
	return 0;
}