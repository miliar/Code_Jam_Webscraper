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

int N;
int x,y,k;
int a[1000][1000];
bool f[1000][1000];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d",&N);
	for (int ii=1; ii<=N; ++ii)
	{
		scanf("%d%d%d", &x, &y, &k);
		memset(a, 0, sizeof a);
		memset(f, true, sizeof f);
		for (int i=0; i<k; ++i)
		{
			int x1,x2;
			scanf("%d%d", &x1, &x2);
			f[x1-1][x2-1]=false;
		}
		a[0][0]=1;
		for (int i=0; i<x; ++i)
			for (int j=0; j<y; ++j)
				if (f[i][j])
				{
					if (i>=2 && j>=1)
						a[i][j] += a[i-2][j-1];
					if (i>=1 && j>=2)
						a[i][j] += a[i-1][j-2];
					a[i][j] %= 10007;
				}
		printf("Case #%d: %d\n", ii, a[x-1][y-1]);
	}
	return 0;
}
