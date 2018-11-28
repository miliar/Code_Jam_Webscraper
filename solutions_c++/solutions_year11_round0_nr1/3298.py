/*
TASK: Q2011A
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
	//READ("A-large.in");
	//WRITE("A-large.out");
	int test, cs = 1, n, p, i, j, total, bp, op, fi, fj;
	string s;
	vector< pii > blue, orange;
	cin >> test;
	while(test--) {
		cin >> n;
		blue.clear();
		orange.clear();
		for(i = 0; i < n; i++) {
			cin >> s >> p;
			if(s == "O") orange.PB(pii(i, p));
			else blue.PB(pii(i, p));
		}
		bp = op = 1; i = j = 0;
		for(total = 0; i < SZ(orange) || j < SZ(blue); ) {
			total++; fi = fj = 0;
			if(i < SZ(orange)) {
				if(j >= SZ(blue) || orange[i].ff < blue[j].ff) {
					if(op < orange[i].ss) op++;
					else if(op > orange[i].ss) op--;
					else fi++;
				}
				else {
					if(op < orange[i].ss) op++;
					else if(op > orange[i].ss) op--;
				}
			}
			
			if(j < SZ(blue)) {
				if(i >= SZ(orange) || blue[j].ff < orange[i].ff) {
					if(bp < blue[j].ss) bp++;
					else if(bp > blue[j].ss) bp--;
					else fj++;
				}
				else {
					if(bp < blue[j].ss) bp++;
					else if(bp > blue[j].ss) bp--;
				}
			}
			i += fi; j += fj;
		}
		printf("Case #%d: %d\n", cs++, total);
	}
	return 0;
}
