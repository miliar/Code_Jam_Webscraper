#pragma comment(linker, "/STACK:128000000")
#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <stack>
#include <cassert>
#include <ctime>
using namespace std;

#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forv(i, v) forn(i, v.size())
#define for1(i, n) for(int i = 1; i <= int(n); i++)

typedef long double ld;
typedef long long ll;
const double pi = M_PI;
const int INF = int(1e7);

struct Point
{
	double x, y;
};

const int SMAX = 1 << 17;
const int NMAX = 100;
vector<int> p[NMAX];

int n, k;

bool g[NMAX][NMAX];

bool can[SMAX];
int d[SMAX];

bool cross(const vector<int>& a, const vector<int>& b)
{
	int p = 0, m = 0;
	forn(i, k)
	{
		if (a[i] == b[i]) return true;
		if (a[i] > b[i]) p++;
		else m++;
	}
	return m > 0 && p > 0;
}

void solve(int tc)
{
	printf("Case #%d: ", tc);

	cin >> n >> k;
	forn(i, n)
	{
		p[i].resize(k);
		forn(j, k)
		{
			cin >> p[i][j];
		}
	}
	
	forn(i, n)
	{
		forn(j, i)
		{
			g[i][j] = g[j][i] = cross(p[i], p[j]);
		}
	}

	forn(mask, 1 << n)
	{

		can[mask] = true;

		forn(i, n)
		{
			if (!(mask & (1 << i))) continue;
			forn(j, i)
			{
				if (!(mask & (1 << j))) continue;
				if (g[i][j])
				{
					can[mask] = false;
					break;
				}
			}
			if (!can[mask]) break;
		}
	}

	forn(i, 1 << n) d[i] = INF;
	d[0] = 0;

	forn(mask, 1 << n)
	{
		if (mask == 0) continue;
		for(int m = mask; m > 0; m = (m-1) & mask)
		{
			assert(d[m ^ mask] != INF);
			if (can[m])
			{
				d[mask] = min(d[mask], d[mask ^ m] + 1);
			}
		}
	}
	printf("%d\n", d[(1<<n)-1]);
}

int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tc;
	cin >> tc;
	forn(i, tc) solve(i+1);

	return 0;
}