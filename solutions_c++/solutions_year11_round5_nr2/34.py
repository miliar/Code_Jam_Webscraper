#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

int n;
vector <int> a;
vector <int> S;

bool check (int ans) {
	S.clear ();
	int px = -inf;
	int i = 0;
	while (i < n) {
		int x = a[i];
		int y = 1;
		while (i + 1 < I a.size() && a[i+1] == a[i]) {
			y ++;
			i ++;
		}
		i ++;
		if (px + 1 != x) {
			if (S.size())
				if (S.back() < ans)
					return 0;
			S.clear ();
		}
		px = x;
		y -= S.size();
		vector <int> S1;
		forn (i, S.size())
			if (y < 0) {
				if (S[i] < ans)
					return 0;
				y ++;
			} else 
				S1.pb (S[i] + 1);
		forn (i, y)
			S1.pb (1);
		S = S1;
	}	
	forn (i, S.size())
		if (S[i] < ans)
			return 0;
	return 1;

}

void calccalc () {
	cin >> n;
	a.resize (n);
	forn (i, n)
		cin >> a[i];
	sort (all (a));
	for (int ans = n; ans >= 0; ans -= 1)
		if (check (ans)) {
			cout << ans << endl;
			return;
		}
	cout << 0 << endl;
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: ", ii+1);
		calccalc ();
	}

	return 0;
}
