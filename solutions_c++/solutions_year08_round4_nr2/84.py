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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	forn(it, nt)
	{
		fprintf(stderr, "%d\n", it);
		int n, m, a;
		cin >> n >> m >> a;
		bool ok = false;
		forn(i, n + 1) forn(j, m + 1)
		forn(k, n + 1) forn(l, m + 1)
		if (i * l - j * k == a)
		{
			if (!ok) printf("Case #%d: %d %d %d %d %d %d\n", it + 1, 0, 0, i, j, k, l);
			ok = true;
		}
		if (!ok) printf("Case #%d: IMPOSSIBLE\n", it + 1);
	}
	return 0;
}
