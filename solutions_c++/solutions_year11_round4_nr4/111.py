#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <complex>
#include <set>
#include <map>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ll> vl;

vi edges[512];
int dist[512];
int P, W;
int best;

void bfs() {
	memset(dist, -1, sizeof(dist));
	queue<int> q;
	q.push(1);
	dist[1] = 0;
	while (q.size() > 0) {
		int i = q.front();
		q.pop();
		for (int e = 0; e < edges[i].size(); ++e) {
			int j = edges[i][e];
			if (dist[j] >= 0) continue;
			dist[j] = dist[i] + 1;
			q.push(j);
		}
	}
	// cout << " bfs=" << dist[0] << endl;
}

int bitcount(ll m) {
	int ret = 0;
	while (m > 0) {
		if (m % 2) {
			++ret;
		}
		m /= 2;
	}
	return ret;
}

void dfs(int i, ll seen) {
	if (i == 1) {
		best = max(best, bitcount(seen));
		return;
	}
	for (int e = 0; e < edges[i].size(); ++e) {
		int j = edges[i][e];
		if (j == 0) continue;
		seen |= (1ll << j);
	}
	// cout << " i=" << i << " seen=" << bitcount(seen) << endl;
	for (int e = 0; e < edges[i].size(); ++e) {
		int j = edges[i][e];
		if (dist[j] == dist[i] - 1) {
			dfs(j, seen);
		}
	}
}

int main() {
	int TT;
	cin >> TT;
	for (int tt = 1; tt <= TT; ++tt) {
		cin >> P >> W;
		for (int i = 0; i < P; ++i) {
			edges[i].clear();
		}
		for (int i = 0; i < W; ++i) {
			char c;
			int x, y;
			cin >> x >> c >> y;
			edges[x].push_back(y);
			edges[y].push_back(x);
		}
		best = 0;
		bfs();
		dfs(0, 0);
		best -= dist[0] - 1;
		cout << "Case #" << tt << ":";
		cout << " ";
		cout << dist[0] - 1;
		cout << " ";
		cout << best;
		cout << endl;
	}
	return 0;
}

