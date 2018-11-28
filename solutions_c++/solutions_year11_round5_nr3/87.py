#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

//   -|\/
const int dx[4][2] = {{ 0, 0}, {-1, 1}, {-1, 1}, {-1,  1}};
const int dy[4][2] = {{-1, 1}, { 0, 0}, {-1, 1}, { 1, -1}};

int T, n, m, N;
char s[100][101];
bool v[100][100];

inline bool gao(int mask, int x, int y) {
	int cx = x, cy = y;
	while (!v[cx][cy]) {
		v[cx][cy] = true;
		int b = !!(mask & 1 << (cx * m + cy));
		int ch = s[cx][cy];
		cx = (cx + dx[ch][b] + n) % n;
		cy = (cy + dy[ch][b] + m) % m;
	}
	return x == cx && y == cy;
}

int main() {
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			scanf("%s", s[i]);
			for (int j = 0; j < m; ++j) {
				s[i][j] =
						s[i][j] == '-' ? 0 :
						s[i][j] == '|' ? 1 :
						s[i][j] == '\\' ? 2 : 3;
			}
		}
		N = n * m;
		int res = 0;
		for (int i = 0; i < (1 << N); ++i) {
			bool succ = true;
			memset(v, 0, sizeof(v));
			for (int j = 0; j < n && succ; ++j) {
				for (int k = 0; k < m && succ; ++k) {
					if (!v[j][k]) {
						succ = gao(i, j, k);
					}
				}
			}
			succ && ++res;
		}
		printf("Case #%d: %d\n", caseNum, res);
	}
	return 0;
}
