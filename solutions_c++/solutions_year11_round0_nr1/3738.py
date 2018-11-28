#include <cstdio>
#include <vector>
#include <cstring>
#include <queue>

using namespace std;

int n;
vector<pair<int, int> > seq;
char chk[101][101][101];

struct node {
	int pos1, pos2;
	int step;
	int w;
};

queue<node> q;

void enqueue(int pos1, int pos2, int step, int w) {
	if (pos1 < 1 || pos1 > 100 || pos2 < 1 || pos2 > 100) return;
	node t;
	t.pos1 = pos1;
	t.pos2 = pos2;
	t.step = step;
	t.w = w + 1;
	if (chk[t.step][t.pos1][t.pos2]) return;
	chk[t.step][t.pos1][t.pos2] = 1;
	q.push(t);
}

int solve() {
	node t;
	t.pos1 = t.pos2 = 1;
	t.step = t.w = 0;
	q.push(t);
	chk[t.step][t.pos1][t.pos2] = 1;
	while (!q.empty()) {
		t = q.front();
		q.pop();
		if (t.step == n) return t.w;
		for (int i = -1; i <= 2; ++i) {
			for (int j = -1; j <= 2; ++j) {
				if (i == 0 && j == 0) continue;
				if (i == 2 && j == 2) continue;
				if (i == 2) {
					if (seq[t.step].first == 0 && seq[t.step].second == t.pos1) {
						enqueue(t.pos1, t.pos2 + j, t.step + 1, t.w);
					}
				} else if (j == 2) {
					if (seq[t.step].first == 1 && seq[t.step].second == t.pos2) {
						enqueue(t.pos1 + i, t.pos2, t.step + 1, t.w);
					}
				} else {
					enqueue(t.pos1 + i, t.pos2 + j, t.step, t.w);
				}
			}
		}
	}
	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int r;
	int no = 0;
	scanf("%d", &r);
	while (r--) {
		scanf("%d", &n);
		seq.clear();
		memset(chk, 0, sizeof(chk));
		while (!q.empty()) q.pop();
		for (int i = 0; i < n; ++i) {
			char buf[10];
			int pos;
			scanf("%s %d", buf, &pos);
			seq.push_back(make_pair(buf[0] == 'O' ? 0 : 1, pos));
		}
		printf("Case #%d: %d\n", ++no, solve());
	}
	return 0;
}