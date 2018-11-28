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

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};

#define MX 12010

char vs[MX][MX];
int x1[MX];
int x2[MX];
int y1[MX];
int y2[MX];

int main() {
	int tc;
	cin >> tc;
	FOR(atc,1,tc+1) {
		printf("Case #%d: ", atc);
		ZERO(vs);
		int n;
		cin >> n;
		int d = 0;
		int x = MX / 2;
		int y = MX / 2;
		int ob = 0;
		int mny = 1 << 20;
		int mnx = 1 << 20;
		REP(i, MX) y1[i] = x1[i] = 1 << 20;
		REP(i, MX) y2[i] = x2[i] = -(1 << 20);
		REP(i, n) {
			string s;
			int k;
			cin >> s >> k;
			REP(j, k) REP(l, s.S) {
				char c = s[l];
				if (c == 'F') {
					x += dx[d];
					y += dy[d];
					vs[x][y] = 1;
					x1[y] <?= x;
					x2[y] >?= x;
					y1[x] <?= y;
					y2[x] >?= y;
					x += dx[d];
					y += dy[d];
					if (y < mny || y == mny && x < mnx)
						mny = y, mnx = x;
				} else if (c == 'L') {
					ob++;
					d = (d + 3) % 4;
				} else {
					ob--;
					d = (d + 1) % 4;
				}
			}
		}

		int no = 0;

		queue<int> q;
		q.push(mnx + 1), q.push(mny + 1);

		while (!q.empty()) {
			int ax = q.front(); q.pop();
			int ay = q.front(); q.pop();
			if (vs[ax][ay]) continue;
			vs[ax][ay] = 2;
			if (vs[ax + 1][ay] == 0 && vs[ax + 2][ay] == 0) q.push(ax + 2), q.push(ay);
			if (vs[ax - 1][ay] == 0 && vs[ax - 2][ay] == 0) q.push(ax - 2), q.push(ay);
			if (vs[ax][ay + 1] == 0 && vs[ax][ay + 2] == 0) q.push(ax), q.push(ay + 2);
			if (vs[ax][ay - 1] == 0 && vs[ax][ay - 2] == 0) q.push(ax), q.push(ay - 2);
		}

		for (int y = 0; y < MX; y += 2) if (x1[y] < x2[y]) for (int x = x1[y] + 1; x <= x2[y] - 1; x += 2) 
			if (vs[x][y] == 0) vs[x][y] = 3, no++;

		for (int x = 0; x < MX; x += 2) if (y1[x] < y2[x]) for (int y = y1[x] + 1; y <= y2[x] - 1; y += 2)
			if (vs[x][y] == 0) vs[x][y] = 3, no++;
/*			
#define SS 20
		FOR(y, MX / 2 - SS, MX / 2 + SS) {
			FOR(x, MX / 2 - SS, MX / 2 + SS)
				cout << (char)(vs[x][y] + '0');
			cout << endl;
		}*/

		cout << no << endl;
	}
}
