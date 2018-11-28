#pragma comment(linker, "/stack:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES

#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <iomanip>
#include <utility>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define debug(x) cerr << #x << " = " << x << endl;
#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(a, b) make_pair((a), (b))
#define X first
#define Y second
#define ft first
#define sc second

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

typedef long double ld;
typedef pair<ld, ld> ptd;
typedef pair <int, int> pt;
typedef long long li;
typedef unsigned char byte;

const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-9;
const int INF = 1000 * 1000 * 1000;

const int N = 13;

int n, m, d;
int a[N][N];

bool check (int x, int y, int k)
{
	forn(i, k / 2)
	{
		int s1 = 0, s2 = 0;
		
		forn(j, k)
		{
			s1 += a[x + i][y + j];
			s2 += a[x + k - 1 - i][y + j];
		}
		
		if (i == 0)
		{
			s1 -= a[x][y] + a[x][y + k - 1];
			s2 -= a[x + k - 1][y] + a[x + k - 1][y + k - 1];
		}
		
		if (s1 != s2)	
			return false;
	}
	
	forn(j, k / 2)
	{
		int s1 = 0, s2 = 0;
		
		forn(i, k)
		{
			s1 += a[x + i][y + j];
			s2 += a[x + i][y + k - 1 - j];
		}
		
		if (j == 0)
		{
			s1 -= a[x][y] + a[x + k - 1][y];
			s2 -= a[x][y + k - 1] + a[x + k - 1][y + k - 1];
		}
		
		if (s1 != s2)	
			return false;
	}
	
	return true;
}

int solve ()
{
	int ans = 0;

	forn(i, n)
		forn(j, m)
			for (int k = min(n - i, m - j); k >= 3; k--)
			{
				if (k <= ans)
					break;
			
				if (check(i, j, k))
					ans = k;
			}
			
	return ans;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int testCount;
	cin >> testCount;
	
	forn(test, testCount)
	{
		cin >> n >> m >> d;
		
		forn(i, n)
		{
			char buf[100];
			scanf("%s", buf);
			
			forn(j, m)
				a[i][j] = d + (buf[j] - '0');
		}
		
		int ans = solve();
		
		printf("Case #%d: ", test + 1);
		
		if (ans == 0)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}

	return 0;
}
























































