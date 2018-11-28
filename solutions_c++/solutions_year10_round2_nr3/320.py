#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define FOR(i, n) for (int i = 0; i < (int)(n); i++)
#define CL(x) memset(x, 0, sizeof(x));

typedef long long LL;
typedef vector<int> vi;
typedef vector<string> VS;

const int P = 100003;

int p2[1000];

int d[512][512];
int c[512][512];

int D(int n, int x)
{
	if (x == 1)
		return 1;
	int &res = d[n][x];
	if (res != -1)
		return res;
	res = 0;
	for (int c1 = 0; c1 <= x; c1++)
	{
		int c2 = x - 1 - c1;
		if (c2 > 0)
		{
			int t = D(x, c2) * c[n - x - 1][c1] % P;
			res = (res + t) % P;
		}
	}
	return res;
}

void Solve()
{
	p2[0] = 1;
	FOR(i, 1000 - 1)
		p2[i + 1] = p2[i] * 2 % P;
	int n;
	scanf("%d", &n);
	int res = 0;

	for (int i = 1; i < n; i++)
	{
		int t = D(n, i);
		res = (res + t) % P;
	}

	printf("%d\n", res);

}

int main()
{
	c[0][0] = 1;
	for (int i = 1; i <= 510; i++)
	{
		c[i][0] = 1;
		for (int j = 1; j <= i; j++)
			c[i][j] = ( c[i - 1][j] + c[i - 1][j - 1] ) % P;
	}
	memset(d, 0xFF, sizeof(d));
	freopen("c:\\my\\in.txt", "r", stdin);
	freopen("c:\\my\\out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	FOR(i, t)
	{
		printf("Case #%d: ", i + 1);
		Solve();
	}
	return 0;
}