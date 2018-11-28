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

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

enum {TOP = 1, RIGHT = 2, BOTTOM = 4, LEFT = 8};
int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};

int L;
char mark[300][300];
string S;
int T;
int minx, miny, maxx, maxy;

int main() {
	int nx, ny;
	int casos, res;
	cin >> casos;
	REP(caso, casos) {
		int x = 150, y = 150, dir = 0;
		minx = maxx = x; miny = maxy = y;
		CLEAR(mark, 0);
		cin >> L;
		REP(lecturas, L) {
			cin >> S >> T;
			REP(veces, T) {
				REP(i, SZ(S)) {
					if (S[i] == 'F') {
						nx = x+dx[dir]; ny = y+dy[dir];
						if (ny != y) {
							int vy = min(y,ny);
							mark[x][vy] |= LEFT;
							mark[x-1][vy] |= RIGHT;
						} else {
							int vx = min(x,nx);
							mark[vx][y] |= BOTTOM;
							mark[vx][y-1] |= TOP;
						}
						x = nx; y = ny;
						minx <?= x; maxx >?= x;
						miny <?= y; maxy >?= y;
						//printf("%d %d\n", x, y);
					} else if (S[i] == 'L') {
						dir = (dir+3)%4;
					} else if (S[i] == 'R') {
						dir = (dir+1)%4;
					}
				}
			}
		}
		res = 0;
		for (x=minx-2; x<=maxx+2; x++) for (y=miny-2; y<=maxy+2; y++) {
		//REP(x, 300) REP(y, 300) {
			int p[4] = {0,0,0,0};
			for (nx = x; nx >= 0; nx--) if (mark[nx][y] & LEFT) p[0]++;
			for (nx = x; nx < 300; nx++) if (mark[nx][y] & RIGHT) p[1]++;
			for (ny = y; ny >= 0; ny--) if (mark[x][ny] & BOTTOM) p[2]++;
			for (ny = y; ny < 300; ny++) if (mark[x][ny] & TOP) p[3]++;
			if ((p[0]%2) == 0 && ((p[0] && p[1]) || (p[2] && p[3]))) res++;
		}
		cout << "Case #" << caso+1 << ": " << res << endl;
	}
	return 0;
}
