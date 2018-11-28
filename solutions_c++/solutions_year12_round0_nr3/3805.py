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
const int INF = 1000 * 1000 * 1000, NMAX = 105;

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);    
	ios_base::sync_with_stdio(false);
	srand(time(NULL));
	/*cout << 50 << "\n";
	forn(i, 50) {
		cout << 2000000 << ' ' << 2000000 << "\n";
	}
	return 0;*/
	vector<PII> v;
	for (int i = 1; i <= 2000000; i++) {
		stringstream ss;
		ss << i;
		string s;
		ss >> s;
			
		int l = s.size();			
		set<int> g;
		forn(k, l + 1) {
			s += s[0];
			s.erase(0, 1);				
			stringstream tt(s);
			int m;
			tt >> m;
			if (m >= 1 && m <= 2000000 && m > i) {
				g.insert(m);
			}
		}								
		for(set<int>::iterator iter = g.begin(); iter != g.end(); ++iter) {
			v.pb(mp(i, *iter));
		}
	}		
	int tests;
	cin >> tests;
	forn(test, tests) {		
		int a, b;
		cin >> a >> b;
		int ans = 0;
		forv(i, v) {
			if (v[i].fs >= a && v[i].sc <= b) ++ans;
		}
		cout << "Case #" << test + 1 << ": " << ans << "\n";
	}
    return 0;
}
