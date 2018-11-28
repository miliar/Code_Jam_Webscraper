#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>

using namespace std;

#define abs(x) ((x) < 0 ? (-(x)) : (x))
#define min(x, y) ((x) < (y) ? (x) : (y))
#define max(x, y) ((x) > (y) ? (x) : (y))

#define mp make_pair
#define pb push_back

typedef long long i64;

const int MAXN = 300;

char s[MAXN][MAXN];
char ss[10000];

int main() {
	int T; scanf("%d\n", &T);
	for (int tt = 0; tt < T; ++tt) {
		int k;
		gets(ss);
		sscanf(ss, "%d", &k);
		for (int i = 1; i <= 2 * k - 1; ++i) {
			gets(s[i] + 1);
			for (int j = 1; !isdigit(s[i][j]); ++j) {
				s[i][j] = '#';
			}
			int n = strlen(s[i] + 1);
			while (n < 2 * k - 1) {
				s[i][n + 1] = '#';
				++n;
			}
			s[i][n + 1] = 0;
// 			cout << (s[i] + 1) << endl;
		}
		int result = 10000000; //(k + 2 * (k - 1)) * (k + 2 * (k - 1)) - k * k;
		for (int x = 1; x <= 2 * k - 1; ++x) {
			bool fx = true;
			for (int y = 1; y <= 2 * k - 1; ++y) {
				bool f = true;
				int S = 0;
				for (int a = 1; a <= 2 * k - 1; ++a) {
					for (int b = 1; b <= 2 * k - 1; ++b) {
						if (s[a][b] != '#') {
							int c = 2 * x - a;
							if ((c >= 1) && (c <= 2 * k - 1) && (s[c][b] != '#')) {
								if (s[a][b] != s[c][b]) {
									f = false;
									fx = false;
									break;
								}
							}
							int d = 2 * y - b;
							if ((d >= 1) && (d <= 2 * k - 1) && (s[a][d] != '#')) {
								if (s[a][b] != s[a][d]) {
									f = false;
									break;
								}
							}
						}
/*						if ((x == 2) && (y == 3)) {
//							cout << a << " " << b << " " << c << " " << d << " " << s[a][b] << " " << s[c][d] << endl;
						}*/
/*						if (!((c < 1) || (d < 1) || (c > 2 * k - 1) || (d > 2 * k - 1)))
							if ((s[a][b] != '#') && (s[c][d] != '#') && (s[a][b] != s[c][d])) {
								f = false;
								break;
							}*/
						if (isdigit(s[a][b])) {
//							S = max(S, max(abs(a - x), abs(b - y)));
							S = max(S, abs(a - x) + abs(b - y));
						}
					}
					if (!f) break;
				}
				if (!fx) break;
//				cout << x << " " << y << " " << f << " " << S << endl;
				if (f) {
					int K = S + 1;
					result = min(result, K * K - k * k);
				}
			}
		}
		printf("Case #%d: %d\n", tt + 1, result);
	}
	return 0;
}
