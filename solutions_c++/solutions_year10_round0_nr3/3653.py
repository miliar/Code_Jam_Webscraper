#include <cstdio>
#include <stdlib.h>
#include <memory.h>

using namespace std;

long long R, k , N;
long long *gi, *givalue;
unsigned int *gipos;

void gengi()
{
	int i, j, pos;
	long long ktemp;
	for(i = 0; i < N; i++) {
		ktemp = k;
		pos = i;
        for (j = 0; j < N; j++) {
            if (ktemp >= *(gi + pos)) {
                ktemp = ktemp - *(gi + pos);
				if(pos >= N - 1) {
					pos = 0;
				} else {
					pos++;
				}
			} else {
				break;
			}
        }
		*(givalue + i) = k - ktemp;
		*(gipos + i) = pos;
	}
}



int main(int argc, char *argv[]) 
{
	int i, pos, T, tc;
	long long gain;
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
    
	scanf("%d", &T);
    
	for(tc = 0; tc < T; tc ++) {
		scanf("%ld %ld %ld", &R, &k, &N);

		gi = (long long*) malloc(N * sizeof(long long));
		givalue = (long long*) malloc(N * sizeof(long long));
		gipos = (unsigned int*) malloc(N * sizeof(unsigned int));
        
		memset(gi, 0x00, N * sizeof(long long));
		memset(givalue, 0x00, N * sizeof(long long));
        memset(gipos, 0x00, N * sizeof(unsigned int));

		for(i = 0; i < N; i++) {
			scanf("%ld", gi+i);
		}

		gengi();

		gain = 0;
		pos = 0;
		for(i = 0; i < R; i++) {
			gain = gain + givalue[pos];
			pos = gipos[pos];
		}

		free(gi);
		free(givalue);
		free(gipos);

		printf("Case #%d: %ld\r\n", tc + 1, gain);
	}
}