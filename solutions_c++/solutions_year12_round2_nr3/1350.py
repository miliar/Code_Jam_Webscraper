#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/stack:67108864")

#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <stack>
#include <queue>
#include <string>
#include <iomanip>
#include <sstream>
#include <cassert>
#include <iostream>

#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

#define forn(i, n) for(register int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())

#define pb push_back
#define mp make_pair
#define fs first
#define sc second

#define all(v) (v).begin(), (v).end()
#define correct(x, y, n, m) ((x) >= 0 && (x) < (n) && (y) >= 0 && (y) < (m))

template <class T> inline T abs(T a) { return (a) > 0 ? (a) : -(a); }
template <class T> inline T sqr(T a) { return (a) * (a); }

typedef long double ld;
typedef pair <ld, ld> pt;
typedef pair <int, int> PII;
typedef vector <int> VI;
typedef long long LL;

const ld PI = 3.1415926535897932, EPS = 1E-9;
const int INF = 1000 * 1000 * 1000, NMAX = 25;

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    forn(test, tests) {
    	cout << "Case #" << test + 1 << ": \n";
    	int n;
    	cin >> n;
    	int a[NMAX];
    	forn(i, n) {
	    	cin >> a[i];
	    }
    	forn(mask, 1 << n) {
    		int sum = 0;
    		forn(i, n)
    		if (mask & (1 << i)) sum += a[i];
    		for (int m = mask; m; m = (m - 1) & mask) {
    			int s = 0;
    			forn(i, n)
    			if (m & (1 << i)) s += a[i];
    			if (s == sum - s) {
    				forn(i, n)
	    			if (m & (1 << i)) cout << a[i] << ' ';
	    			cout << "\n";
					forn(i, n)
	    			if ((mask ^ m) & (1 << i)) cout << a[i] << ' ';
	    			goto done;
    			}
    		}
    	}
    	cout << "Impossible";
    	done:
    	cout << "\n";
    }
    return 0;
}
