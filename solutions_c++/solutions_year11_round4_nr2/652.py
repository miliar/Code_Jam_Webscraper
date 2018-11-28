#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
//#include <complex>
 
using namespace std;
 
void ASS(bool b)
{
    if (!b)
    {
        ++*(int*)0;
    }
}
 
#define FOR(i, x) for (int i = 0; i < (int)(x); i++)
#define CL(x) memset(x, 0, sizeof(x))
 
#pragma comment(linker, "/STACK:106777216")
 
typedef vector<int> vi;
typedef long long LL;

struct M
{
	M(){}
	double x, y;
	int m;
	M(double xx, double yy, int mm)
	{
		x = xx;
		y = yy;
		m = mm;
	}
};

M add(const M& a, const M& b)
{
	if (a.m == 0)
		return b;
	if (b.m == 0)
		return a;
	M res;
	res.m = a.m + b.m;
	res.x = a.x * a.m + b.x * b.m;
	res.y = a.y * a.m + b.y * b.m;
	res.x /= res.m;
	res.y /= res.m;
	return res;
}

const int N = 1 << 9;

struct RSQ
{
	M a[N * 2][N * 2];
	void Build(int *x, int L, int R)
	{
		int k = 0;
		for (L += N, R += N; L < R; L >>= 1, R >>= 1)
		{
			if (L & 1)
			{
				x[k++] = L;
				L++;
			}
			if (R & 1)
			{
				R--;
				x[k++] = R;
			}
		}
		x[k] = -1;
		sort(x, x + k);
	}

	M Sum(int Lx, int Rx, int Ly, int Ry)
	{
		static int x[1024];
		static int y[1024];
		Build(x, Lx, Rx);
		Build(y, Ly, Ry);
		M res(0, 0, 0);
		for (int i = 0; x[i] != -1; i++)
			for (int j = 0; y[j] != -1; j++)
				res = add(res, a[x[i]][y[j]]);
		return res;
	}
	void Add(int x, int y, M m)
	{
		for (int i = N + x; i; i >>= 1)
			for (int j = N + y; j ; j >>= 1)
				a[i][j] = add(a[i][j], m);
	}
};

RSQ rsq;

int a[N][N];

void Solve()
{
	memset(&rsq, 0, sizeof(rsq));
	int n, m, d;
	cin >> n >> m >> d;
	FOR(i, n)
	{
		static char s[1 << 20];
		scanf("%s", s);
		FOR(j, m)
	{
			a[i][j] = s[j] - '0' + d;
			rsq.Add(i, j, M(i + 0.5, j + 0.5, a[i][j])); 
		}
	}
	const double eps = 1e-9;
	for (int k = min(n, m); k >= 3; k--)
	{
		FOR(i, n - k + 1)
			FOR(j, m - k + 1)
		{
			if (k == 5 && i == 1 && j == 1)
				n = n;
			M z = rsq.Sum(i, i + k, j, j + k);
			z = add(z, M(i + 0.5, j + 0.5, -a[i][j]));
			z = add(z, M(i + 0.5 + k - 1, j + 0.5, -a[i + k - 1][j]));
			z = add(z, M(i + 0.5, j + 0.5 + k - 1, -a[i][j + k - 1]));
			z = add(z, M(i + 0.5 + k - 1, j + 0.5 + k - 1, -a[i + k - 1][j + k - 1]));
			if (fabs((i + i + k) / 2.0 - z.x) < eps && fabs((j + j + k) / 2.0 - z.y) < eps)
			{
				printf("%d\n", k);
				return;
			}
		}
	}
	printf("IMPOSSIBLE\n");
}

int main()
{
#ifndef _DEBUG_4444
	freopen("c:\\GCJ\\in.txt", "r", stdin);
	freopen("c:\\GCJ\\out.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}