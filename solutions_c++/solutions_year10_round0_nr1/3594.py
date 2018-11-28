#include <cstdio>
#include <cstring>

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int cases, N, K;
	scanf("%d", &cases);
	for (int cc = 1; cc <= cases; ++cc) {
		scanf("%d %d", &N, &K);
		int t = (1 << N) - 1;
		
		printf("Case #%d: ", cc);
		if ((K & t) == t) puts("ON");
		else
			puts("OFF");
	}
	
	return 0;
}

