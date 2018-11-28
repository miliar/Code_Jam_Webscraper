#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

char s[50][50];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; ++t) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			char buf[50];
			scanf("%s", s[i]);
		}
		int res = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = i; j < n; ++j) {
				int right = 0;
				for (int k = 0; k < n; ++k)
					if (s[j][k] == '1')
						right = k;
				if (right <= i) {
					for (int k = j; k > i; --k)
						strcpy(s[k], s[k - 1]);
					res += j - i;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", t + 1, res);
	}
	return 0;
}