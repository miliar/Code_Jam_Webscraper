/*
TASK: Q2011B
ALGO: simulation
USER: zobayer1
*/
/*
#pragma warning (disable: 4786)
#pragma comment (linker, "/STACK:0x800000")
*/
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
#include <utility>
using namespace std;

template< class T > T _abs(T n) { return (n < 0 ? -n : n); }
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }
template< class T > T sq(T x) { return x * x; }
template< class T > T gcd(T a, T b) { return (b != 0 ? gcd<T>(b, a%b) : a); }
template< class T > T lcm(T a, T b) { return (a / gcd<T>(a, b) * b); }
template< class T > bool inside(T a, T b, T c) { return a<=b && b<=c; }

#define MP(x, y) make_pair(x, y)
#define REV(s, e) reverse(s, e)
#define SET(p) memset(p, -1, sizeof(p))
#define CLR(p) memset(p, 0, sizeof(p))
#define MEM(p, v) memset(p, v, sizeof(p))
#define CPY(d, s) memcpy(d, s, sizeof(s))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define SZ(c) (int)c.size()
#define PB(x) push_back(x)
#define ff first
#define ss second
#define i64 long long
#define ld long double
#define pii pair< int, int >
#define psi pair< string, int >

const double EPS = 1e-9;
const int INF = 0x7f7f7f7f;

int main() {
	//READ("B-small-attempt0.in");
	//WRITE("B-small-attempt0.out");
	int test, cs = 1, com, i, opp, n, sz;
	map< string, char > M;
	map< string, char >::iterator it;
	map< char, char > Opp;
	map< char, char >::iterator ot;
	vector< char > R;
	vector< char >::iterator vt;
	string s, r;
	cin >> test;
	while(test--) {
		cin >> com;
		M.clear();
		Opp.clear();
		R.clear();
		for(i = 0; i < com; i++) {
			cin >> s;
			r = s; swap(r[0], r[1]);
			//cout << s.substr(0,2) << ' ' << r.substr(0,2) << endl;
			M.insert(MP(s.substr(0,2), s[2]));
			M.insert(MP(r.substr(0,2), r[2]));
		}
		cin >> opp;
		for(i = 0; i < opp; i++) {
			cin >> s;
			Opp.insert(MP(s[0], s[1]));
			Opp.insert(MP(s[1], s[0]));
		}
		cin >> n >> s;
		for(i = 0; i < n; i++) {
			R.PB(s[i]);
			if((sz=SZ(R)) >= 2) {
				r = ""; r += R[sz-2]; r += R[sz-1];
				it = M.find(r);
				if(it != M.end()) {
					R.pop_back();
					R.pop_back();
					R.PB(it->second);
				}
				else {
					ot = Opp.find(s[i]);
					if(ot != Opp.end()) {
						vt = find(R.begin(), R.end()-1, ot->second);
						if(vt != R.end()-1) R.clear();
					}
				}
			}
		}
		printf("Case #%d: [", cs++);
		for(i = 0; i < SZ(R); i++) {
			if(i) printf(", ");
			printf("%c", R[i]);
		}
		printf("]\n");
	}
	return 0;
}
