#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX = 220;

struct Node {
	int color, pos;
} node[MAX];
int pt[2], pos[2][MAX], top[2];
int T, n;
char op[12];

int main() {
	int cas = 1;
	int x, y, ret = 1;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	while (T--) {
		ret = 0;
		x = y = 1;
		pt[0] = pt[1] = 0;
		top[0] = top[1] = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s%d", op, &node[i].pos);
			if (op[0] == 'O')
				node[i].color = 0;
			else
				node[i].color = 1;
			pos[node[i].color][top[node[i].color]++] = i;
		}
		for (int i = 0; i < n; i++) {
			if (pt[0] == top[0]) {
				ret += abs(node[pos[1][pt[1]]].pos - y) + 1;
				y = node[pos[1][pt[1]]].pos;
				pt[1]++;
			} else if (pt[1] == top[1]) {
				ret += abs(node[pos[0][pt[0]]].pos - x) + 1;
				x = node[pos[0][pt[0]]].pos;
				pt[0]++;
			} else {
				if (pos[0][pt[0]] == i) {
					int mov = abs(node[pos[0][pt[0]]].pos - x) + 1;
					ret += mov;
					x = node[pos[0][pt[0]]].pos;
					pt[0]++;
					if (mov >= abs(node[pos[1][pt[1]]].pos - y)) {
						y = node[pos[1][pt[1]]].pos;
					} else {
						if (node[pos[1][pt[1]]].pos > y) {
							y += mov;
						} else {
							y -= mov;
						}
					}
				} else {
					int mov = abs(node[pos[1][pt[1]]].pos - y) + 1;
					ret += mov;
					y = node[pos[1][pt[1]]].pos;
					pt[1]++;
					if (mov >= abs(node[pos[0][pt[0]]].pos - x)) {
						x = node[pos[0][pt[0]]].pos;
					} else {
						if (node[pos[0][pt[0]]].pos > x) {
							x += mov;
						} else {
							x -= mov;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", cas++, ret);
	}

	return 0;
}
