#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX = 1200;

int main() {
	int T, n, x;
	int ret, cas = 1;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	while (T--) {
		scanf("%d", &n);
		ret = 0;
		for (int i = 1; i <= n; i++) {
			scanf("%d", &x);
			if (x != i)
				ret++;
		}
		printf("Case #%d: %d.000000\n", cas++, ret);
	}

	return 0;
}
