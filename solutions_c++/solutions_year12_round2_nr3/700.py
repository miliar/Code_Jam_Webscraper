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
		
		int n, nmax = 0;
		cin >> n;
		vector<int> s(n, 0);
		REP(i, n) {
			cin >> s[i];
			nmax += s[i];
		}
		
		int sol1 = 0, sol2 = 0;
		bool found = false;
		
		vector<int> mask(100010 * 50, 0);
		REP(k, 20) {
			if (mask[s[k]] > 0) {
				sol1 = (1 << k);
				sol2 = mask[s[k]];
				found = true;
				break;
			}
			else {
				mask[s[k]] = (1 << k);
			}
			FOR(i, 1, nmax) {
				if (mask[i] > 0 && (mask[i] & (1 << k)) == 0) {
					int to = i + s[k];
					if (mask[to] > 0 && (mask[to] & mask[i]) == 0) {
						sol1 = mask[to];
						sol2 = (mask[i] | (1 << k));
						found = true;
						break;
					}
					else {
						mask[to] = (mask[i] | (1 << k));
					}
				}
			}
			if (found)
				break;
		}
		
		printf("Case #%d:\n", tc + 1);
		if (!found) {
			printf("Impossible\n");
		}
		else {
			vector<int> o1, o2;
			REP(k, 25) {
				if (((1 << k) & sol1) > 0) {
					o1.pb(s[k]);
				}
				if (((1 << k) & sol2) > 0) {
					o2.pb(s[k]);
				}
			}
			REP(i, sz(o1) - 1) {
				printf("%d ", o1[i]);
			}
			printf("%d\n", o1.back());
			REP(i, sz(o2) - 1) {
				printf("%d ", o2[i]);
			}
			printf("%d\n", o2.back());
			
		}
	}
	
	
	return 0;
}

















