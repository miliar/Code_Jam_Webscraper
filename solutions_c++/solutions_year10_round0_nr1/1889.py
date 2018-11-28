#include <cstdio>

using namespace std;

int main()
{
	int t, n, k;
	scanf("%d ",&t);
	for (int i=1;i<=t;i++) {
		scanf("%d %d ",&n, &k);
		n = (1<<n);
		if (k%n==n-1) printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
	return 0;
}
