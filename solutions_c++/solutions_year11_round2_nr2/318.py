/*
USER:
TASK:
ALGO:
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

double pos[1048576], temp[1048576], must; int tp;

bool possible(double d) {
	temp[0] = pos[0] - d;
	for(int i = 1; i < tp; i++) {
		if(temp[i-1] + must > pos[i] + EPS) {
			if(fabs(temp[i-1] + must - pos[i]) > d + EPS) return false;
			temp[i] = temp[i-1] + must;
		}
		else {
			if(fabs(temp[i-1] + must - pos[i]) > d + EPS) temp[i] = pos[i] - d;
			else temp[i] = temp[i-1] + must;
		}
	}
	return true;
}

double search(double st, double en) {
	double mid;
	int prec = 100;
	while(prec--) {
		mid = 0.5*(st + en);
		if(possible(mid)) en = mid;
		else st = mid;
	}	
	return mid;
}

int main() {
	READ("B-large.in");
	WRITE("B-large.out");
	int test, cs = 1, c, p, v, i;
	double ret;
	scanf("%d", &test);
	while(test--) {
		printf("Case #%d:", cs++);
		scanf("%d %lf", &c, &must);
		for(i = tp = 0; i < c; i++) {
			scanf("%d %d", &p, &v);
			while(v--) pos[tp++] = (double)p;
		}
		ret = search(0.0, 1e19);
		printf(" %.10lf\n", ret + EPS);
	}
	return 0;
}
