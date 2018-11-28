#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <map>

using namespace std;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

long long solveIt(int H, int W, vector<int> &ry, vector<int> &rx) {
	vector<vector<int> > ct(H, vector<int>(W, 0)), vis = ct;

	for (int i = 0; i < ry.size(); i++) ct[ry[i]-1][rx[i]-1] = -1;

	ct[0][0] = 1;
	queue<int> q;
	q.push(0);
	while (!q.empty()) {
		int y = q.front()/128, x = q.front()%128;
		q.pop();
		if (vis[y][x]) continue;
		vis[y][x] = 1;
		if (y+2 < H && x+1 < W && ct[y+2][x+1] >= 0) {
			ct[y+2][x+1] += ct[y][x];
			ct[y+2][x+1] %= 10007;
			q.push((y+2)*128+(x+1));
		}
		if (y+1 < H && x+2 < W && ct[y+1][x+2] >= 0) {
			ct[y+1][x+2] += ct[y][x];
			ct[y+1][x+2] %= 10007;
			q.push((y+1)*128+(x+2));
		}
	}

	return ct[H-1][W-1];
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int H, W, R;
		scanf("%d %d %d ", &H, &W, &R);
		vector<int> rx(R), ry(R);
		for (int i = 0; i < R; i++) scanf("%d %d ", &ry[i], &rx[i]);

		long long res = solveIt(H, W, ry, rx);

		printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

