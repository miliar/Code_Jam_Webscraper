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
VS mp;
int res[17][17][17][17][4];
bool done[17][17][17][17][4];
int porx[17][17][4], pory[17][17][4];
int startx, starty, endx, endy;
struct State {
	int x, y, px, py, k;
};
const int inf = 1000000000;
#define RES(state) (res[(state).x][(state).y][(state).px][(state).py][(state).k])
#define DONE(state) (done[(state).x][(state).y][(state).px][(state).py][(state).k])

int main() {
	int ccc;
	cin >> ccc;
	REP(cc,ccc) {
		int n, m;
		cin >> n >> m;
		mp.clear();
		mp.PB(string(m+2,'#'));
		REP(i,n) {
			string line;
			cin >> line;
			mp.PB('#' + line + '#');
		}
		mp.PB(string(m+2,'#'));
		n += 2;
		m += 2;
		REP(i,n) REP(j,m) {
			if (mp[i][j] == 'O') {
				startx = i;
				starty = j;
				mp[i][j] = '.';
			}
			if (mp[i][j] == 'X') {
				endx = i;
				endy = j;
				mp[i][j] = '.';
			}
		}
		REP(i,n) REP(j,m)
			if (mp[i][j] != '#') {
				REP(k,4) {
					int xx = i, yy = j;
					while (xx >= 0 && xx < n && yy >= 0 && yy < m && mp[xx][yy] != '#') {
						xx += dx[k];
						yy += dy[k];
					}
					porx[i][j][k] = xx;
					pory[i][j][k] = yy;
				}
			}
		REP(i,n) REP(j,m) REP(pi,n) REP(pj,m) REP(k,4) {
			res[i][j][pi][pj][k] = inf;
			done[i][j][pi][pj][k] = 0;
		}
		queue<State> q[2];
		q[0].push((State){startx,starty,0,0,0});
		res[startx][starty][0][0][0] = 0;
		while (!q[0].empty() || !q[1].empty()) {
			State s;
			if (!q[0].empty()) {
				s = q[0].front();
				q[0].pop();
			} else {
				s = q[1].front();
				q[1].pop();
			}
			if (DONE(s))
				continue;
			DONE(s) = 1;
			REP(k,4) {
				State ss = (State){s.x,s.y,porx[s.x][s.y][k],pory[s.x][s.y][k],k};
				if (RES(ss) > RES(s)) {
					RES(ss) = RES(s);
					q[0].push(ss);
				}
			}
			REP(k,4) {
				int xx = s.x + dx[k];
				int yy = s.y + dy[k];
				if (mp[xx][yy] == '#') {
					xx = s.px - dx[s.k];
					yy = s.py - dy[s.k];
					if (mp[xx][yy] == '#')
						continue;
				}
				State ss = (State){xx,yy,s.px,s.py,s.k};
				if (RES(ss) > RES(s) + 1) {
					RES(ss) = RES(s) + 1;
					q[1].push(ss);
				}
			}
		}
		int rrr = inf;
		REP(pi,n) REP(pj,m) REP(k,4)
			rrr <?= res[endx][endy][pi][pj][k];
		if (rrr == inf)
			cout << "Case #" << cc+1 << ": THE CAKE IS A LIE" << endl;
		else
			cout << "Case #" << cc+1 << ": " << rrr << endl;
	}
}
