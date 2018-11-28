#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

// of the vines
int dist[10011];
int len[10011];
int sz;
int target;
bool poss;

void dfs(int i, int held) {
	// check
	if (dist[i] + min(held, len[i]) >= target) {
		poss = true;
		return;
	}
	for (int j = i+1; j < sz; j++) {
		// check
		int allow = min(held, min(len[i], dist[j] - dist[i]));
		if (allow + dist[i] < dist[j]) {
			break;
		}
		//cout << "can go from " << i << " to " << j << "\n";
		dfs(j, allow);
		if (poss) return;
	}
}

int main() {
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int N; cin >> N;
		memset(dist,0,sizeof(dist));
		memset(len,0,sizeof(len));
		poss = false;
		sz = N;
		for (int i = 0; i < N; i++) {
			int di, leni;
			cin >> di >> leni;
			dist[i] = di;
			len[i] = leni;
		}
		int dest; cin >> dest;
		target = dest;
		dist[N] = target;
		// find possible starting
		dfs(0, dist[0]);
		if (poss) {
			cout << "Case #" << t << ": YES\n";
		} else {
			cout << "Case #" << t << ": NO\n";
		}
	}

	return 0;
}