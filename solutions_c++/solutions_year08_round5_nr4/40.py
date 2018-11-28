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

const int MOD = 10007;

int H, W, R;
int U[10], V[10];
int pref[101000000];
int inv[20000];

int getMod(int u)
{
	int res = 0;
	while (u) res += u / MOD, u /= MOD;
	return res;
}

int getpow(int a, int b, int c)
{
	int res = 1;
	while (b)
		if (b)
		{
			res = (res * a) % c;
			b--;
		}
		else
		{
			a = (a * a) % c;
			b /= 2;
		}
	return res;
}

int inverse(int x)
{
	return getpow(x, MOD - 2, MOD);
}

int getC(int U, int V)
{
	if (getMod(U) - getMod(V) != getMod(U - V)) return 0;
	int res = (pref[U] * inv[pref[V]]) % MOD;
	res = (res * inv[pref[U - V]]) % MOD;
	return res;
}

int get_ways(int N, int M)
{
	if (!N && !M) return 1;
	if (N <= 0 || M <= 0) return 0;
	int p = 2 * N - M;
	int q = 2 * M - N;
	if (p % 3 || q % 3) return 0;
	p /= 3;
	q /= 3;
	if (p < 0 || q < 0) return 0;
	return getC(p + q, p);
}

void solve(int test_num)
{
	cerr << test_num << "\n";
	cin >> H >> W >> R;
	forn(i, R) cin >> U[i] >> V[i];
	int ans = 0;
	forn(i, 1 << R)
	{
		vector<pair<int, int> > tmp;
		tmp.push_back(mp(1, 1));
		int num = 0;
		forn(j, R) if ((i >> j) & 1) tmp.push_back(mp(U[j], V[j])), num++;
		tmp.push_back(mp(H, W));
		sort(all(tmp));
		int cur = 1;
		fors(j, tmp) if (j != sz(tmp) - 1)
			cur = (cur * get_ways(tmp[j + 1].first - tmp[j].first, tmp[j + 1].second - tmp[j].second)) % MOD;
		if (num % 2) cur = (MOD - cur) % MOD;
		ans = (ans + cur) % MOD;
	}
	printf("Case #%d: ", test_num);
	printf("%d\n", ans);
}


int main()
{
	pref[0] = 1;
	for (int i = 1; i <= 100000000; i++)
	{
		int t = i;
		while (t % MOD == 0) t /= MOD;
		t %= MOD;
		pref[i] = (pref[i - 1] * t) % MOD;
	}
	for (int i = 1; i < MOD; i++)
	{
		inv[i] = inverse(i);
		assert(inv[i]);
	}
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	for (int it = 1; it <= nt; it++)
		solve(it);
	return 0;
}
