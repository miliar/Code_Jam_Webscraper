#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

typedef long long lint;

int main()
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n;
		int sum = 0;
		int mini = 100000000;
		int vxor = 0;

		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			int v;
			scanf("%d", &v);
			sum += v;
			mini = min(mini, v);
			vxor ^= v;
		}

		if (vxor)
			printf("Case #%d: NO\n", t+1);
		else
			printf("Case #%d: %d\n", t+1, sum-mini);
	}

	return 0;
}
