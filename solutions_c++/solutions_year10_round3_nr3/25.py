#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
#include <map>
#include <cassert>
using namespace std;

static inline int parseHexDigit(const char ch) {
	if (ch >= '0' && ch <= '9')
		return ch - '0';
	else
		return 10 + (ch - 'A');
}

static inline bool inBoard(int x, int y, int n, int m) {
	return (x >= 0 && y >= 0 && x < n && y < m);
}

int main(void) {
	int testNum;
	scanf("%d", &testNum);
	for (int testCase = 1; testCase <= testNum; testCase++) {
		int n, m;
		scanf("%d%d", &n, &m);
		vector< vector<char> > ma(n, vector<char>(m));
		for (int i = 0; i < n; i++) {
			char str[500];
			scanf("%s", str);
			for (int j = 0; j < m/4; j++) {
				int t = parseHexDigit(str[j]);
				ma[i][j*4 + 0] = t & 8;
				ma[i][j*4 + 1] = t & 4;
				ma[i][j*4 + 2] = t & 2;
				ma[i][j*4 + 3] = t & 1;
			}
		}
		map<int, int, greater<int> > result;
		vector< vector<int> > u(n, vector<int>(m));
		for (int i = 0; i < n; i++)
			u[i][m-1] = 1;
		for (int i = m - 2; i >= 0; i--)
			for (int j = 0; j < n; j++)
				u[j][i] = ((bool)ma[j][i] == (bool)ma[j][i+1]) ? 1 : u[j][i+1] + 1;
		vector< vector<int> > v(n, vector<int>(m));
		for (int j = 0; j < m; j++) {
			multiset<int> s;
			int k = 1;
			s.insert(u[0][j]);
			for (int i = 0; i < n; i++) {
				while (k < n && (k == i || ((bool)ma[k][j] != (bool)ma[k-1][j] && k - i < *s.begin() && k - i < u[k][j]))) {
					s.insert(u[k][j]);
					++k;
				}
				v[i][j] = k - i;
				s.erase(s.find(u[i][j]));
			}
		}
		while (true) {
			int bestSquareSize = 0;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					bestSquareSize = max(bestSquareSize, v[i][j]);
				}
			}
			if (bestSquareSize == 0)
				break;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					if (v[i][j] == bestSquareSize) {
						++result[bestSquareSize];
						for (int i2 = 0; i2 < bestSquareSize; i2++)
							for (int j2 = 0; j2 < bestSquareSize; j2++) {
								assert(v[i + i2][j + j2] != 0);
								v[i + i2][j + j2] = 0;
							}
						for (int k = 0; k < bestSquareSize; k++) {
							for (int l = 1; inBoard(i + k, j - l, n, m) && v[i+k][j-l] > l; l++) {
								for (int q = 0; inBoard(i + k - q, j - l - q, n, m) && v[i + k - q][j - l - q] > l + q; q++)
									v[i+k-q][j-l-q] = l + q;
							}
							for (int l = 1; inBoard(i - l, j + k, n, m) && v[i-l][j+k] > l; l++) {
								for (int q = 0; inBoard(i - l - q, j + k - q, n, m) && v[i - l - q][j + k - q] > l + q; q++)
									v[i-l-q][j+k-q] = l + q;
							}
						}
						for (int l = 1; inBoard(i - l, j - l, n, m) && v[i-l][j-l] > l; l++)
							v[i-l][j-l] = l;
					}
				}
			}
		}
		int square = 0;
		printf("Case #%d: %d\n", testCase, result.size());
		for (map<int, int, greater<int> >::const_iterator it = result.begin(); it != result.end(); it++) {
			printf("%d %d\n", it->first, it->second);
			square += it->first * it->first * it->second;
		}
		if (square != m * n) {
			fprintf(stderr, "Oh fuck! Test #%d\n", testCase);
		}
	}
	return 0;
}