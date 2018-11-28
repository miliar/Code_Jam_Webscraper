#include <cstdio>
#include <cstring>

const int MAXN = 100 + 1;

char combine[255][255];
bool oppose[255][255];

char stack[MAXN];
int top;

int main() {
	int m;
	scanf("%d", &m);
	for (int q = 1; q <= m; q++) {
		memset(combine, 0, sizeof(combine));
		memset(oppose, false, sizeof(oppose));
		int c, d, n;
		scanf("%d ", &c);
		for (int i = 1; i <= c; i++) {
			char x, y, z;
			scanf("%c%c%c ", &x, &y, &z);
			combine[x][y] = combine[y][x] = z;
		}
		scanf("%d ", &d);
		for (int i = 1; i <= d; i++) {
			char x, y;
			scanf("%c%c ", &x, &y);
			oppose[x][y] = oppose[y][x] = true;
		}
		scanf("%d ", &n);
		top = 0;
		for (int i = 0; i < n; i++) {
			top++;
			scanf("%c", &stack[top]);
			while (top > 1 && combine[ stack[top] ][ stack[top - 1] ] != 0) {
				char tmp = combine[ stack[top] ][ stack[top - 1] ];
				top--;
				stack[top] = tmp;
			}
			for (int j = top - 1; j > 0; j--)
				if (oppose[ stack[j] ][ stack[top] ]) {
					top = 0;
					break;
				}
		}
		printf("Case #%d: [", q);
		for (int i = 1; i < top; i++) printf("%c, ", stack[i]);
		if (top > 0) printf("%c]\n", stack[top]);
		else printf("]\n");
	}
	return 0;
}

