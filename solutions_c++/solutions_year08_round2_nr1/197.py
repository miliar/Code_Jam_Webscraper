//* Problem  : Crop Triangles
//* Contest  : Google Code Jam 2008. Online Round 1B
//* Date     : 2008.07.26
//* Author   : alt
//* Language : C++
//* Compiler : Microsoft Visual C++ 8.0

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

#define int64 long long
#define MP make_pair
#define PB push_back
#define SZ(a) (int)a.size()
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define FORSZ(i, a) FOR(i, SZ(a))
#define INF 1000*1000*1000
#define INFLL ((long long)INF*INF)
#define ALL(a) a.begin(), a.end()
#define RALL(a) a.rbegin(), a.rend()

#define int64 long long

#define PI (2.0 * acos(0.0))

int it, nt;

long long A, B, C, D, x00, y00, M;

long long x[100], y[100];

int n, res;

void solve()
{
	int64 X = x00, Y = y00;
	for (int i = 0; i < n; i++)
	{
		x[i] = X; y[i] = Y;
		X = (A * X + B) % M;
		Y = (C * Y + D) % M;
	}
	res = 0;
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			for (int k = j + 1; k < n; k++)
			{
				int xx = x[i] + x[j] + x[k];
				int yy = y[i] + y[j] + y[k];
				res += (xx % 3 == 0) && (yy % 3 == 0);
			}
}

void result()
{
	printf("Case #%d: %d\n", it, res);
}


int main()
{
#ifdef _DEBUG
	freopen("1064", "r", stdin);
	freopen("A-small.out", "w", stdout);	
#endif
	scanf("%d", &nt);
	for (it = 1; it <= nt; it++)
	{
		scanf("%d%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x00, &y00, &M);
		solve();
		result();
	}
	return 0;
}

