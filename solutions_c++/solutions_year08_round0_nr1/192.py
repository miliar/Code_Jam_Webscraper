#include <cstdio>
#include <map>
#include <string>

using namespace std;

char s[2000];

int a[2000];
int w[2000][2000];

int main() {
	int T;
	gets(s); sscanf(s, "%d", &T);
	for (int t = 0; t < T; ++t) {
		map<string, int> d;
		int n, m;
		gets(s); sscanf(s, "%d", &n);
		for (int i = 0; i < n; ++i) {
			gets(s);
			d[s] = i;
		}
		gets(s); sscanf(s, "%d", &m);
		for (int i = 0; i < m; ++i) {
			gets(s);
			a[i] = d[s];
		}
		memset(w, ~0, sizeof(w));
		int result = -1;
		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				if (!i) {
					if (a[i] != j) w[i][j] = 0;
				} else if (a[i] != j) {
					w[i][j] = w[i - 1][j];
					for (int k = 0; k < n; ++k) if (k != j) {
						if (w[i - 1][k] != -1) {
							if ((w[i][j] == -1) || (w[i][j] > w[i - 1][k] + 1)) {
								w[i][j] = w[i - 1][k] + 1;
							}
						}
					}
				}
				if ((i == m - 1) && (w[i][j] != -1) && ((result == -1) || (result > w[i][j]))) {
					result = w[i][j];
				}
			}
		}
		if (!m) result = 0;
		printf("Case #%d: %d\n", t + 1, result);
	}
	return 0;
}
