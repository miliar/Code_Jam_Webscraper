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

long long nn, ii;
long long r, k, n, iter, sum, step;
queue<long long> q;
long long aa[1111];
long long bb[1111];

void gg()
{
	long long t = 0, tt = 0;
	while (t + q.front() <= k && tt < n)
	{
		t += q.front();
		q.push(q.front());
		q.pop();
		++iter;
		++tt;
	}
	sum += t;
	++step;

	if (aa[iter%n] == -1)
	{
		aa[iter%n] = sum;
		bb[iter%n] = step;
	}
	else
	{
		long long dist = (step-bb[iter%n]);
		long long cnt = (r-step)/dist;
		long long weight = (sum-aa[iter%n]);
		sum += weight*cnt;
		step += dist*cnt;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%I64d", &nn);
	for (ii=0; ii<nn; ++ii)
	{
		while (!q.empty())
			q.pop();
		//r = 100000000;
		//k = 1000000000;
		//n = 1000;
		scanf("%I64d %I64d %I64d", &r, &k, &n);
		for (long long i=0; i<n; ++i)
		{
			long long x = 10000000;
			scanf("%I64d", &x);
			q.push(x);
		}

		iter = sum = step = 0;
		memset(aa, -1, sizeof aa);
		while (step < r)
			gg();

		printf("Case #%I64d: %I64d\n", ii+1, sum);
	}
	return 0;
}
