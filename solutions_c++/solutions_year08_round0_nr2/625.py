#include <stdio.h>
#include <queue>
using namespace std;
priority_queue<int, vector<int>, greater<int>> req[2], sup[2];

int getTime() {
	int h, m;
	scanf("%d%*c%d", &h, &m);
	return h * 60 + m;
}

int main() {
	int rep;
	scanf("%d", &rep);
	for (int ri = 0; ri < rep; ri++) {
		int rt;
		int na, nb;
		scanf("%d%d%d", &rt, &na, &nb);
		for (int i = 0; i < na; i++) {
			req[0].push(getTime());
			sup[1].push(getTime() + rt);
		}
		for (int i = 0; i < nb; i++) {
			req[1].push(getTime());
			sup[0].push(getTime() + rt);
		}
		int ea = 0, eb = 0;
		int ra = 0, rb = 0;
		for (int i = 0; i < 24 * 60; i++) {
			// A => B
			while (!sup[0].empty() && sup[0].top() == i) {
				ea ++;
				sup[0].pop();
			}
			while (!req[0].empty() && req[0].top() == i) {
				ea --;
				req[0].pop();
			}
			if (ea < 0) {
				ra -= ea;
				ea = 0;
			}

			// B => A
			while (!sup[1].empty() && sup[1].top() == i) eb++, sup[1].pop();
			while (!req[1].empty() && req[1].top() == i) eb--, req[1].pop();
			if (eb < 0) {
				rb -= eb;
				eb = 0;
			}
		}
		printf("Case #%d: %d %d\n", ri + 1, ra, rb);
	}
}