#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAX_N = 500 + 5;

int T;
int R, C, D;
char s[MAX_N][MAX_N];
long long sumsX[MAX_N][MAX_N];
long long sumsY[MAX_N][MAX_N];
long long mass[MAX_N][MAX_N];
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; t ++) {
		scanf("%d %d %d\n", &R, &C, &D);
		for (int i = 0; i < R; i ++) {
			gets(s[i]);
		}
		for (int i = 0; i < MAX_N; i ++) {
			sumsX[0][i] = sumsX[i][0] = 0;
			sumsY[0][i] = sumsY[i][0] = 0;
		}
		for (int i = 0; i < R; i ++) {
			for (int j = 0; j < C; j ++) {
				sumsX[i + 1][j + 1] = sumsX[i][j + 1] + sumsX[i + 1][j] - sumsX[i][j];
				sumsX[i + 1][j + 1] += (s[i][j] - '0' + D) * i;

				sumsY[i + 1][j + 1] = sumsY[i][j + 1] + sumsY[i + 1][j] - sumsY[i][j];
				sumsY[i + 1][j + 1] += (s[i][j] - '0' + D) * j;
				
				mass[i + 1][j + 1] = mass[i][j + 1] + mass[i + 1][j] - mass[i][j];
				mass[i + 1][j + 1] += s[i][j] - '0' + D;
			}
		}

		int res = -1;
		for (int i = 0; i < R; i ++) {
			for (int j = 0; j < C; j ++) {
				for (int size = 3; i + size <= R && j + size <= C; size ++) {
					int endX = i + size;
					int endY = j + size;
					long long curMass = mass[endX][endY] - mass[i][endY] - mass[endX][j] + mass[i][j];
					curMass -= s[i][j] - '0' + D;
					curMass -= s[i][endY - 1] - '0' + D;
					curMass -= s[endX - 1][j] - '0' + D;
					curMass -= s[endX - 1][endY - 1] - '0' + D;

					
					long long curMassX = sumsX[endX][endY] - sumsX[i][endY] - sumsX[endX][j] + sumsX[i][j];
					curMassX -= (s[i][j] - '0' + D) * i;
					curMassX -= (s[i][endY - 1] - '0' + D) * i;
					curMassX -= (s[endX - 1][j] - '0' + D) * (endX - 1);
					curMassX -= (s[endX - 1][endY - 1] - '0' + D) * (endX - 1);

					long long curMassY = sumsY[endX][endY] - sumsY[i][endY] - sumsY[endX][j] + sumsY[i][j];
					curMassY -= (s[i][j] - '0' + D) * j;
					curMassY -= (s[i][endY - 1] - '0' + D) * (endY - 1);
					curMassY -= (s[endX - 1][j] - '0' + D) * j;
					curMassY -= (s[endX - 1][endY - 1] - '0' + D) * (endY - 1);

					double midX = i + (size - 1) * .5;
					double midY = j + (size - 1) * .5;
					if (fabs(midX * curMass - curMassX) < 1e-5 && fabs(midY * curMass - curMassY) < 1e-5) {
						res = max(res, size);
					}
				}
			}
		}
		printf("Case #%d: ", t);
		if (res == -1) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", res);
		}
	}
}
