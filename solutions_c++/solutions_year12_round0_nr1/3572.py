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

const ld PI = 3.1415926535897932, EPS = 1E-9;
const int INF = 1000 * 1000 * 1000, NMAX = 100005;
const string b = "yhesocvxduiglbkr tnwjpfma ";
const string u = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);    
	int tests;
	cin >> tests;
	scanf("\n");
	forn(test, tests) {
		string s;
		getline(cin, s);
		cout << "Case #" << test + 1 << ": ";
		forv(i, s)
		if (s[i] == ' ') cout << ' ';
		else cout << u[int(s[i] - 'a')];
		cout << "\n";
	}
    return 0;
}
