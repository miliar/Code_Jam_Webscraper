#include <iostream>
#include <algorithm>
using namespace std;
typedef __int64 llong;

int main() {
	int t, n;
	llong st1[1024], st2[1024];
	scanf("%d", &t);
	for (int k = 0; k < t; ++k) {
		llong ret = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%I64d", &st1[i]);
		for (int i = 0; i < n; ++i)
			scanf("%I64d", &st2[i]);
		sort(st1, st1 + n);
		sort(st2, st2 + n, greater<llong>());
		for (int i = 0; i < n; ++i)
			ret += st1[i] * st2[i];
		printf("Case #%d: %I64d\n", k + 1, ret);
	}
	return 0;
}
