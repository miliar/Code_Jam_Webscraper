// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cmath>
#include <queue>
#include <set>
#include <cstring>
using namespace std;

#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;

ifstream inp("B.in");
ofstream out("B.out");

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool removable(vector<int> neighbor, vector<int> cover);
int max_removable(vector<vector<int> > neighbors, vector<int> cover);
vector<int> procedure_1(vector<vector<int> > neighbors, vector<int> cover);
vector<int> procedure_2(vector<vector<int> > neighbors, vector<int> cover, int k);
int solve(vector<vi> &Graph);
int cover_size(vector<int> cover);
//ifstream infile ("graph.txt");
//ofstream outfile ("coloring.txt");

ll p[102][27], n, k;

ll sign(ll x1, ll y1, ll x2, ll y2, ll x, ll y) {
	ll t = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1);
	if (t > 0) return 1;
	if (t == 0) return 0;
	return -1;
}

ll inter(ll x1, ll y1, ll x2, ll y2, ll xx1, ll yy1, ll xx2, ll yy2) {
	ll tmp = sign(x1, y1, x2, y2, xx1, yy1);
	ll tmp2 = sign(x1, y1, x2, y2, xx2, yy2);

	ll tmp3 = sign(xx1, yy1, xx2, yy2, x1, y1);
	ll tmp4 = sign(xx1, yy1, xx2, yy2, x2, y2);

	if (tmp * tmp2 <= 0 && tmp3 * tmp4 <= 0) return 1;
	return 0;
}

bool is_inter(int i, int j) {
	for (int l = 0; l < k - 1; l++) {
		for (int m = 0; m < k - 1; m++) {
			if (inter(l, p[i][l], l + 1, p[i][l + 1], m, p[j][m], m + 1, p[j][m + 1])) {
				return true;
			}
		}
	}
	return false;
}


int color[102], best;
vector<vi> g;

void rec(int cnt, int start, int c) {
	if (c + 1 >= best) {
		return;
	}

	if (cnt == n) {
		if (c + 1 < best) {
			best = c + 1;
		}
		return;
	}

	int im;
	int used[102];
	//vector<pair<int,int> > z;

	for (int i = start; i < n; i++) {
		if (color[i] != -1) {
			continue;
		}
		memset(used, 0, sizeof(used));
		int col = 0;
		for (int j = 0; j < g[i].size(); j++) {
			if (color[g[i][j]] != -1) {
				used[color[g[i][j]]] = 1;
			}
		}
		for (int j = 0; j <= c; j++) {
			if (!used[j]) {
				color[i] = j;
				rec(cnt + 1, i + 1, c);
				color[i] = -1;
			}
		}
		color[i] = c + 1;
		rec(cnt + 1, i + 1, c + 1);
		color[i] = -1;
		break;
	}
}

int solve() {
	memset(color, -1, sizeof(color));
	best = n;
	rec(0, 0, 0);
	return best;
}

int main() {
	int NT;
	inp >> NT;
	for (int t = 1; t <= NT; t++) {
		
		//int n, k;
		
		inp >> n >> k;
		g.clear();

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < k; j++) {
				inp >> p[i][j];
			}
		}
		
		int bb[102][102];
		memset(bb,0,sizeof(bb));
		for (int i =0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (i == j) continue;
				if (is_inter(i, j)) {
					bb[i][j] = bb[j][i] = 1;
				} else {
					bb[i][j] = bb[j][i] = 0;
				}
			}
		}

		//bb[2][0] = bb[0][2] = bb[2][1] = bb[1][2] = 1;

		for (int i = 0; i < n; i++) {
			vi cur;
			for (int j = 0; j < n; j++) {
				if (bb[i][j]) {
					cur.pb(j);
				}
			}
			g.pb(cur);
		}

		cout << "solving...";
		int ans = solve();
		
		out << "Case #" << t << ": " << ans << endl;
		cout << "Case #" << t << ": " << ans << endl;
	}
}