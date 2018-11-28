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

const int MAXC = 1000090;

int64 n, p[MAXC], np = 0;
bool pr[MAXC];

void solve() {
	cin >> n;
//	n = 1E12;

	if (n == 1) {
		puts("0");
		return;
	}
/*
	l = INF;
	r = -INF;
	rec(0, 0, 0);
*/
	int64 ans = 1;
	forn(i, np) {
		if (p[i] > n)
			break;
		int64 pw = p[i];
		int st = 0;
		while (pw <= n) {
			pw *= p[i];
			st++;
		}

		ans += st - 1;
	}	

//	cout << l << ' ' << r << endl;
	cout << ans << endl;
}

int main() {
#ifdef RADs_project
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif	

	memset(pr, 1, sizeof(pr));
	pr[0] = pr[1] = false;
	for (int i = 2; i < MAXC; i++)
		if (pr[i]) {
			p[np++] = i;
			for (int j = i + i; j < MAXC; j += i)
				pr[j] = false;
		}
	
	int tt;
	scanf("%d", &tt);
//	tt = 1000;
	forn(ii, tt) {
		cerr << ii << ' ' << clock() << endl;

		printf("Case #%d: ", ii + 1);

		solve();
	}
	
	return 0;
}