const double pi=3.1415926535897932, e=2.7182818284590452;
#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/stack:16000000")
#include <cstdio>
#include <cmath>
#include <complex>
#include <algorithm>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

long long gcd(long long a, long long b)
{
	if (b==0)
		return a;
	else
		return gcd(b,a%b);
}

long long cnt=0;
long long prim[1000000];

bool Prime(long long x)
{
	long b=long(sqrt(float(x)));
	for (long i=1; prim[i]<=b; i++)
		if (x%prim[i]==0)
			return false;
	return true;
}

const int mx=1100000;

struct Les
{
	int r[mx],h[mx];
	Les(long long n=mx)
	{
		for (long long i=0; i<n; ++i)
			r[i]=i,
			h[i]=0;
	};
	void Get(long long x, long long &R, long long &H)
	{
		if (r[x]==x)
			R=x,
			H=0;
		else
		{
			Get(r[x],R,H);
			r[x]=R;
			H=h[x]=(h[x]+H)%2;
		}
	};
};

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cnt=5, prim[1]=2,prim[2]=3,prim[3]=5,prim[4]=7,prim[5]=11;
	for (long long i=13; i<1100000; i++)
		if (Prime(i))
			prim[++cnt]=i;

	long long nn;
	scanf("%I64d", &nn);
	for (long long ii=0; ii<nn; ++ii)
	{
		long long a,b,p;
		scanf("%I64d%I64d%I64d",&a,&b,&p);
		Les aaa;
		for (long long i=a; i<=b; ++i)
			for (long long j=i+1; j<=b; ++j)
				for (long long k=1; prim[k]<=min(i,j-i); ++k)
					if (prim[k]>=p && i%prim[k]==0 && j%prim[k]==0)
					{
						long long x1,y1,x2,y2;
						aaa.Get(i-a,x1,y1);
						aaa.Get(j-a,x2,y2);
						aaa.r[x1] = x2;
						break;
					}
		set<long long> ss;
		for (long long i=a; i<=b; ++i)
		{
			long long x,y;
			aaa.Get(i-a,x,y);
			ss.insert(x);
		}
		printf("Case #%I64d: %d\n",ii+1,ss.size());
	}
	return 0;
}
