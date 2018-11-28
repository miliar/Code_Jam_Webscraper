// baihacker's head file start--------------
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
// baihacker's head file end--------------

//qu317058542's宏 start-------------
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MEM(a,q) memset(a,q,sizeof(a))
#define FOR(i,s,n) for(i=s;i<n;i++)
#define FORD(i,n,s) for(i=n;i>=s;i--)
#define PI acos(-1.0)

#define in(x) scanf("%d",&x)
#define out(x) printf("%d",x)
#define ins(x) scanf("%s",&x)
#define outs(x) printf("%s",x)
#define ind(x) scanf("%lf",&x)
#define outd(x) printf("%.3f",x)
#define outs(x) printf("%s",x)
#define put puts("")
#define pc(x) putchar(x)
#define pc_ putchar(' ')
#define p2(x,y) ((x)*(x)+(y)*(y))
int gcd(int x,int y)
{
    return x==0?y:gcd(y%x,x);
}
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
//qu317058542's宏 end-------------
int a[1081],b[11][1081];
int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int x1,y1,x2,y2,j,n,i,k,t,ca=0;
	in(t);
	while(t--)
	{
		in(n);
		FOR(i,0,(1<<n))
		{
			in(a[i]);
		}
		FOR(i,0,n)
		{
			FOR(j,0,(1<<(n-1-i)))
			{
				in(b[i][j]);
			}
		}
		int q=(1<<n);
		int ans=0;
		FOR(i,0,n)
		{
			for(j=0;j<q;j+=2)
			{
				if(a[j]==0||a[j+1]==0)
				{
					ans++;
				}
				a[j/2]=MIN(a[j],a[j+1]);
				if(a[j/2])
				a[j/2]--;
			}
			q/=2;
		}
		printf("Case #%d: %d\n",++ca,ans);
	}
	return 0;
}
