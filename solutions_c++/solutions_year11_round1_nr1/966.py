#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int main() {
	int T;

	scanf("%d", &T);

	for (int caso = 1; caso <= T; caso++) {
		unsigned long long N, PD, PG, i;

		scanf("%llu %llu %llu", &N, &PD, &PG);

		if ((PG == 100 && PD != 100) || (PG == 0 && PD != 0)) {
			printf("Case #%d: Broken\n", caso);
			continue;
		}

		for (i = 1; i <= N && (i*PD)%100 != 0; i++);

		if (i > N) {
			printf("Case #%d: Broken\n", caso);
			continue;
		}

		printf("Case #%d: Possible\n", caso);
		continue;
	}

	return 0;
}
