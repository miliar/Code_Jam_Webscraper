#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <bitset>

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define sz(v) ((int)(v.size()))

using namespace std;

typedef long long int64;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<string> vs;

template<class T> T abs(T x){ return x > 0 ? x : (-x); }
template<class T> T sqr(T x){ return x * x; }

const int maxn = 200;

int n, k;
int a[maxn][maxn];

bool c[maxn][maxn];

bool Less(int x, int y, int z)
{
	for (int i = 0; i < z; i++)
		if (a[x][i] > a[y][i]) return false;
	return true;
}

bool eq(int x, int y, int z)
{
	for (int i = 0; i < z; i++)
		if (a[x][i] != a[y][i]) return false;
	return true;
}

void solve(int testnum)
{
	printf("Case #%d: ", testnum + 1);
	cin >> n >> k;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < k; j++)
			cin >> a[i][j];
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			c[i][j] = true;
			for (int t = 0; t < k; t++)
			{
				if (a[i][t] >= a[j][t])
				{
					c[i][j] = false;
					break;
				}
			}
		}
	/*
	vector<vi> v;
	v.pb(vi());
	for (int i = 0; i < n; i++)
		v[0].pb(i);
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++)
			if (!Less(v[0][i], v[0][j], 1))
				swap(v[0][i], v[0][j]);
	for (int i = 1; i < k; i++)
	{
		vector<vi> w;
		for (int j = 0;  j < sz(v); j++)
		{
			vi cur = v[j];
			for (int p = 0; p < sz(cur); p++)
				for (int q = p + 1; q < sz(cur); q++)
					if (eq(cur[p], cur[q], i) && !Less(cur[p], cur[q], i + 1))
						swap(cur[p], cur[q]);
			vi u(sz(cur), 0);
			while (1)
			{
				vi tmp;
				for (int t = 0; t < sz(cur); t++)
				{
					if (u[t]) continue;
					if (!sz(tmp))
					{
						tmp.pb(cur[t]);
						u[t] = 1;
						continue;
					}
					if (Less(tmp[sz(tmp) - 1], cur[t], i + 1))
					{
						tmp.pb(cur[t]);
						u[t] = 1;
					}
				}
				if (!sz(tmp)) break;
				w.pb(tmp);
			}
		}
		v = w;
	}
	int res = 0;
	for (int i = 0; i < sz(v); i++)
	{
		int cur = 0;
		for (int j = 0; j < sz(v[i]); j++)
		{
			int tmp = 0;
			for (int t = 0; t < sz(v[i]); t++)
				if (!c[v[i][j]][v[i][t]] && !c[v[i][t]][v[i][j]])
					tmp++;
			cur = max(cur, tmp);
		}
		res += cur;
	}
	*/
	int res = 0;
	for (int mask = 0; mask < (1 << n); mask++)
	{
		bool ok = true;
		for (int i = 0; i < n; i++)
		{
			if (! ((mask >> i) & 1)) continue;
			for (int j = i + 1; j < n; j++)
			{
				if (! ((mask >> j) & 1)) continue;
				if (c[i][j] || c[j][i]) ok = false;
			}
		}
		if (ok)
		{
			int x = mask;
			int cur = 0;
			while (x)
			{
				cur += x % 2;
				x /= 2;
			}
			res = max(res, cur);
		}
	}
	cout << res;
	printf("\n");
}

int main()
{
//	freopen("", "r", stdin);
//	freopen("", "w", stdout);
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		solve(it);
	}
	return 0;
}
