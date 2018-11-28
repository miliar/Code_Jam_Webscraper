#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int n, m;
vector<pi> likes[3000];
int wmalt[3000];
bool chosen[3000];
int unmalted[3000];
bool sat[3000];
vi gusta[3000][2];

bool solve() {
	stack<int> v;
	CLEAR(chosen, false);
	REP(i, n) REP(j, 2) gusta[i][j].clear();
	REP(i, m) {
		unmalted[i] = 0; wmalt[i] = -1; sat[i] = false;
		REP(j, SZ(likes[i])) {
			gusta[likes[i][j].first][likes[i][j].second].pb(i);
			if (likes[i][j].second == 1) {
				wmalt[i] = likes[i][j].first;
			} else {
				unmalted[i]++;
			}
		}
		if (unmalted[i] == 0) v.push(i);
	}
	while (!v.empty()) {
		int x = v.top(); v.pop();
		if (!sat[x]) {
			int y = wmalt[x];
			chosen[y] = true;
			REP(i, SZ(gusta[y][1])) {
				sat[gusta[y][1][i]] = true;
			}
			REP(i, SZ(gusta[y][0])) {
				int k = gusta[y][0][i];
				unmalted[k]--;
				if (unmalted[k] == 0 && !sat[k]) {
					if (wmalt[k] != -1) {
						v.push(k);
					} else {
						return false;
					}
				}
			}
		}
	}
	return true;
}

int main() {
	int C;
	int t, flav, bit;
	cin >> C;
	REP(caso, C) {
		cin >> n >> m;
		REP(i, m) {
			likes[i].clear();
			cin >> t;
			REP(j, t) {
				cin >> flav >> bit;
				likes[i].pb(make_pair(flav-1, bit));
			}
		}
		if (solve()) {
			cout << "Case #" << caso+1 << ":";
			REP(i, n) cout << (chosen[i]?" 1":" 0");
			cout << endl;
			
			// CHECK
			/*REP(i, m) {
				bool sati = false;
				REP(j, SZ(likes[i])) {
					if ((likes[i][j].second == 0 && !chosen[likes[i][j].first]) ||
						(likes[i][j].second == 1 && chosen[likes[i][j].first])) {
						sati = true;
						break;
						}
				}
				if (!sati) {
					cout << "ERROR" << endl;
					return -1;
				}
			}
			cout << "TODO BIEN" << endl;*/
			////
			
		} else {
			cout << "Case #" << caso+1 << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
