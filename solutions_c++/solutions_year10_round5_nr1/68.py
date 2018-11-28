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

int64 s[1000];
set<int64> ans;
int k;
bool isp[1100000];

void check(int64 a, int64 m) {
	int64 b = ((s[1] - s[0] * a) % m + m) % m;

	for (int i = 1; i < k; i++)
		if (s[i] != (s[i - 1] * a + b) % m)
			return;

	ans.insert((s[k - 1] * a + b) % m);
}

int64 binpow(int64 a, int64 b, int64 m) {
	int64 res = 1;

	while (b)
		if (b & 1) {
			res = res * a % m;
			b--;
		}
		else {
			a = a * a % m;
			b >>= 1;
		}

	return res;
}

void solve() {
	ans.clear();
	int d;
	cin >> d >> k;
	forn(i, k)
		scanf("%d", &s[i]);

	if (k <= 1) {
		puts("I don't know.");
		return;
	}

	int st = 1;
	forn(i, d)
		st *= 10;
	for (int64 m = 2; m < st; m++) {
		if (!isp[m] || m <= s[0])
			continue;

		forn(i, k - 2) {
			int64 a = ((s[i + 2] - s[i + 1]) % m + m) % m * binpow(((s[i + 1] - s[i]) % m + m) % m, m - 2, m) % m;
			check(a, m);
		}
		check(0, m);
		check(1, m);
	}

	if ((int)ans.size() != 1)
		puts("I don't know.");
	else
		printf("%I64d\n", *ans.begin());
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	

	memset(isp, true, sizeof(isp));
	isp[0] = isp[1] = false;

	for (int i = 2; i <= 1000000; i++)
		if (isp[i]) {
			for (int j = 2 * i; j <= 1000000; j += i)
				isp[j] = false;
		}
	
	int tt;
	scanf("%d", &tt);
	forn(ii, tt) {
		cerr << ii + 1 << '/' << tt << endl;

		printf("Case #%d: ", ii + 1);

		solve();
	}

	cerr << clock() << endl;
	
	return 0;
}