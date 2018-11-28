#include <cstdio>
#include <cstring>
using namespace std;

const int M = 64;
char matrix[M][M];
int pos[M];

void swap(int &a, int &b) {
	int c = a;
	a = b;
	b = c;
}

int main() {
	int t, n;
	scanf("%d", &t);
	for (int kase = 0; kase < t; ++kase) {
		scanf("%d", &n);
		memset(matrix, 0, sizeof(matrix));
		memset(pos, 0, sizeof(pos));
		for (int i = 0; i < n; ++i) {
			scanf("%s", matrix[i]);
		}
		for (int i = 0; i < n; ++i) {
			for (int j = n - 1; j >=0; --j) {
				if (matrix[i][j] == '1') {
					pos[i] = j;
					break;
				}
			}
		}
		int ret = 0;
		for (int i = 0; i < n; ++i) {
			if (pos[i] > i) {
				for (int j = i; j < n; ++j) {
					if (pos[j] <= i) {
						for (int k = j; k > i; --k) {
							swap(pos[k], pos[k-1]);
							ret ++;
						}
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", kase + 1, ret);
	}
	return 0;
}

