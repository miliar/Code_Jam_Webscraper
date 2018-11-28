#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

char str[105];
char gewichten[105][105];
int echtegewicht[10][10];

int T,R,C,D;

bool passend(int i, int j, int x, int y) {
	int Xmid = i + x;
	int Ymid = j + y;
	int Xmass = 0;
	int Ymass = 0;
	for (int a = i; a <= x; a++) {
		for (int b = j; b <= y; b++) {
			if ((a == i || a == x) && (b == j || b == y))
				continue;
			Xmass += (2 * a - Xmid) * gewichten[a][b];
			Ymass += (2 * b - Ymid) * gewichten[a][b];
		}
	}
	return (Xmass == 0 && Ymass == 0);
}

void solve(int nummer) {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			echtegewicht[i][j] = ((int) (gewichten[i][j] - '0')) + D;
		}
	}
	int min = 2;
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			for (int x = i + min; x < R; x++) {
				int y = j + (x - i);
				if (y >= C)
					break;
				if (passend(i, j, x, y)) {
					min = x - i + 1;
				}
			}
		}
	}
	printf("Case #%d: ", nummer);
	if (min == 2)
		printf("IMPOSSIBLE\n");
	else
		printf("%d\n", min);
}

int main() {
	fgets(str, 100, stdin);
	sscanf(str, "%d", &T);
	for (int i = 0; i < T; i++) {
		fgets(str, 100, stdin);
		sscanf(str, "%d %d %d", &R, &C, &D);
		for (int j = 0; j < R; j++) {
			fgets(str, 100, stdin);
			strcpy(gewichten[j], str);
		}
		solve(i + 1);
	}
	return 0;
}

