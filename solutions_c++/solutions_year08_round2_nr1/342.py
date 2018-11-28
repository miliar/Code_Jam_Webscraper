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

long long x[1000000],y[1000000];
long long a[3][3];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	long long nn;
	scanf("%I64d", &nn);
	for (int ii=0; ii<nn; ++ii)
	{
		long long n, A, B, C, D, X, Y, M;
		scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d", &n, &A, &B, &C, &D, &X, &Y, &M);
		memset(a, 0, sizeof a);
		for (long long i=0; i<n; ++i)
		{
			x[i]=X;
			y[i]=Y;
			++a[X%3][Y%3];
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}
		long long res = 0, res1 = 0;
/*		for (int i=0; i<n; ++i)
			for (int j=i+1; j<n; ++j)
				for (int k=j+1; k<n; ++k)
				{
					long long x1 = x[i]-x[j], x2 = x[i]-x[k], y1 = y[i]-y[j], y2 = y[i]-y[k];
						if ((x[i]+x[j]+x[k])%3==0 && (y[i]+y[j]+y[k])%3==0)
							++res1;
				}/**/
		for (long long i1=0; i1<3; ++i1)
		for (long long i2=0; i2<3; ++i2)
		for (long long i3=0; i3<3; ++i3)
		for (long long j1=0; j1<3; ++j1)
		for (long long j2=0; j2<3; ++j2)
		for (long long j3=0; j3<3; ++j3)
			if ((i1+i2+i3)%3==0 && (j1+j2+j3)%3==0)
			{
				if ((i1!=i2 || j1!=j2) && (i1!=i3 || j1!=j3) && (i3!=i2 || j3!=j2))
					res += a[i1][j1]*a[i2][j2]*a[i3][j3];
				else
				if (!(i1!=i2 || j1!=j2) && !(i1!=i3 || j1!=j3) && !(i3!=i2 || j3!=j2))
					res += a[i1][j1]*(a[i1][j1]-1)*(a[i1][j1]-2);
				else
				{
					if (i1==i2 && j1==j2)
						res += a[i1][j1]*(a[i2][j2]-1)*a[i3][j3]/2;
					if (i1==i3 && j1==j3)
						res += a[i1][j1]*a[i2][j2]*(a[i3][j3]-1)/2;
					if (i3==i2 && j3==j2)
						res += a[i1][j1]*(a[i2][j2]-1)*a[i3][j3]/2;
				}
			}
		
		printf("Case #%d: %I64d\n", ii+1, res/6);
	}
	return 0;
}
