#include<iostream>
#include<sstream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<string>
#include<queue>
#include<algorithm>
using namespace std;
typedef vector<int>VI;typedef vector<VI>VVI;
typedef vector<string>VS;
typedef pair<int,int>PII;
#define FOR(i,n) for((i)=0;(i)<(n);(i)++)
#define FORN(i,n) for((i)=(n)-1;(i)>=0;(i)--)
#define BE(a) ((a).begin()),((a).end())
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define FORIT(i,a) for((i)=(a).begin();(i)!=(a).end();(i)++)
#define CLR(a,v) memset((a),(v),sizeof(a))

int di[] = {-1,+1, 0, 0};
int dj[] = { 0, 0,-1,+1};

char g[17][17];
int n, m;
int dist[17][17][17][17];
int shr[17][17][4], shc[17][17][4];
deque <VI> qu, nqu;

inline VI make_vi(int i, int j, int r, int c) {
	VI ret(4);
	ret[0] = i; ret[1] = j; ret[2] = r; ret[3] = c;
	return ret;
}

inline void parse_vi(VI v, int & i, int & j, int & r, int & c) {
	i = v[0]; j = v[1]; r = v[2]; c = v[3];
}

int main() {
	int ans, cases, casen, si, sj, i, j, r, c, ni, nj, nr, nc, d;
	VI cur, next;
	cin >> cases;
	for (casen = 1; casen <= cases; casen++) {
		CLR(g, '#');
		cin >> n >> m;
		FOR (i,n) FOR (j,m) cin >> g[1 + i][1 + j];
		n += 2; m += 2;
		CLR(dist, 128);
		FOR (i,n) FOR (j,m) FOR (d,4) {
			shr[i][j][d] = shc[i][j][d] = -1;
			if (g[i][j] == '#') continue;
			ni = i; nj = j;
			while (g[ni][nj] != '#') {
				ni += di[d];
				nj += dj[d];
			}
			ni -= di[d];
			nj -= dj[d];
			shr[i][j][d] = ni;
			shc[i][j][d] = nj;
		}
		FOR (si,n) FOR (sj,m) if (g[si][sj] == 'O') goto sfin;
sfin:
		dist[si][sj][0][0] = 0;
		qu.clear();
		qu.PB(make_vi(si, sj, 0, 0));
		ans = -1;
		while (!qu.empty()) {
			nqu.clear();
			while (!qu.empty()) {
				cur = qu.front();
				qu.pop_front();
				parse_vi(cur, i, j, r, c);
				if (g[i][j] == 'X') {
					ans = dist[i][j][r][c];
					goto fin;
				}
				// Shoot
				FOR (d,4) if (shr[i][j][d] >= 0) {
					ni = i; nj = j;
					nr = shr[i][j][d]; nc = shc[i][j][d];
					if (dist[ni][nj][nr][nc] < 0) {
						dist[ni][nj][nr][nc] = dist[i][j][r][c];
						qu.PB(make_vi(ni, nj, nr, nc));
					}
				}
				// Move
				FOR (d,4) {
					ni = i + di[d];
					nj = j + dj[d];
					nr = r; nc = c;
					if (g[ni][nj] == '#') continue;
					if (dist[ni][nj][nr][nc] < 0) {
						dist[ni][nj][nr][nc] = dist[i][j][r][c] + 1;
						nqu.PB(make_vi(ni, nj, nr, nc));
					}
				}
				// Teleport
				if (r != 0 || c != 0) {
					FOR (d,4) {
						ni = i + di[d];
						nj = j + dj[d];
						if (g[ni][nj] == '#') break;
					}
					if (d < 4) {
						ni = r; nj = c;
						nr = r; nc = c;
						if (dist[ni][nj][nr][nc] < 0) {
							dist[ni][nj][nr][nc] = dist[i][j][r][c] + 1;
							nqu.PB(make_vi(ni, nj, nr, nc));
						}
					}
				}
			}
			qu = nqu;
		}
		fin:
		cout << "Case #" << casen << ": ";
		if (ans < 0) cout << "THE CAKE IS A LIE";
		else cout << ans;
		cout << endl;
	}
	return 0;
}
