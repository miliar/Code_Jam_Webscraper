#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cctype>
#include <sstream>
#include <cassert>
#include <bitset>
#include <memory.h>

using namespace std;

#pragma comment(linker, "/STACK:200000000")

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define fore(i, a, n) for(int i = (int)(a); i < (int)(n); i++)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) (int(a.size()) - 1)
#define all(a) a.begin(), a.end()

const double EPS = 1E-9;
const int INF = 1000000000;
const int64 INF64 = (int64) 1E18;
const double PI = 3.1415926535897932384626433832795;

int sz[11000];
string s[11000];

bool sym(int n, int x, int y) {
	forn(i, 2 * n - 1)
		forn(j, 2 * n - 1)
			if (s[i][j] != ' ') {
				int nx = 2 * x - i;
				int ny = j;

				if (0 <= nx && nx < 2 * n - 1 && 0 <= ny && ny < 2 * n - 1 && s[nx][ny] != ' ' && s[nx][ny] != s[i][j])
					return false;

				nx = i;
				ny = 2 * y - j;

				if (0 <= nx && nx < 2 * n - 1 && 0 <= ny && ny < 2 * n - 1 && s[nx][ny] != ' ' && s[nx][ny] != s[i][j])
					return false;
			}
	return true;
}

void solve() {
	int n;
	scanf("%d", &n);
	getline(cin, s[0]);
	forn(i, 2 * n - 1) {
		getline(cin, s[i]);
		while ((int)s[i].size() < 2 * n - 1)
			s[i] += " ";
	}

	for (int i = 1; i <= 1000; i++)
		sz[i] = i * i;

	int ans = INF;
	forn(i, 2 * n - 1)
		forn(j, 2 * n - 1)
			if (sym(n, i, j))
				ans = min(ans, sz[n + abs(n - 1 - i) + abs(n - 1 - j)] - sz[n]);

	cout << ans;
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		printf("Case #%d: ", ii + 1);

		solve();

		puts("");
	}
	
	return 0;
}