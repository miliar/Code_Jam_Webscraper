#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 101;

int inc[3][2] = { {0, 1}, {1, 0}, {1, 1} };

int cas, n, K;
char a[MAXN][MAXN];

void rotate() {
	char tmp[MAXN][MAXN];

	memset(tmp, '\0', sizeof(tmp));
	for (int i = 0; i < n; i ++)
		for (int j = 0; j < n; j ++)
			tmp[i][j] = a[n-1-j][i];
	memcpy(a, tmp, sizeof(tmp));
}

bool check(int d, int j) {
	if (a[d][j] != '.')
		return false;
	for (int i = d-1; i >= 0; i --)
		if (a[i][j] != '.')
			return true;
	return false;
}

void change() {
	for (int j = 0; j < n; j ++) {
		for (int d = n-1; d >= 0; d --) {
			while (a[d][j] == '.' && check(d, j)) {
				for (int i = d; i > 0; i --)
					a[i][j] = a[i-1][j];
				a[0][j] = '.';
			}
		}
	}
// 	for (int i = 0; i < n; i ++)
// 		printf("%s\n", a[i]);
// 	puts("");
}

bool valid(int x, int y) {
	return x >= 0 && x < n && y >= 0 && y < n;
}

bool check(char tar) {
	for (int i = 0; i < n; i ++) {
		for (int j = 0; j < n; j ++) {
			if (a[i][j] == tar) {
				for (int d = 0; d < 3; d ++) {
					int s = 1;
					int x = i;
					int y = j;
						
					if (s == K)
						return true;
					while(true) {
						x += inc[d][0];
						y += inc[d][1];
						if (! valid(x, y) || a[x][y] != tar)
							break;
						else
							s ++;
						if (s == K)
							return true;
					}
				}
			}
		}
	}
	return false;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &cas);
	for (int c = 1; c <= cas; c ++) {
		scanf("%d%d", &n, &K);
		for (int i = 0; i < n; i ++)
			scanf("%s", a[i]);

		rotate();
		change();
		bool R = check('R');
		bool B = check('B');

// 		printf("[%d %d] \n", n, K);
		printf("Case #%d: ", c);
		if (R && B)
			puts("Both");
		else if (R && !B)
			puts("Red");
		else if (!R && B)
			puts("Blue");
		else
			puts("Neither");
	}

	return 0;
}