#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <queue>
#include <bitset>
//#include <cmath>
#include <sstream>
#include <string>
#include <vector>

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()

using namespace std;

typedef pair<int, int> ii;
typedef long long int64;
typedef vector<int> vi;

template<class T> T abs(T x) {return x > 0 ? x : (-x); }
template<class T> T sqr(T x) {return x * x; }

const int maxn = 500;

int a[maxn][maxn];
int n;

int get(int x, int y)
{
	if (x < 0 || x >= n || y < 0 || y >= n) return -1;
	return a[x][y];
}

bool eq(int x, int y)
{
	if (x == -1 || y == -1) return true;
	return x == y;
}

void reflect1(int x, int y, int x0, int y0, int s, int& xx, int& yy)
{
	x -= x0, y -= y0;
	x += s, y += s;
	xx = y, yy = x;
	xx -= s, yy -= s;
	xx += x0, yy += y0;
}

void reflect2(int x, int y, int x0, int y0, int s, int& xx, int& yy)
{
	x -= x0, y -= y0;
	x += s, y += s;
	xx = 2 * s - y, yy = 2 * s - x;
	xx -= s, yy -= s;
	xx += x0, yy += y0;
}

void Solve()
{
	cin >> n;
	for (int i = 0; i < 2 * n - 1; i++)
	{
		int k = i + 1;
		k = min(k, 2 * n - 1 - i);
		for (int j = 0; j < k; j++)
		{
			int x;
			cin >> x;
			if (i < n)
				a[i - j][j] = x;
			else
				a[n - j - 1][i - n + 1 + j] = x;
		}
	}
	/*
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			cerr << a[i][j] << " ";
		cerr << "\n";
	}
	*/
	int res = 10000000;
	for (int i = -4 * n; i <= 4 * n + 2; i++)
		for (int j = -4 * n; j <= 4 * n + 2; j++)
		{
			bool ok = true;
			int s = n;
			s = max(s, abs(i + 1));
			s = max(s, abs(i - 2 * n + 1));
			s = max(s, abs(j + 1));
			s = max(s, abs(j - 2 * n + 1));
			if (s * s >= res) continue;
			for (int x = i - s; x <= i + s && ok; x++)
			{
				if (x % 2) continue;
				for (int y = j - s; y <= j + s; y++)
				{
					if (y % 2) continue;
					bool bad = false;
					int xx, yy;
					reflect1(x, y, i, j, s, xx, yy);
					if (!eq(get(x / 2, y / 2), get(xx / 2, yy / 2)))
						bad = true;
					reflect2(x, y, i, j, s, xx, yy);
					if (!eq(get(x / 2, y / 2), get(xx / 2, yy / 2)))
						bad = true;
					if (bad)
					{
						ok = false;
						break;
					}
				}
			}
			if (ok) res = s * s;
		}
	res -= n * n;
	cout << res << "\n";
}

int main()
{
	int nc;
	cin >> nc;
	for (int it = 0; it < nc; it++)
	{
		printf("Case #%d: ", it + 1);
		Solve();
	}
	return 0;
}
