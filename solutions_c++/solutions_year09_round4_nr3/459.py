#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

const int MAX=200;
bool adj[MAX][MAX];
vector<int> G[MAX];

int prices[MAX][MAX];

void add_edge(int i, int j) {
	adj[i][j] = adj[j][i] = 1;
	G[i].push_back(j);
	G[j].push_back(i);
}

const int INF=1<<30;
int best;
int n;

int cur[MAX];

void solve(int at, int colors) {
	if (at==n) {
		best = min(best, colors);
		return;
	}
	if (colors>=best) return;

	vector<bool> can_use(n,0);
	for (int i=0;i<colors;++i) can_use[i] = 1;

	for (int i=0;i<G[at].size();++i) {
		int v = G[at][i];
		if (cur[v] != -1) {
			can_use[cur[v]] = 0;
		}
	}

	for (int i=0;i<colors;++i) if (can_use[i]) {
		cur[at] = i;
		solve(at+1, colors);
		cur[at] = -1;
	}
	cur[at] = colors;
	solve(at+1, colors+1);
	cur[at] = -1;
}

int main() {
	int NCASES;
	cin >> NCASES;
	for (int z=1;z<=NCASES;++z) {
		int k;
		cin >> n >> k;
		assert(k!=1);

		for (int i=0;i<n;++i) {
			G[i].clear();
			for (int j=0;j<n;++j) {
				adj[i][j] = 0;
			}
		}

		for (int i=0;i<n;++i) {
			for (int j=0;j<k;++j) {
				cin >> prices[i][j];
			}
		}

		for (int i=0;i<n;++i) {
			for (int j=i+1;j<n;++j) {

				bool found = 0;
				for (int h=0;h<k;++h) {
					if (prices[i][h] == prices[j][h]) {
						add_edge(i,j);
						found = 1;
						break;
					}
				}

				if (found) continue;

				for (int h=0;h+1<k;++h) {
					bool stat1 = (prices[i][h]   < prices[j][h]);
					bool stat2 = (prices[i][h+1] < prices[j][h+1]);
					if (stat1 != stat2) {
						add_edge(i,j);
						break;
					}
				}
			}
		}

		for (int i=0;i<n;++i) cur[i] = -1;

		best = INF;
		solve(0, 0);
		assert(best!=INF);
		printf("Case #%d: %d\n", z, best);
	}
}
