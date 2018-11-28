#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int dir[8][2] = {{-1, 0}, {1, 0},
	{0, -1}, {0, 1},
	{1, -1}, {-1, 1},
	{1, 1}, {-1, -1}};

vector< pair<int, int> > eq[10000];
int eq2[10000];
int N;

bool check(int i, int val) {
	for (int j = 0; j < eq[i].size(); j++)
		if (eq[i][j].first == val)
			return true;
	return false;
}

void combine(int x, int y) {
	vector< pair<int, int> > tmp;
	for (int i = 0; i < eq[x].size(); i++) tmp.push_back(eq[x][i]);
	for (int i = 0; i < eq[y].size(); i++) tmp.push_back(eq[y][i]);
	sort(tmp.begin(), tmp.end());

	eq2[y] = eq2[y] ^ eq2[x];

	eq[y].clear();
	for (int i = 0; i < tmp.size(); i++)
		if (i + 1 < tmp.size() && tmp[i].first == tmp[i + 1].first) {
			if (tmp[i].second != tmp[i + 1].second) eq2[y] = eq2[y] ^ 1;
			i++;
		} else {
			eq[y].push_back(tmp[i]);
		}
}

bool final[10000];

bool solve() {
	memset(final, 0, sizeof final);

	int fixed = 0;
	for (int i = 0; i < N; i++) {
		int j; for (j = 0; j < N; j++) if (!final[j] && check(j, i)) break;

		if (j < N) fixed++;
		final[j] = true;

		for (int k = j + 1; k < N; k++)
			if (!final[k] && check(k, i)) {
				combine(j, k);
				if (eq[k].size() == 0 && eq2[k] == 1) return false;
			}
	}

	int ans = 1;
	for (int i = 0; i < N - fixed; i++)
		ans = (ans * 2) % 1000003;

	printf("%d\n", ans);

	return true;
}

int pos(int R, int C, int r, int c) {
	return r * C + c;
}

void init() {
	int R, C; scanf("%d%d", &R, &C);

	N = R * C;
	for (int i = 0; i < N; i++) {
		eq[i].clear();
		eq2[i] = 1;
	}

	for (int i = 0; i < R; i++) {
		static char buf[500]; scanf("%s", buf);
		for (int j = 0; j < C; j++) {
			char ch = buf[j];

			int d;
			if (ch == '|') d = 0;
			else if (ch == '-') d = 2;
			else if (ch == '/') d = 4;
			else d = 6;

			for (int x = 0; x < 2; x++) {
				int r1 = (i + dir[d + x][0] + R) % R;
				int c1 = (j + dir[d + x][1] + C) % C;

				eq[pos(R, C, r1, c1)].push_back(make_pair(pos(R, C, i, j), x));
			}
		}
	}
}

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		init();
		printf("Case #%d: ", i);
		if (!solve()) printf("0\n");
	}

	return 0;
}
