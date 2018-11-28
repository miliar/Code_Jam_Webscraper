#define _CRT_SECURE_NO_DEPRECATE
#define _USE_MATH_DEFINES
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <ctype.h>
#include <complex>
using namespace std;
#define REP(i,n) for (int i=0,_n=int(n);i<_n;++i)
#define REPD(i,n) for (int i=int(n)-1;i>=0;--i)
#define FOR(i,a,b) for (int _b=int(b),i=int(a);i<=_b;++i)
#define FORD(i,a,b) for(int i=int(a),_b=int(b);i>=_b;--i)
#define FILL(x,v) memset(x,v,sizeof x);
#define MP make_pair
#define x first
#define y second
#define sz(s) int((s).size())
#define pb push_back
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef long long ll;
typedef long double ldb;
template<class T> T sqr(T x) {return x * x;}
template<class T> T abs(T x) {return (x < 0) ? -x : x;}
const double EPS = 1e-9;
const int INF = 1010*1000*1000;

int main () {
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	char a[400];
	
	a['a'] = 'y';
	a['b'] = 'h';
	a['c'] = 'e';
	a['d'] = 's';
	a['e'] = 'o';
	a['f'] = 'c';
	a['g'] = 'v';
	a['h'] = 'x';
	a['i'] = 'd';
	a['j'] = 'u';
	a['k'] = 'i';
	a['l'] = 'g';
	a['m'] = 'l';
	a['n'] = 'b';
	a['o'] = 'k';
	a['p'] = 'r';
	a['q'] = 'z';
	a['r'] = 't';
	a['s'] = 'n';
	a['t'] = 'w';
	a['u'] = 'j';
	a['v'] = 'p';
	a['w'] = 'f';
	a['x'] = 'm';
	a['y'] = 'a';
	a['z'] = 'q';
	a[' '] = ' ';
	
	int n;
	scanf("%d\n", &n);
	REP(i, n) {
		string s;
		getline(cin, s);
		REP(j, sz(s)) {
			s[j] = a[s[j]];
		}
		printf("Case #%d: ", i + 1);
		cout << s << '\n';
	}
	return 0;
}














