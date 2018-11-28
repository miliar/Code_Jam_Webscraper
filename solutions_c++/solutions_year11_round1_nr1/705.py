#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>

using namespace std;

#define	sqr(a)		((a)*(a))
#define	rep(i,a,b)	for(int i=(a);i<(int)(b);i++)
#define	per(i,a,b)	for(int i=((a)-1);i>=(int)(b);i--)
#define	PER(i,n)	per(i,n,0)
#define	REP(i,n)	rep(i,0,n)
#define	clr(a)		memset((a),0,sizeof (a))
#define	SZ(a)		((int)((a).size()))
#define	ALL(x)		x.begin(),x.end()
#define	mabs(a)		((a)>0?(a):(-(a)))
#define	inf			1000000001
#define	eps			1e-6

#define	MAXN		

long long gcd(long long a,long long b)
{
	while(b!=0)
	{
		long long t = b;
		b = a % b;
		a = t;
	}
	return a;
}

int main()
{
//#define MY_DEBUG
#ifndef MY_DEBUG
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
#endif

	int T;
	scanf("%d",&T);

	REP(k,T)
	{
		long long p,q;
		long long r;
		scanf("%I64d %I64d %I64d",&r,&p,&q);
		if ((p < 100 && q == 100) || (p != 0 && q == 0))
		{
			printf("Case #%d: Broken\n",k + 1);
			continue;
		}
		if (p == 0 && q == 0)
		{
			printf("Case #%d: Possible\n",k + 1);
			continue;
		}
		long long m = gcd(100 - p,100);
		long long n = gcd((100 - q),100);
		long long x1 = p / m;
		long long x2 = (100 - p) / m;
		long long y1 = q / n;
		long long y2 = (100 - q) / n;
		if (y1 < x1)
		{
			y2 *= (x1 / y1) + 1;
			y1 *= (x1 / y1) + 1;
		}
		if (x1 + x2 <= r)
		{
			printf("Case #%d: Possible\n",k + 1);
		}
		else
		{
			printf("Case #%d: Broken\n",k + 1);
		}
	}

	return 0;
}