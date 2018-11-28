#include<iostream>
#include<cstring>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<cmath>
#include<string>
#include<cstdlib>
#include<vector>
#include<cstdio>
#include<set>
#include<list>
#include<numeric>
#include<cassert>
#include<ctime>
#include<bitset>

using namespace std;

const int INF = 1000000000;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("in","r",stdin);
	freopen("out","w",stdout);
#endif

	int T, n, t= 1;
	for (scanf("%d", &T); T--; ) {
		int sum = 0, xorSum = 0, x, Min = INF;
		scanf("%d", &n);
		for (int i = 0; i < n; i ++) {
			scanf("%d", &x);
			xorSum ^= x;
			sum += x;
			Min = min(Min, x);
		}
		printf("Case #%d: ", t++);
		if(xorSum != 0) {
			puts("NO");
		} else {
			printf("%d\n", sum - Min);
		}
	}
	return 0;
}