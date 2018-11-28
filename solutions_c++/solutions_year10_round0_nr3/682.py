#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#pragma comment(linker, "/STACK:16777216")
using namespace std;

#define bit(n) (1<<(n))
#define inf 1000000000
#define eps 1e-9
#define PI 3.1415926535897932385
#define pb push_back
#define sz size()
#define mp make_pair
#define cl clear()
#define all(a) a.begin(),a.end()
#define fill(ar,val) memset(ar,val,sizeof ar)
#define MIN(a,b) if(a>(b)) a=(b)
#define MAX(a,b) if(a<(b)) a=(b)
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef __int64 LL;

#define N 1111

int n;

struct func
{
	int p[N];
	LL s[N];
};

func operator*(func a,func b)
{
	func c;
	int i;
	for(i=0;i<n;i++)
	{
		c.p[i]=b.p[a.p[i]];
		c.s[i]=b.s[a.p[i]]+a.s[i];
	}
	return c;
}

int main()
{
	freopen("C2.in","r",stdin);
	freopen("C2.out","w",stdout);
	int T,t=0;
	for(scanf("%d",&T);T--;)
	{
		LL r,k;
		LL a[N];
		scanf("%I64d%I64d%d",&r,&k,&n);
		int i,j;
		for(i=0;i<n;i++) scanf("%I64d",&a[i]);
		func x;
		for(i=0;i<n;i++)
		{
			LL c=0;
			for(j=i;;)
			{
				if(c+a[j]>k) break;
				c+=a[j];
				j=(j+1)%n;
				if(j==i) break;
			}
			x.p[i]=j;
			x.s[i]=c;
		}
		func y;
		for(i=0;i<n;i++) y.p[i]=i,y.s[i]=0;
		for(;r;)
		{
			if(r%2) y=y*x;
			if(r/=2) x=x*x;
		}
		printf("Case #%d: %I64d\n",++t,y.s[0]);
	}
	return 0;
}
