#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
typedef long long LL;
using namespace std;
int main() {
	int t;
	LL s, e, c;
	scanf("%d", &t);
	for(int zz=1;zz<=t;zz++) {
		scanf("%lld%lld%lld", &s, &e, &c);
		int cnt = 0;
		while (s < e)
			cnt ++, s *= c;
		int ans = 0, z = 1;
		while (z < cnt)
			z *= 2, ans++;
//		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n", zz, ans);
//		printf(" (%lld)\n", gao);
	}
}
