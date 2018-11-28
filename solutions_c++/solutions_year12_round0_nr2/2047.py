#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cstring>
#include <string>
#include <queue>

#pragma comment(linker, "/STACK:64000000") 

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef pair<int64,int64> pii64;
typedef pair<double, int> pdi;
typedef pair<double, double> pdd;
typedef pair<pii, int> piii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<pii> vpii;
typedef vector<vpii> vvpii;

#define xn _dsfhsdfsj
#define yn _dthsdfshj

#define toMod 1000000007

int nt;
int n, m, p;
int a[1 << 7];

int f[1 << 7][1 << 7];

int rec(int x, int y)
{
	if (x == n) return 0;
	
	if (f[x][y] != -1) return f[x][y];
	
	int res = 0; 
	
	int cur = a[x] / 3;
	if (a[x] % 3) ++cur;
	if (cur >= p)
		res = max(res, 1 + rec(x + 1, y));
	else
		res = max(res, rec(x + 1, y));

	if (y)
	{
		int X = a[x] / 3;
		int Y = a[x] / 3;
		int Z = a[x] / 3;
		if (a[x] % 3) ++X;
		if (a[x] % 3 == 2) ++Y;
		if (((X + 1) - min(Y - 1, Z) <= 2) && Y) ++X, --Y;
		if (((X + 1) - min(Y, Z - 1) <= 2) && Z) ++X, --Z;
		if (X >= p)
			res = max(res, 1 + rec(x + 1, y - 1));
		else
			res = max(res, rec(x + 1, y - 1));
	}

	return f[x][y] = res;
}

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	scanf("%d", &nt);
	for (int tn = 1; tn <= nt; ++tn)
	{
		scanf("%d", &n);
		scanf("%d%d", &m, &p);
		for (int i = 0; i < n; ++i)
			scanf("%d", &a[i]);
		sort(a, a + n);
		reverse(a, a + n);
		memset(f, -1, sizeof f);
		int res = rec(0, m);
		printf("Case #%d: %d\n", tn, res);
	}

	return 0;
}