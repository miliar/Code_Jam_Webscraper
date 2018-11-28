#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); i++)

const int maxn = 200;

int max(int a, int b, int c)
{
	return max(max(a, b), c);
}
int min(int a, int b, int c)
{
	return min(min(a, b), c);
}

bool ok(int a, int b, int c)
{
	return max(a, b, c) - min(a, b, c) <= 2;
}
bool surpr(int a, int b, int c)
{
	return max(a, b, c) - min(a, b, c) == 2;
}

bool can[maxn][maxn], cans[maxn][maxn];

void precomp()
{
	forn(i, 11) forn(j, 11) forn(k, 11) if (ok(i, j, k))
	{
		if (surpr(i, j, k))
			cans[i+j+k][max(i, j, k)] = 1;
		else
			can[i+j+k][max(i, j, k)] = 1;
	}
	forn(i, maxn) for (int j = 9; j >= 0; --j)
	{
		can[i][j] |= can[i][j+1];
		cans[i][j] |= cans[i][j+1];
	}
}

void relax(int& a, int b) {a = max(a, b);}

int n, s, p, a[maxn];
int d[maxn][maxn];
int solve()
{
	cin >> n >> s >> p;
	forn(i, n) cin >> a[i];
	
	forn(i, maxn) forn(j, maxn) d[i][j] = -1;
	d[0][s] = 0;
	
	forn(i, n) forn(j, s+1) if (d[i][j] != -1)
	{
		relax(d[i+1][j], d[i][j]);
		if (j && cans[a[i]][0])
			relax(d[i+1][j-1], d[i][j]);
		if (can[a[i]][p])
			relax(d[i+1][j], d[i][j] + 1);
		if (j && cans[a[i]][p])
			relax(d[i+1][j-1], d[i][j] + 1);
	}
	return max(0, d[n][0]);
}

int main()
{
	precomp();
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	cin >> t;
	forn(i, t)
		cout << "Case #" << i+1 << ": " << solve() << endl;
		
	return 0;
}
