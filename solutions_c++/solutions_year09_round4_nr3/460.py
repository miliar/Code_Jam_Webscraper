#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

template <class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }
typedef long long LL;
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define FORU(i, a) for (int i = a; ; ++i)
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

int n, k, v[100][25];
bool can[100][100], can2[100][1<<16];

bool check(int x, int y) {
	int last1 = v[x][0], last2 = v[y][0];
	FOR(i, 1, k) {
		int next1 = v[x][i], next2 = v[y][i];
		if (next1 == next2 || ((last1 < last2)^(next1 < next2))) return false;
		last1 = next1;
		last2 = next2;
	}
	return true;
}

bool check2(int x, int mask) {
	FORU(i, 0) {
		if (i == n) return true;
		if ((mask&(1<<i)) && !can[i][x]) return false;
	}
}

/*
bool check(const vector<int>& v, int x) {
	FORE(i, v) {
		if (!can[v[i]][x]) return false;
	}
	return true;
}
*/

bool dp[1<<16][26];
int best;

void go(int pos, int total, int cur, int cnt) {
	if (total == (1<<n)-1) {
		best <?= cnt;
		return;
	}
	if (cnt >= best) return;
	if (pos == 0 && cur == 0 && dp[total][cnt]) return;
	dp[total][cnt] = true;
	if (cur == 0) {
		while (total&(1<<pos)) ++pos;
		go(pos+1, total, cur+(1<<pos), cnt);
		return;
	}
	if (pos == n) {
		go(0, total+cur, 0, cnt+1);
		return;
	}
	if (total&(1<<pos)) {
		go(pos+1, total, cur, cnt);
		return;
	}
	go(pos+1, total, cur, cnt);
	if (can2[pos][cur]) go(pos+1, total, cur+(1<<pos), cnt);
	/*
	FORU(i, 0) {
		if (i == n) {
			res <?= go(pos+1, total, cur+(1<<pos));
			break;
		}
		if ((cur&(1<<i)) && !can[i][pos]) break;
	}
	*/
}

int main() {
	int t;
	cin >> t;
	FOR(i, 0, t) {
		cin >> n >> k;
		FOR(j, 0, n) FOR(l, 0, k) cin >> v[j][l];
		FOR(j, 0, n) FOR(l, 0, n) can[j][l] = check(j, l);
		int bound = 1<<n;
		FOR(j, 0, n) FOR(l, 0, bound) can2[j][l] = check2(j, l);
        //FOR(j, 0, n) FOR(l, j+1, n) cout << j << ' ' << l << ' ' << can[j][l] << endl;
        SET(dp, false);
        best = INT_MAX;
        go(0, 0, 0, 0);
		cout << "Case #" << i+1 << ": " << best << endl;








		/*
		vector<bool> vis(n, false);
		int res = 0, cnt = 0;
		while (cnt < n) {
			++res;
			FORU(j, 0) {
				if (!vis[j]) {
					vector<int> comp(1, j);
					vis[j] = true;
					++cnt;
					FORE(l, comp) {
						int cur = comp[l];
						FOR(m, 0, n) {
							if (can[cur][m] && !vis[m] && check(comp, m)) {
								comp.push_back(m);
								vis[m] = true;
								++cnt;
							}
						}
					}
					//FORE(l, comp) cout << comp[l] << endl;
					//cout << "---\n";
					break;
				}
			}
		}
		*/
		//cout << "Case #" << i+1 << ": " << res << endl;
	}
}
