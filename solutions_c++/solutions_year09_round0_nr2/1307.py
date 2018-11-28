#include <cmath>
#include <queue>
#include <memory>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define s(c) ((int)((c).size()))
#define mset(a, v) memset(a, v, sizeof(a))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)

int h, w;
int alt[102][102];
int dr[] = {-1, 0, 0, 1};
int dc[] = {0, -1, 1, 0};
int moo[] = {3, 2, 1, 0};
int dir[102][102];
char lab[102][102];

void bfs(int r, int c, char cur) {
	queue<int> qr, qc;
	qr.push(r); qc.push(c);
	lab[r][c] = cur;
	while (!qr.empty()) {
		int rr = qr.front(); qr.pop();
		int cc = qc.front(); qc.pop();
		if (dir[rr][cc] != -1) {
			int ro = rr + dr[dir[rr][cc]];
			int co = cc + dc[dir[rr][cc]];
			if (lab[ro][co] == 0) {
				lab[ro][co] = cur;
				qr.push(ro); qc.push(co);
			}
		}
		f(i, 0, 3) {
			int ro = rr + dr[i];
			int co = cc + dc[i];
			if (ro > 0 && ro <= h && co > 0 && co <= w && dir[ro][co] == moo[i] && lab[ro][co] == 0) {
				lab[ro][co] = cur;
				qr.push(ro); qc.push(co);
			}
		}
	}
}

void solve(int t) {
	scanf("%d%d", &h, &w);
	f(r, 1, h) f(c, 1, w) scanf("%d", &alt[r][c]);
	f(r, 1, h) f(c, 1, w) {
		int d = -1, mn = alt[r][c];
		f(k, 0, 3) {
			int rr = r + dr[k];
			int cc = c + dc[k];
			if (rr > 0 && rr <= h && cc > 0 && cc <= w && alt[rr][cc] < mn) {
				mn = alt[rr][cc];
				d = k;
			}
		}
		dir[r][c] = d;
	}
	mset(lab, 0);
	char cur = 'a';
	f(r, 1, h) f(c, 1, w) if (lab[r][c] == 0) {
		bfs(r, c, cur);
		++cur;
	}
	printf("Case #%d:\n", t);
	f(r, 1, h) {
		//puts(&lab[r][1]);
		f(c, 1, w - 1) printf("%c ", lab[r][c]);
		printf("%c", lab[r][w]);
		if (r < h)
			printf("\n");
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	f(i, 1, t) {
		solve(i);
		if (i < t)
			printf("\n");
	}
	return 0;
}
