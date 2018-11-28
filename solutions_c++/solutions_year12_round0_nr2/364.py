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
	
	int tests;
	cin >> tests;
	
	REP(tc, tests) {
		int n, s, p, t[200];
		cin >> n >> s >> p;
		FILL(t, 0);
		REP(i, n) {
			cin >> t[i];
		}
		int sol = 0;
		REP(i, n) {
			int x = t[i] / 3;			
			if (t[i] % 3 == 0) {
				if (x >= p) {
					sol++;
					continue;
				}
				if (x + 1 >= p && s > 0 && x > 0) {
					s--;
					sol++;
					continue;
				}
			}
			if (t[i] % 3 == 1) {
				if (x + 1 >= p) {
					sol++;
					continue;
				}
			}
			if (t[i] % 3 == 2) {
				if (x + 1 >= p) {
					sol++;
					continue;
				}
				if (x + 2 >= p && s > 0) {
					s--;
					sol++;
					continue;
				}
			}
		}
		printf("Case #%d: %d\n", tc + 1, sol);
	}
	
	return 0;
}














