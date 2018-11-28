#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
int a[10000], mi;

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int T;
	scanf("%d", &T);
	for (int ti=1;ti<=T;ti++) {
		scanf("%d", &n);
		printf("Case #%d: ", ti);
		int xor_sum = 0, sum = 0;
		for (int i=0;i<n;i++) {
			scanf("%d", &a[i]);
			if (i==0) mi = a[i]; else if (a[i] < mi) mi = a[i];
			sum += a[i];
			xor_sum = xor_sum ^ a[i];
		}
		if (xor_sum != 0) printf("NO\n"); else
			printf("%d\n", sum - mi);
	}
	return 0;
}
