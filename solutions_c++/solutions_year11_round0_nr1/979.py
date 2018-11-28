#pragma comment(linker, "/STACK:160777216")
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <numeric>
#include <ctime>
#include <deque>
#include <climits>
#include <list>
using namespace std;

int nextInt() {
	int x;
	scanf("%d", &x);
	return x;
}

double nextDouble() {
	double x;
	scanf("%lf", &x);
	return x;
}

long long nextLong() {
	long long x;
	scanf("%lld", &x);
	return x;
}

char buf[1010111];
string nextString() {
	scanf("%s", buf);
	return buf;
}

string nextLine() {
	gets(buf);
	return buf;
}

const int N = 100;
const int inf = INT_MAX / 2;

void check(queue<int> &q, vector<vector<vector<int> > > &dist, int visited, int atO, int atB, int value) {
	if (atO < 1 || atO > N
			|| atB < 1 || atB > N) {
		return;
	}
	if (dist[visited][atO][atB] > value) {
		dist[visited][atO][atB] = value;
		q.push(visited);
		q.push(atO);
		q.push(atB);
	}
}

int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("a_large.out", "wt", stdout);
	int T = nextInt();
	for (int cas = 1; cas <= T; ++cas) {
		int n = nextInt();
		vector<pair<int, int> > seq(n);
		for (int i = 0; i < n; ++i) {
			seq[i].first = nextString()[0];
			seq[i].second = nextInt();
		}
		vector<vector<vector<int> > > dist(seq.size() + 1, vector<vector<int> >(N + 1, vector<int>(N + 1, inf)));
		queue<int> q;
		check(q, dist, 0, 1, 1, 0);
		while (!q.empty()) {
			int visited = q.front(); q.pop();
			int atO = q.front(); q.pop();
			int atB = q.front(); q.pop();
			int curDist = dist[visited][atO][atB];
			for (int d1 = -1; d1 <= 1; ++d1) {
				for (int d2 = -1; d2 <= 1; ++d2) {
					check(q, dist, visited, atO + d1, atB + d2, curDist + 1);
				}
			}
			if (visited < seq.size()) {
				bool isO = seq[visited].first == 'O';
				int nv = ((isO ? atO : atB) == seq[visited].second) + visited;
				for (int d = -1; d <= 1; ++d) {
					check(q, dist, nv, atO + d * (!isO), atB + d * isO, curDist + 1);
				}
			}
		}
		int res = inf;
		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				res = min(res, dist[seq.size()][i][j]);
			}
		}
		printf("Case #%d: %d\n", cas, res);
		cerr << cas << " " << T << endl;
	}
	return 0;
}