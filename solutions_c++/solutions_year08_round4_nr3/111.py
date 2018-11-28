#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define REP(i,a)    FOR(i,0,a)
#define FORE(i,a)   for(__typeof(a.begin()) i=a.begin();i!=a.end();i++)
#define ZERO(m)     memset(m,0,sizeof(m))
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()
#define LL          long long
#define LD          long double
#define MP          make_pair
#define PII         pair<int, int>
#define X           first
#define Y           second
#define VC          vector
#define VI          VC<int>
#define VVI         VC< VI >
#define VS          VC<string>
#define VPII        VC< PII >
#define DB(a)       cerr << #a << ": " << a << endl;

void print(VI v) {cout << "[";if (v.S) cout << v[0];FOR(i, 1, v.S) cout << ", " << v[i];cout << "]\n";}
void print(VS v) {cout << "[";if (v.S) cout << v[0];FOR(i, 1, v.S) cout << ", " << v[i];cout << "]\n";}
void print(VVI v) {cout << "[ ---";if (v.S) cout << " ", print(v[0]);FOR(i, 1, v.S) cout << " ", print(v[i]);	cout << "--- ]\n";}
void print(PII p) {cout << "{" << p.X << ", " << p.Y << "}";}
void print(VPII v) {cout << "[";if (v.S) print(v[0]);FOR(i, 1, v.S)  cout << ", ", print(v[i]);cout << "]\n";}

template<class T> string i2s(T x) {ostringstream o; o << x; return o.str(); }
VS splt(string s, char c = ' ') {VS rv; int p = 0, np; while (np = s.find(c, p), np >= 0) {if (np != p) rv.PB(s.substr(p, np - p)); p = np + 1;} if (p < s.S) rv.PB(s.substr(p)); return rv;}

int vv[2000][3], p[2000];
int x[2000], y[2000], z[2000];
int n;
int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		cin >> n;
		REP(i, n) cin >> vv[i][0] >> vv[i][1] >> vv[i][2] >> p[i];
		double mn = 1e18;
		VI pr;
		REP(i, 3) pr.PB(i);
		double cc = 1;//1.0 / sqrt(2); 
		do {
			REP(i, n) x[i] = vv[i][pr[0]];
			REP(i, n) y[i] = vv[i][pr[1]];
			REP(i, n) z[i] = vv[i][pr[2]];
			REP(i, n) {
				double l = 0, r = 1e8;
				int az = z[i];
				REP(abc, 500) {
					double s = (l + r) / 2;
					int ok = 1;
					REP(k, n) if (abs(z[k] - az) > s * p[k]) ok = 0;
					if (ok == 0) {
						l = s;
						continue;
					}
					double x1 = -1e10, x2 = 1e10, y1 = -1e10, y2 = 1e10;
					REP(k, n) {
						double left = (s * p[k] - abs(z[k] - az)) * cc;
						x1 >?= x[k] + y[k] - left;
						x2 <?= x[k] + y[k] + left;
						y1 >?= x[k] - y[k] - left;
						y2 <?= x[k] - y[k] + left;
					}

					if (x1 > x2 || y1 > y2) {
						l = s;
					} else
						r = s;
				}
				mn <?= l;
			}
		} while (next_permutation(ALL(pr)));
		printf("%.8f\n", mn);
	}
}
