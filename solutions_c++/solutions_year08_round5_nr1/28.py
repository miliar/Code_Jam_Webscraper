#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define REP(i,n) FOR(i,0,n)
#define REPD(i,n) FORD(i,0,n)
#define VAR(v,w) __typeof(w) v=(w)
#define FORE(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define SIZE(c) ((int)(c).size())
#define MP make_pair
#define FT first
#define SD second
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<double> VD;
typedef vector<LD> VLD;
typedef vector<LL> VLL;
typedef vector<bool> VB;
typedef istringstream ISS;
typedef ostringstream OSS;

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1, 0, -1};
int miny[6010], maxy[6010];
int minx, maxx;
int x, y, k;
int area;

int main() {
	int ccc;
	cin >> ccc;
	REP(cc,ccc) {
		int l;
		cin >> l;
		x = y = k = 0;
		minx = maxx = 0;
		area = 0;
		REP(i,6010)
			miny[i] = 1000000000;
		REP(i,6010)
			maxy[i] = -1000000000;
		REP(ll,l) {
			string s;
			int t;
			cin >> s >> t;
			REP(tt,t) {
				FORE(it,s) {
					switch (*it) {
						case 'L':
							k = ((k+1)&3);
							break;
						case 'R':
							k = ((k+3)&3);
							break;
						case 'F':
							switch (k) {
								case 0:
									area -= y;
									miny[x+3005] <?= y;
									maxy[x+3005] >?= y;
									break;
								case 1:
									area += x;
									break;
								case 2:
									area += y;
									miny[x+3004] <?= y;
									maxy[x+3004] >?= y;
									break;
								case 3:
									area -= x;
									break;
							}
							x += dx[k];
							y += dy[k];
							minx <?= x;
							maxx >?= x;
							break;
						default:
							break;
					}
				}
			}
		}
		VI mi, ma;
		FOR(xx,minx,maxx) {
			mi.PB(miny[xx+3005]);
			ma.PB(maxy[xx+3005]);
		}
		int n = maxx - minx;
		VI left(n), right(n);
		left[0] = ma[0];
		FOR(i,1,n)
			left[i] = (left[i-1] >? ma[i]);
		right[n-1] = ma[n-1];
		REPD(i,n-1)
			right[i] = (right[i+1] >? ma[i]);
		REP(i,n)
			ma[i] = (left[i] <? right[i]);
		left[0] = mi[0];
		FOR(i,1,n)
			left[i] = (left[i-1] <? mi[i]);
		right[n-1] = mi[n-1];
		REPD(i,n-1)
			right[i] = (right[i+1] <? mi[i]);
		REP(i,n)
			mi[i] = (left[i] >? right[i]);
		int hull = 0;
		REP(i,n)
			hull += ma[i] - mi[i];
		cout << "Case #" << cc+1 << ": " << hull - (abs(area)>>1) << endl;
	}
}
