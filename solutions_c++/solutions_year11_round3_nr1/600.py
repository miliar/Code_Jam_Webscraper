#include <vector>
#include <cstdio>
#include <cmath>
using namespace std;
const int maxn = 51;
char res[maxn][maxn];
int R, C;

bool change(int a, int b, char c) {
	if (res[a][b] != '#')
		return false;
	res[a][b] = c;
	return true;
}

bool solve() {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++)  {
			if (res[i][j] == '#') {
				if (i + 1 >= R)
					return false;
				if (j + 1 >= C)
					return false;
				if (!change(i, j, '/')) return false;
				if (!change(i, j + 1, '\\')) return false;
				if (!change(i + 1, j, '\\')) return false;
				if (!change(i + 1, j + 1, '/')) return false;
			}
		}
	}
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d %d", &R, &C);
		for (int i = 0; i < R; i++)
			scanf("%s", res[i]);
		printf("Case #%d:\n", t);
		if (solve()) {
			for (int i = 0; i < R; i++)
				printf("%s\n", res[i]);
		}else {
			printf("Impossible\n");
		}
	}
	return 0;
}
