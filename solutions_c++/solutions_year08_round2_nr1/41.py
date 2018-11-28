#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
using namespace std;

long long n, a, b, c, d, x0, y0, m;
long long xx[110000];
long long yy[110000];
int nn;

void Load()
{
	scanf("%I64d%I64d%I64d%I64d%I64d%I64d%I64d%I64d", &n, &a, &b, &c, &d, &x0, &y0, &m);
	set<pair<long long, long long> > ws;
	xx[0] = x0;
	yy[0] = y0;
	int i;
	nn = 1;
	ws.insert(make_pair(x0, y0));
	for (i = 1; i < n; i++)
	{
		x0 = (a * x0 + b) % m;
		y0 = (c * y0 + d) % m;
		if (ws.find(make_pair(x0, y0)) == ws.end())
		{
			ws.insert(make_pair(x0, y0));
			xx[nn] = x0;
			yy[nn] = y0;
			nn++;
		}
	}
	n = nn;
}

long long num[9];

void Solve()
{
	memset(num, 0, sizeof(num));
	int i;
	for (i = 0; i < n; i++)
	{
		num[(xx[i] % 3) * 3 + yy[i] % 3]++;
	}
	long long ans = 0;
	int j, k;
	for (i = 0; i < 9; i++)
	{
		for (j = 0; j < 9; j++)
		{
			for (k = 0; k < 9; k++)
			{
				if (((i % 3) + (j % 3) + (k % 3)) % 3 != 0) continue;
				if (((i / 3) + (j / 3) + (k / 3)) % 3 != 0) continue;
				long long cans = 1;
				cans *= num[i];
				num[i]--;
				cans *= num[j];
				num[j]--;
				cans *= num[k];
				num[k]--;
				if (cans > 0) ans += cans;
				num[i]++;
				num[j]++;
				num[k]++;
			}
		}
	}
	cout << ans / 6;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}