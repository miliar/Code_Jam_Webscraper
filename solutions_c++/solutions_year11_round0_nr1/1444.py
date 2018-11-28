#include <cstdio>
#include <cstdlib>
#include <queue>

using namespace std;

int main(int argc, char** argv) {
	int t;
	scanf("%d", &t);
	for (int nCase = 1; nCase <= t; ++nCase) {
		int n;
		scanf("%d", &n);
		char color[9];
		int pos;
		queue<pair<char, int> >q;
		queue<int>qo, qb;
		for (int i = 0; i < n; ++i) {
			scanf("%s%d", color, &pos);
			if (color[0] == 'O') {
				qo.push(pos);
			} else {
				qb.push(pos);
			}
			q.push(make_pair(color[0], pos));
		}
		int po = 1, pb = 1, to, tb, time = 0;
		while (!q.empty()) {
			char c = q.front().first;
			int p = q.front().second;
			if (!qo.empty()) {
				to = qo.front();
			} else {
				to = po;
			}
			if (!qb.empty()) {
				tb = qb.front();
			} else {
				tb = pb;
			}
			if (c == 'O') {
				int step = abs(p - po) + 1;
				if (abs(tb - pb) <= step) {
					pb = tb;
				} else {
					if (tb > pb) {
						pb += step;
					} else if (tb < pb) {
						pb -= step;
					}
				}
				po = p;
				time += step;
				qo.pop();
			} else {
				int step = abs(p - pb) + 1;
				if (abs(to - po) <= step) {
					po = to;
				} else {
					if (to > po) {
						po += step;
					} else if (to < po) {
						po -= step;
					}
				}
				pb = p;
				time += step;
				qb.pop();
			}
			q.pop();
		}
		printf("Case #%d: %d\n", nCase, time);
	}
	return 0;
}
