#include <string.h>
#include <assert.h>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <set>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#define sf scanf
#define pf printf
#define fr(i,a,b) for(int i=a;i<b;++i)
using namespace std;
#define ll long long
const double eps = 1e-8;

double dp[1000020];

struct coor
{
	int a,b,w;
}c[10000];

int cmp1( const coor &a, const coor &b)
{
	return a.a<b.a||a.a==b.a&&a.w<b.a;
}

int cmp2( const coor &a, const coor &b )
{
	return a.w < b.w || a.w == b.w && a.a < b.a;
}

int main()
{
	int T;
	sf("%d",&T);
	int ca=0;
	while(T--)
	{
		int x,s,r,t,n;

		sf("%d%d%d%d%d",&x,&s,&r,&t,&n);
		fr(i,0,n)
		{
			sf("%d%d%d",&c[i].a,&c[i].b,&c[i].w);
		}
		sort(c,c+n,cmp1);
		int m=n;	
		int begin = 0;

		fr(i,0,n)
		{
			if( begin < c[i].a )
			{
				c[m].a=begin;
				c[m].b=c[i].a;
				c[m].w=0; 
				m++;
			}
			begin = c[i].b;
		}
		if( begin != x )
		{
			c[m].a=begin;
				c[m].b=x;
				c[m].w=0; 
				m++;

		}
		n=m;
		assert( n < 10000 );
		sort( c, c+n, cmp2 );
		double ret = t;
		double ans = 0;
		fr(i,0,n)
		{
			double newt = (double)( c[i].b-c[i].a )	/ ( c[i].w + r );
		//	printf("a = %d b = %d w = %d\n",c[i].a,c[i].b,c[i].w);
		//	printf(" newt(%lf) ret(%lf)\n",newt,ret );
			if( newt < ret + eps )
			{
				ret -= newt;
				ans += newt;
			}
			else
			{
				double s1 = ( c[i].w + r ) * ret;
				double rets = c[i].b - c[i].a - s1;
				double t2 = rets / ( c[i].w + s );
		//		printf(" s1(%lf) rets(%lf) t2(%lf)\n",s1,rets,t2);
				ans += ret + t2;
				ret = 0;
			}
		}
		printf("Case #%d: %.8lf\n",++ca,ans);

	}
}


