#include <cstdlib>
#include <cstdio>
#include <memory.h>

int main(int argc, char **argv) {

	int nbTests;
	int s, res, nb, min;

	int nn[31], ss[31];

	for(int i=0; i<31; ++i) {
		nn[i] = (i+2)/3;
		ss[i] = (i+4)/3;
	}

	scanf("%d", &nbTests);

	for(int n=1; n<=nbTests; ++n) {
		scanf("%d%d%d", &nb, &s, &min);
		res = 0;
		int tt;
		for(int i=0; i<nb; ++i) {
			scanf("%d", &tt);
			if(nn[tt] >= min) {
				res++;
			}
			else if(tt > 1 && tt < 29 && s && ss[tt] >= min && nn[tt] < min) {
				res++;
				s--;
			}
		}

		printf("Case #%d: %d\n", n, res);
	}

	return 0;
}