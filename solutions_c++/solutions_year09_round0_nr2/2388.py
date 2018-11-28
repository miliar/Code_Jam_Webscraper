#include <iostream>
using namespace std;

char ans[128][128];
int H;
int W;

pair<int, int> next[128][128];

void printResult() {
	for (int y = 0; y < H; y++) {
		for (int x = 0; x < W; x++) {
			cout << ans[y][x] << (x == W - 1 ? "" : " ");
		}
		cout << '\n';
	}
}

pair<int, int> nextPair() {
	for (int y = 0; y < H; y++) {
		for (int x = 0; x < W; x++) {
			if (ans[y][x] == 'W') {
				//				cout << "nextPair: y = "<<y << ',' << "x = " << x <<"\n";
				return make_pair(y, x);
			}
		}
	}
	return make_pair(-1, -1);
}

void fill(pair<int, int> root, char c) {
	pair<int, int> now = make_pair(root.first, root.second);
	while (true) {
		ans[now.first][now.second] = c;
		pair<int, int> dn = next[now.first][now.second];
		if ((dn.first == now.first) && (dn.second == now.second)) {
			break;//loop
		}
		now = make_pair(dn.first, dn.second);

	}
}

int solve() {
	memset(ans, 87, sizeof ans);
	pair<int, int> root;
	char c = 'a' - 1;
	while (true) {
		c++;
		pair<int, int> now = nextPair();
		//		cout << "c = " << c << '\n';
		if (now.first == -1) {
			printResult();
			return 0;
		}
		root = make_pair(now.first, now.second);
		while (true) {//not end
			ans[now.first][now.second] = c;
			pair<int, int> dn = next[now.first][now.second];
			//			cout << "got next " << dn.first << " " << dn.second << "\n";
			if (dn.first == now.first && dn.second == now.second) {
				break;//loop
			}

			now = make_pair(dn.first, dn.second);

			char rrr = ans[dn.first][dn.second];
			if (rrr != 'W') {
				//				cout << "doing root fill with " << rrr << "\n";
				fill(root, rrr);
				c--;
				break;
			}
		}

	}

	return -1;

}

int main() {
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int u = 0; u < 30; u++) {
		cout << '\n';
	}
	for (int t = 1; t <= T; t++) {
		cin >> H >> W;

		int map[H][W];
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				cin >> map[y][x];
			}
		}

		int dy[] = { -1, 0, 0, 1 };
		int dx[] = { 0, -1, 1, 0 };
		//		char ds[] = {'^', '<', '>', 'v'};
		for (int y = 0; y < H; y++) {
			for (int x = 0; x < W; x++) {
				int min = map[y][x];
				int bx = -1;
				int by = -1;
				for (int i = 0; i < 4; i++) {
					int nx = x + dx[i];
					int ny = y + dy[i];
					if (nx < 0 || nx >= W)
						continue;
					if (ny < 0 || ny >= H)
						continue;
					int next = map[ny][nx];
					if (next < min) {
						//						cout << "tysh " << y << " " << x << ":" << ds[i] << "=" << next << '\n';
						min = next;
						by = ny;
						bx = nx;
					}
				}
				if ((by != -1) && (bx != -1)) {
					//					cout << y << " " << x << "pair = " << by << " " << bx << "\n";
					next[y][x] = make_pair(by, bx);
				} else {
					//					cout << "found basin " << y << " " << x <<"\n";
					next[y][x] = make_pair(y, x);
				}
			}
		}
		//		cout << "DOTO:\n";
		//		for (int y = 0; y < H; y++) {
		//			for (int x = 0; x < W; x++) {
		//				cout << next[y][x].first << " " << next[y][x].second << '\t';
		//			}
		//			cout << '\n';
		//		}

		cout << "Case #" << t << ":\n";
		solve();

	}

	return 0;
}
