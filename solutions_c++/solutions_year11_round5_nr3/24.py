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
#include <cstring>
using namespace std;

#define FOR(i,a,b) for (int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FOREACH(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) ((int)(x).size())

typedef pair<int,int> pi; typedef vector<int> vi; typedef vector<string> vs; typedef long long ll;

int R, C;
string mapa[200];
const ll MOD = 1000003;

vector<pi> to[110][110];
vector<pi> from[110][110];

bool seenleft[110][110];
bool seenright[110][110];
int visleft, visright;

void goright(int i, int j);

void goleft(int i, int j) {
	if (seenleft[i][j]) return;
	seenleft[i][j] = true;
	visleft++;
	REP(k, SZ(to[i][j])) goright(to[i][j][k].first, to[i][j][k].second);
}

void goright(int i, int j) {
	if (seenright[i][j]) return;
	seenright[i][j] = true;
	visright++;
	REP(k, SZ(from[i][j])) goleft(from[i][j][k].first, from[i][j][k].second);
}

int main() {
	int casos;
	cin >> casos;
	REP(caso, casos) {
		cin >> R >> C;
		REP(i, R) cin >> mapa[i];
		REP(i, R) REP(j, C) {
			from[i][j].clear();
			to[i][j].clear();
		}
		REP(i, R) REP(j, C) {
			if (mapa[i][j] == '|') {
				int ni = (i+1)%R, nj = j;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
				from[(i+1)%R][j].pb(make_pair(i,j));
				ni = (i+R-1)%R, nj = j;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
			} else if (mapa[i][j] == '\\') {
				int ni = (i+1)%R, nj = (j+1)%C;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
				ni = (i+R-1)%R, nj = (j+C-1)%C;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
			} else if (mapa[i][j] == '/') {
				int ni = (i+1)%R, nj = (j+C-1)%C;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
				ni = (i+R-1)%R, nj = (j+1)%C;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
			} else if (mapa[i][j] == '-') {
				int ni = i, nj = (j+1)%C;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
				ni = i, nj = (j+C-1)%C;
				to[i][j].pb(make_pair(ni,nj));
				from[ni][nj].pb(make_pair(i,j));
			}
		}
		CLEAR(seenleft, false);
		CLEAR(seenright, false);
		ll res = 1;
		REP(i, R) REP(j, C) if (!seenleft[i][j]) {
			visleft = visright = 0;
			goleft(i, j);
			if (visleft != visright) {
				res = 0;
				break;
			}
			//cout << visleft << "  " << visright << endl;
			res = (res*2)%MOD;
		}
		cout << "Case #" << caso+1 << ": " << res << endl;
	}
	return 0;
}
