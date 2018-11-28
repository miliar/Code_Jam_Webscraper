
#include <cstdio>
#include <algorithm>
using namespace std;

int n, val[1005];

main() {
	int ntc;
	scanf("%d", &ntc);
	for (int test=1; test<=ntc; test++) {
		scanf("%d",&n);
		for (int i=0; i<n; i++) scanf("%d",val+i);
		
		sort(val,val+n);
		int tot=0, sum=0;
		for (int i=1; i<n; i++) {
			tot += val[i];
			sum ^= val[i];
		}
		
		printf("Case #%d: ", test);
		if (sum==val[0]) printf("%d\n", tot);
		else printf("NO\n");
	}
}
