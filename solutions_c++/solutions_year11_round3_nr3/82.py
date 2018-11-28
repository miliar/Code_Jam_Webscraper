#include <iostream>
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
#define problem "c"

int n;
LL L, H;
LL a[10010];
LL g[10010];

void Load()
{
	cin >> n >> L >> H;
	for (int i = 0; i < n; i++)
	{
		scanf("%I64d", &a[i]);
	}
}

LL RoundUp(ldb a)
{
	if (fabsl((LL)(a + eps) - a) < eps)
		return (LL)(a + eps);
	else return (LL)(a + eps) + 1;
}

void Solve(int Test)
{
	cout << "Case #" << Test << ": ";
	sort(a, a + n);
	int i;
	g[n] = 0;
	for (i = n - 1; i >= 0; i--)
	{
		g[i] = __gcd(g[i + 1], a[i]);
	}
	bool found = false;
	LL r;
	for (LL k = RoundUp((ldb)g[0] / (ldb)H); k <= g[0] / L; k++)
	{
		if (g[0] % k == 0)
		{
			found = true;
			r = g[0] / k;
		}
	}
	if (found)
	{
		cout << r << "\n";
		return;
	}
	LL nok = 1;
	LL k1, k2, k;
	for (i = 0; i < n - 1; i++)
	{
		nok = nok / __gcd(nok, a[i]) * a[i];
		if (g[i + 1] % nok == 0ll)
		{
			k = g[i + 1] / nok;
			k1 = RoundUp((ldb)L / (ldb)nok);
			if (k1 == 0) k1++;
			k2 = H / nok;
			for (; k1 <= k2; k1++)
			{
				if (k % k1 == 0ll)
				{
					break;
				}
			}
			if (k1 <= k2)
			{
				cerr << k1 << "\n";
				cout << nok * k1 << "\n";
				return;
			}
		}
	}
	cerr << "ok\n";
	nok = nok / __gcd(nok, a[i]) * a[i];
	k1 = RoundUp((ldb)L / (ldb)nok);
	if (k1 == 0) k1++;
	k2 = H / nok;
	if (k1 <= k2)
	{
		nok *= k1;
		cout << nok << "\n";
		return;
	}
	cout << "NO\n";


}

int main()
{
	freopen(problem ".in", "rt", stdin);
	freopen(problem ".out", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		Load();
		Solve(i + 1);
	}
	return 0;
}

