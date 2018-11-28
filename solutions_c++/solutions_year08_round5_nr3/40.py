#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
//#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<bool> vb;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))

#define forn(i, x) for (int i = 0; i < int(x); i++)
#define fors(i, x) forn(i, sz(x))

template<typename T> T sqr(T x) { return x * x;            }
template<typename T> T abs(T x) { return (x > 0) ? x : -x; }

int dp[20][5000];
int mask[100];

int get(int x, int y)
{
	if (y < 0) return 0;
	return (x >> y) & 1;
}

void solve(int test_num)
{
	int n, m;
	string f[20];
	cin >> n >> m;
	forn(i, n) cin >> f[i];
	forn(i, n)
	{
		mask[i] = 0;
		forn(j, m) mask[i] = mask[i] * 2 + (f[i][j] == 'x');
	}
	memset(dp, 255, sizeof(dp));
	dp[0][0] = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < (1 << m); j++)
		{
			if (dp[i][j] == -1) continue;
			for (int k = 0; k < (1 << m); k++)
			{
				if (k & mask[i]) continue;
				bool botva = false;
				int num = 0;
				forn(l, m)
				{
					if (!((k >> l) & 1)) continue;
					num++;
					if (get(j, l - 1) || get(j, l + 1) || get(k, l - 1) || get(k, l + 1))
					{
						botva = true;
						break;
					}
				}
				if (!botva && dp[i][j] + num > dp[i + 1][k]) dp[i + 1][k] = dp[i][j] + num;
			}
		}
	}
	int ans = -1;
	forn(i, (1 << m)) ans >?= dp[n][i];
	printf("Case #%d: ", test_num);
	printf("%d\n", ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	for (int it = 1; it <= nt; it++)
		solve(it);
	return 0;
}
