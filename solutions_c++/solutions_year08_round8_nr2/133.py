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

int N, n, res;
char nam[1000][20];
int a[1000], b[1000], aa[1000], bb[1000];

set<string> ss;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n", &N);
	for (int ii=1; ii<=N; ++ii)
	{
		scanf("%d\n", &n);
		for (int i=0; i<n; ++i)
			scanf("%s%d%d\n", nam[i], &aa[i], &bb[i]);
		res = 10000;
		for (int k=(1<<n)-1; k>=0; --k)
		{
			ss.clear();
			int r = 0;
			for (int i=0; i<n; ++i)
				if (k & (1<<i))
				{
					a[r] = aa[i];
					b[r] = bb[i];
					++r;
					ss.insert(nam[i]);
				}
			for (int t=0; t<r; ++t)
				for (int i=1; i<r; ++i)
					if (a[i]<a[i-1])
						swap(a[i], a[i-1]),
						swap(b[i], b[i-1]);
			bool f = ss.size()<=3;
			int mx = 0, mn1 = -1,  mn2 = 100000;
			for (int i=0; i<r; ++i)
			{
				if (a[i]<=mx+1)
					mx = max(mx, b[i]);
				else
					f = false;

				if (a[i]>b[i])
					mn1 = max(mn1, b[i]),
					mn2 = min(mn2, a[i]);
			}

			f = f && (a[0] == 1 || a[0] <= mn1+1) && (mx == 10000 || mx >= mn2-1);
			if (f)
				res = min(res, r);
		}
		if (res != 10000)
			printf("Case #%d: %d\n", ii, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", ii);
	}
	return 0;
}
