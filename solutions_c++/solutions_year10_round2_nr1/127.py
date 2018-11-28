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


char a[1001];
map<string,int>qu;

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int ca,t,n,m,ans,i;
	in(t);
	FOR(ca,1,t+1)
	{
		qu.clear();
		in(n);
		in(m);
		ans=0;
		while(n--)
		{
			ins(a);
			qu[a]=1;
			for(i=1;a[i];i++)
			{
				if(a[i]=='/')
				{
					a[i]=0;
					qu[a]=1;
					a[i]='/';
				}
			}
		}
		while(m--)
		{
			ins(a);
			int s=strlen(a);
			if(qu[a])continue;
			ans++;
			qu[a]=1;
			for(i=s-1;i>0;i--)
			{
				if(a[i]=='/')
				{
					a[i]=0;
					if(qu[a]) break;
					qu[a]=1;
					ans++;
					a[i]='/';
				}
			}
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
