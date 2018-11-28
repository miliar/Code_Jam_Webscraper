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

char grid[128][128];
double wp[128], owp[128], oowp[128];

double calcWP(char *s, int n) {
	int total = 0, win = 0, i;
	for(i = 0; i < n; i++) {
		if(s[i] != '.') total++;
		if(s[i] == '1') win++;
	}
	if(!total) return 0.00;
	return (double)win / (double)total;
}

double calcOWP(int n, int pl) {
	int i, total = 0, temp;
	double totalWP = 0.;
	for(i = 0; i < n; i++) {
		if(i == pl) continue;
		if(grid[i][pl] != '.') {
			temp = grid[i][pl];
			grid[i][pl] = '.';
			totalWP = totalWP + calcWP(grid[i], n);
			total++;
			grid[i][pl] = temp;
		}
	}
	if(!total) return 0.0;
	else return totalWP / (double)total;
}

double calcOOWP(int n, int pl) {
	int total = 0, i;
	double totalOWP = 0.0;
	for(i = 0; i < n; i++) {
		if(i != pl && grid[i][pl]!='.') {
			total++;
			totalOWP = totalOWP + owp[i];
		}
	}
	if(!total) return 0.0;
	return totalOWP / (double) total;
}

int main() {
	READ("A-large.in");
	WRITE("A-large.out");
	int test, cs = 1, n, i;
	double rpi, eps = 1e-12;
	scanf("%d", &test);
	while(test--) {
		printf("Case #%d:\n", cs++);
		scanf("%d", &n);
		for(i = 0; i < n; i++) {
			scanf("%s", grid[i]);
			wp[i] = calcWP(grid[i], n);
		}
		for(i = 0; i < n; i++) {
			owp[i] = calcOWP(n, i);
		}
		for(i = 0; i < n; i++) {
			oowp[i] = calcOOWP(n, i);
		}
		for(i = 0; i < n; i++) {
			rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			printf("%.10lf\n", rpi + eps);
		}
	}
	return 0;
}
