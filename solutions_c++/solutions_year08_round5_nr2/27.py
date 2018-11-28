#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
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

#define BAD "THE CAKE IS A LIE"
int vs[15][15];
#define PX pair < int, pair <int, int > >
string mp[15];
int wd[15][15];
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};
int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		int sy, sx;
		cin >> sy >> sx;
		REP(i, sy) cin >> mp[i];

		ZERO(wd);
		queue<int> q;
		REP(x, sx) REP(y, sy) if (mp[y][x] == '#') q.push(x), q.push(y), q.push(0);
		REP(y, sy) q.push(0), q.push(y), q.push(1);
		REP(y, sy) q.push(sx - 1), q.push(y), q.push(1);
		REP(x, sx) q.push(x), q.push(0), q.push(1);
		REP(x, sx) q.push(x), q.push(sy - 1), q.push(1);
		while (!q.empty()) {
			int x = q.front(); q.pop();
			int y = q.front(); q.pop();
			int t = q.front(); q.pop();
			if (wd[x][y]) continue;
			wd[x][y] = t;
			REP(d, 4) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				if (nx >= 0 && nx < sx && ny >= 0 && ny < sy && mp[ny][nx] != '#')
					q.push(nx), q.push(ny), q.push(t + 1);
			}
		}

		/*
		cout << endl;
		REP(y, sy) {
				REP(x, sx) 
					cout << wd[x][y];
			cout << endl;
		}*/

		int mn = 1 << 20;
		priority_queue<PX, VC < PX >, greater < PX > > pq;
		REP(y, sy) REP(x, sx) if (mp[y][x] == 'O') pq.push(MP(0, MP(x, y)));
		memset(vs, 0x1f, sizeof vs);
		while (!pq.empty()) {
			PX p = pq.top(); pq.pop();
			int x = p.Y.X;
			int y = p.Y.Y;
			int t = p.X;
			//cout << x << ' ' << y << ' '<<t << endl;
			if (vs[x][y] <= t) continue;
			vs[x][y] = t;

			if (mp[y][x] == 'X') {
				mn = t;
				break;
			}

			REP(d, 4) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				if (nx >= 0 && nx < sx && ny >= 0 && ny < sy && mp[ny][nx] != '#')
					pq.push(MP(t + 1, MP(nx, ny)));

				nx = x;
				ny = y;
				while (nx >= 0 && nx < sx && ny >= 0 && ny < sy && mp[ny][nx] != '#') {
					nx += dx[d];
					ny += dy[d];
				}

				nx -= dx[d];
				ny -= dy[d];

				if (wd[x][y])
					pq.push(MP(t + wd[x][y], MP(nx, ny)));
			}
		}

		
		//cout << endl;
		//REP(i, sy) cout << mp[i] << endl;

		printf("Case #%d: ", atc);
		if (mn == 1 << 20)
			cout << BAD;
		else
			cout << mn;
		cout << endl;
	}
}

