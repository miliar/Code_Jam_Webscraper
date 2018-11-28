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

long long ii, nn;


int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%I64d", &nn);
	for (ii=0; ii<nn; ++ii)
	{
		long long n,k,b,t;
		long long x[1000];
		long long v[1000];
		scanf("%I64d%I64d%I64d%I64d\n", &n, &k, &b, &t);
		for (long long i=0; i<n; ++i)
			scanf("%I64d", &x[i]);
		for (long long i=0; i<n; ++i)
			scanf("%I64d", &v[i]);

		long long res = 0, inq = 0, inb = 0;
		for (long long i=n-1; i>=0 && inb<k; --i)
		{
			if (x[i] + v[i] * t >= b)
			{
				res += inq;
				++inb;
			}
			else
				++inq;
		}

		if (inb >= k)
			printf("Case #%I64d: %I64d\n", ii+1, res);
		else
			printf("Case #%I64d: IMPOSSIBLE\n", ii+1);
	}
	return 0;
}
