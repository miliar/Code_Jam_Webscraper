#include <stdio.h>

int main()
{
	int T;
	scanf("%d", &T);
	long long N;
	int PD, PG;
	for (int ncas = 1; ncas <= T; ncas++) {
		scanf("%lld%d%d", &N, &PD, &PG);
		printf("Case #%d: ", ncas);
		if ((PD != 100 && PG == 100) || (PD != 0 && PG == 0)) {
			printf("Broken\n");
			continue;
		}
		if (N >= 100) {
			printf("Possible\n");
		} else {
			bool can=false;
			for (int i = 1; i <= N; i++) {
				if ((i * PD) % 100 == 0) {
					can = true;
					break;
				}
			}
			if (can) {
				printf("Possible\n");
			} else {
				printf("Broken\n");
			}
		}
	}
	return 0;
}
