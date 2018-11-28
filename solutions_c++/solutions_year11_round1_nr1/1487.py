
#include <iostream>
#include <cstdlib>
#include <cstdio>

#include <vector>
#include <algorithm>


using namespace std;

int main (void)
{
	int T, N, PD, PG;
	int i, j;

	scanf ("%d", &T);
	for (i = 1; i <= T; i++) {
		printf ("Case #%d: ", i);

		scanf ("%d %d %d", &N, &PD, &PG);

		for (j = 1; j <= N; j++) {
			int tw = j*PD/100;
			float fw = (float)j*PD/100;
			if (tw == fw) {
				if (PD!=0 && PG ==0 ||
				PG==100 && PD != 100) {
				}
				else {
					printf ("Possible\n");
					break;
				}
			}
		}
		if (j > N) { printf ("Broken\n"); }
	}

	return 0;
}

