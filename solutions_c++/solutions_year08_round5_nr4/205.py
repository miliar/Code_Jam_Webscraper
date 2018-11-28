#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

#define MOD 10007

int inv[MOD];

int step(int x, int s)
{
	if (s == 0)
		return 1;
	int r = step(x, s>>1);
	r = (r*r) % MOD;
	if (s & 1)
		r = (r*x) % MOD;
	return r;
}

void calcInv()
{
	int i;
	for (i = 1; i < MOD; ++i)
	{
		inv[i] = step(i, MOD-2);
	}
}

int F(int H, int W)
{
	if (H < 0 || W < 0)
		return 0;
	if (H == 0 && W == 0)
		return 1;
	if ((2*H - W) % 3 || (2*H-W) < 0)
		return 0;
	int a, b;
	a = (2*H-W) / 3;
	b = H-2*a;
	if (b < 0)
		return 0;
	b += a;
	int r = 1;
	int i;
	for (i = b; i > a; --i)
		r = (r*i) % MOD;
	for (i = b-a; i > 1; --i)
		r = (r*inv[i]) % MOD;
	return r;
}

PII A[20];

int main()
{
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
//	freopen("-large.in", "r", stdin);
//	freopen("-large.out", "w", stdout);
	calcInv();

	int T, t;
	scanf("%d", &T);
	for (t = 0; t < T; ++t)
	{
		int H, W, R;
		scanf("%d%d%d", &H, &W, &R);
		int i;
		for (i = 0; i < R; ++i)
			scanf("%d%d", &A[i].first, &A[i].second);
		sort(A, A+R);
		int mask;
		int res = 0;
		for (mask = 0; mask < (1<<R); ++mask)
		{
			int r = 1;
			int px, py;
			px = 1;
			py = 1;
			int k = 0;
			for (i = 0; i < R; ++i)
				if (mask & (1<<i))
				{
					++k;
					r = (r*F(A[i].first - px, A[i].second - py))%MOD;
					px = A[i].first;
					py = A[i].second;
					if (r == 0)
						break;
				}
			r = (r*F(H - px, W - py))%MOD;
			if (k & 1)
				res = (res - r) % MOD;
			else
				res = (res + r) % MOD;
		}
		res = (res + MOD) % MOD;
		printf("Case #%d: %d\n", t+1, res);
		fprintf(stderr, "%d\n", t+1);
	}
	return 0;
};
