#define _CRT_SECURE_NO_DEPRECATE
#define _SECURE_SCL 0

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

char s[110][110];
int cnt[110];
double a[110], b[110], c[110];

void solve() {
	int n;
	scanf("%d", &n);
	forn(i, n)
		scanf("%s", s[i]);

	forn(i, n) {
		cnt[i] = 0;
		int win = 0;
		forn(j, n)
			if (s[i][j] != '.') {
				cnt[i]++;
				if (s[i][j] == '1')
					win++;
			}
		a[i] = double(win) / cnt[i];
	}

	forn(i, n) {
		b[i] = 0;
		forn(j, n)
			if (s[i][j] != '.')
				b[i] += (a[j] * cnt[j] - (s[j][i] - '0')) / (cnt[j] - 1);
		b[i] /= cnt[i];
	}

	forn(i, n) {
		c[i] = 0;
		forn(j, n)
			if (s[i][j] != '.')
				c[i] += b[j];
		c[i] /= cnt[i];
	}

	forn(i, n)
		printf("%.10lf\n", a[i] * 0.25 + b[i] * 0.5 + c[i] * 0.25);
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		printf("Case #%d:\n", ii + 1);
		solve();
	}
	
	return 0;
}