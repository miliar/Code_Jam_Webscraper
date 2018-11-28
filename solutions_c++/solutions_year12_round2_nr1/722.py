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
#define mp make_pair
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
const int INF = 1010 * 1000 * 1000;

int main () {
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);	
	//freopen("Input.txt", "r", stdin);freopen("Output.txt", "w", stdout);
	
	int test;
	cin >> test;
	REP(tc, test) {
		int n, x = 0;
		cin >> n;
		vector<int> s(n, 0);
		REP(i, n) {
			cin >> s[i];
			x += s[i];
		}
		vector<double> a(n, 0.0);
		REP(i, n) {
			double l = 0.0, r = 1.0;
			REP(bin, 75) {
				double m = (l + r) / 2.0;
				double v = x * m + s[i];
				double c = m;
				REP(j, n) {
					if (i == j)
						continue;
					if (s[j] < v) {
						c += (v - s[j]) / double(x);
					}
				}
				if (c > 1.0) {
					r = m;
				}
				else {
					l = m;
				}
			}
			a[i] = l;
		}
		printf("Case #%d:", tc + 1);
		REP(i, n) {
			printf(" %.9lf", a[i] * 100.0);
		}
		printf("\n");
	}
	
	
	return 0;
}

















