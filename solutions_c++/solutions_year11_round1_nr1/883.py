#include <cstdio>
#include <algorithm>

using namespace std;

const int LIMIT = 500;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	long long cases, n, pd, pg;
	scanf("%lld", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		scanf("%lld%lld%lld", &n, &pd, &pg);
		printf("Case #%d: ", cc);
		if (pd && !pg) {
			puts("Broken");
			continue;
		}
		if (pg == 100 && pd != 100) {
			puts("Broken");
			continue;
		}
		int flag = 0;
		if (n > LIMIT) n = LIMIT;
		for (int i = n; i; --i) {
			if (i * pd % 100 == 0) {
				puts("Possible");
				flag = 1;
				break;
			}
		}
		if (!flag) puts("Broken");
	}
	return 0;
}
