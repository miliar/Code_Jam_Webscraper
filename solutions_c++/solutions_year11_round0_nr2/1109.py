#include <stdio.h>
#include <string.h>

char combine[26][26];
bool clear[26][26];
char str[110];
char stack[110];
int top;

void process() {
	memset(combine, 0, sizeof(combine));
	memset(clear, 0, sizeof(clear));
	int cbNum, clNum, len;
	int x, y;
	scanf("%d", &cbNum);
	for (int i = 0; i < cbNum; ++i) {
		scanf("%s", str);
		x = str[0] - 'A';
		y = str[1] - 'A';
		combine[x][y] = combine[y][x] = str[2];
	}
	scanf("%d", &clNum);
	for (int i = 0; i < clNum; ++i) {
		scanf("%s", str);
		x = str[0] - 'A';
		y = str[1] - 'A';
		clear[x][y] = clear[y][x] = 1;
	}
	scanf("%d%s", &len, str);
	top = 0;
	for (int i = 0; i < len; ++i) {
		if (top == 0) {
			stack[top++] = str[i];
			continue;
		}
		x = stack[top-1] - 'A';
		y = str[i] - 'A';
		if (combine[x][y] != 0) {
			stack[top-1] = combine[x][y];
			continue;
		}
		for (int j = 0; j < top; ++j) {
			x = stack[j] - 'A';
			if (clear[x][y] != 0) {
				top = 0;
			}
		}
		if (top > 0) {
			stack[top++] = str[i];
		}
	}
	printf("[");
	for (int i = 0; i < top; ++i) {
		if (i > 0) printf(", ");
		printf("%c", stack[i]);
	}
	printf("]");
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; ++i) {
		printf("Case #%d: ", i);
		process();
		printf("\n");
	}
	return 0;
}
