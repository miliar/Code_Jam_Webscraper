#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <fstream>
#include <iostream>

using namespace std;

#define CL(x) memset(x, 0, sizeof(x))

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;

int r, k, n;

int a[2010];
int f[2010];
LL c[2010];

void DoStep(int &x, LL &sum)
{
	sum = a[x];
	int x1 = (x + 1) % n;
	while (x1 != x && sum + a[x1] <= k)
	{
		sum += a[x1];
		x1 = (x1 + 1) % n;
	}
	x = x1;
}

LL Solve()
{
	scanf("%d %d %d", &r, &k, &n);
	FOR(i, n)
		scanf("%d", &a[i]);
	if (r <= n * 7)
	{
		LL res = 0;
		int x = 0;
		FOR(i, r)
		{
			LL t;
			DoStep(x, t);
			res += t;
		}
		return res;
	}
	LL res = 0;
	int x = 0;
	FOR(i, n)
	{
		LL t;
		DoStep(x, t);
		res += t;
	}
	CL(f);
	int CicL = 0;
	LL CicC = 0;
	FOR(i, n * 2)
	{
		LL t;
		DoStep(x, t);
		res += t;
		if (f[x])
		{
			CicL = i + 1 - f[x];
			CicC = res - c[x];
		}
		f[x] = i + 1;
		c[x] = res;
	}
	if (CicL == 0)
	{
		printf("BADBADBAD\n");
		++*(int*)0;
	}
	res += ((r - n * 5) / CicL) * CicC;
	FOR(i, n * 2 + ((r - n * 5) % CicL))
	{
		LL t;
		DoStep(x, t);
		res += t;
	}
	return res;
}


int main()
{
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);

	int t;
	scanf("%d", &t);

	FOR(i, t)
	{
		LL res = Solve();
		printf("Case #%d: %lld\n", i + 1, res);
	}
	return 0;
}