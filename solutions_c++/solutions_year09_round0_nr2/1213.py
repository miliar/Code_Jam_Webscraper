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

struct point{
	int h, i, j;
};

int T, N, M;
char ans[102][102];
int a[102][102], ind[102][102];
int p[10002], h[10002], u[102][102], color[102][102], label[10002];
const int di[4] = {-1, 0, 0, 1};
const int dj[4] = {0, -1, 1, 0};

void initialize() {
	memset(a, 0, sizeof(a));
	memset(u, 0, sizeof(u));
	memset(ans, 0, sizeof(ans));
	memset(ind, 0, sizeof(ind));
	memset(label, -1, sizeof(label));
}

int get_parent(int i) {
	if (p[i] == i) {
		return i;
	}
	return p[i] = get_parent(p[i]);
}

void join(int i, int j) {
	int p1 = get_parent(i);
	int p2 = get_parent(j);
	if (p1 == p2) {
		return;
	}
	if (h[p1] > h[p2]) {
		p[p2] = p1;
	} else if (h[p1] < h[p2]) {
		p[p1] = p2;
	} else {
		h[p1]++;
		p[p2] = p1;
	}
}

int my_less(const point &a, const point &b) {
	return a.h > b.h || (a.h == b.h && a.i < b.i) || (a.h == b.h && a.i == b.i && a.j < b.j);
}

void dfs(int ci, int cj) {
	u[ci][cj] = 1;
	int nx_min = -1;
	for (int k = 0; k < 4; k++) {
		int nxi = ci + di[k], nxj = cj + dj[k];
		if (nxi >= 0 && nxj >= 0 && nxi < N && nxj < M) {
			if (nx_min == -1 || a[nxi][nxj] < nx_min) {
				nx_min = a[nxi][nxj];
			}
		}
	}
	if (nx_min < a[ci][cj]) {
		for (int k = 0; k < 4; k++) {
			int nxi = ci + di[k], nxj = cj + dj[k];
			if (nxi >= 0 && nxj >= 0 && nxi < N && nxj < M) {
				if (a[nxi][nxj] == nx_min) {
					join(color[ci][cj], color[nxi][nxj]);
					if (!u[nxi][nxj]) {
						dfs(nxi, nxj);
					}
					break;
				}
			}
		}
	}
}

void solve() {
	point all[10002];
	int k = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			all[k].h = a[i][j];
			all[k].i = i;
			all[k].j = j;
			p[k] = k;
			h[k] = 0;
			color[i][j] = k;
			k++;
		}
	}
	sort(all, all + k, my_less);
	for (int i = 0; i < k; i++) {
		if (!u[all[i].i][all[i].j]) {
			dfs(all[i].i, all[i].j);
		}
	}
	// finally label them
	int basins = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int p = get_parent(color[i][j]);
			if (label[p] == -1) {
				label[p] = basins++;
			}
			ans[i][j] = (char)('a' + label[p]);
		}
	}
}

int main()
{
	inp >> T;
	for (int nt = 0; nt < T; nt++) {
		initialize();

		inp >> N >> M;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				inp >> a[i][j];
			}
		}

		solve();

		out << "Case #" << nt + 1 << ":\n";
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (j) out << " ";
				out << ans[i][j];
			}
			out << endl;
		}
	}
	inp.close();
	out.close();
	return 0;
}
