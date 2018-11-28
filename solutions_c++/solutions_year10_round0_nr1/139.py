#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>

int main() {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T, ca, n, k;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ++ca) {
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",ca);
		if (k % (1<<n) != (1<<n) - 1)
			printf("OFF\n");
		else
			printf("ON\n");
	}
	return 0;
}
