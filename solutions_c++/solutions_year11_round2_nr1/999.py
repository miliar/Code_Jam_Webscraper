#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <set>
#define LL long long
#define ldb long double
#define sqr(a) ((a) * (a))
#define nextLine() {int c = 0; while((c = getchar()) != 10 && c != EOF);}
#define addEdge(a, b) next[edges] = first[a]; first[a] = edges; end[edges] = a;
#define debug(a) cerr << #a << " = " << a << " ";
#define debugl(a) cerr << #a << " = " << a << "\n";
const ldb eps = 1e-9;
const ldb pi = fabsl(atan2(0.0, -1.0));
const LL LINF = 1ll << 60;
const ldb LDINF = 1e42;
const int INF = 0x7f7f7f7f;
using namespace std;
#define problem "a"

int a[110][110];
int n;

void Load()
{
	cin >> n;
	nextLine();
	int i, j;
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < n; j++)
		{
			a[i][j] = getchar();
		}
		nextLine();
	}
}

ldb res[110][110];
int cnt[110];
int wins[110];

ldb calc(int a, int b)
{
	if (b == 0)
	{
		cerr << "A!\n";
		return 1;
	}
	return (ldb) a / (ldb) b;
}

ldb calcWP(int i)
{
	cnt[i] = 0;
	wins[i] = 0;
	for (int j = 0; j < n; j++)
	{
		if (a[i][j] == '1')
			wins[i]++;
		if (a[i][j] == '1' || a[i][j] == '0')
			cnt[i]++;
	}
	return calc(wins[i], cnt[i]);
}

ldb WP[110], OWP[110], OOWP[110];

void Solve(int Test)
{
	cout << "Case #" << Test << ":\n";
	int i;
	for (i = 0; i < n; i++)
	{
		WP[i] = calcWP(i);
	}
	int cc;
	ldb OOWP = 0;
	for (i = 0; i < n; i++)
	{
		OWP[i] = 0;
		cc = 0;
		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '.') continue;
			cc++;
			if (a[j][i] == '0')
			{
				OWP[i] += calc(wins[j], cnt[j] - 1);
			}
			else if (a[j][i] == '1')
			{
				OWP[i] += calc(wins[j] - 1, cnt[j] - 1);
			}
		}
		if (cc == 0)
		{
			cerr << "A!\n";
			OWP[i] = 1;
		}
		else OWP[i] /= cc;
	}
	for (int i = 0; i < n; i++)
	{
		cc = 0;
		OOWP = 0;
		for (int j = 0; j < n; j++)
		{
			if (a[i][j] == '0' || a[i][j] == '1')
			{
				OOWP += OWP[j];
				cc++;
			}
		}
		if (cc == 0) OOWP = 1;
		else OOWP /= cc;
		cout << 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP << "\n";
	}

}

int main()
{
	freopen(problem ".in", "rt", stdin);
	freopen(problem ".out", "wt", stdout);
	cout << setprecision(15) << fixed;
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		Load();
		Solve(i + 1);
	}
	return 0;
}

