#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int T, N, C;
int num[100];
char mark[101];
int sum = 0;
int psum = 0;

int int_cmp(const void *a, const void *b)  { 
    const int *ia = (const int *)a; 
    const int *ib = (const int *)b;
    return *ia  - *ib; 
} 

void reset() {
	sum = 0;
	psum = 0;
	memset(num, 0, sizeof(num));
	memset(mark, 0, sizeof(mark));
}

void next() {
	int pos = 0;
	do {
		sum ^= mark[pos];
		psum ^= mark[pos];
		mark[pos] ^= 1;
		pos++;
	} while (mark[pos-1]==0 && pos<N);
}

int main(int argc, char* argv[]) {
	scanf("%d", &T);
	int cs = 0;
	while (cs++<T) {
		reset();
		printf ("Case #%d: ", cs); fflush(0); 
		bool not_done = true;
		scanf("%d", &N);
		int i=0;
		while (i<N) {
			scanf("%d", &(num[i]));
			sum ^= num[i];
//			printf (" [%d]", num[i]);
			i++;
		}
//		printf("\n");

		qsort(num, N, sizeof(int), int_cmp);
		
		do {
			next();
//			for (int x=0; x<N; x++) printf("%d", (int)mark[x]); printf("\n");
//			for (int x=0; x<N; x++) printf("%d", (int)num[x]); printf("\n");

			if (sum==psum && mark[N-1]==0) {
				long long all = 0;
				i=0;
				while (i<N) {
					if (mark[i]==0) { all+= (long long)num[i]; /*printf(" %d+%d", i, num[i]);*/ }
					//else printf(" %d#%d", i, num[i]);
					i++;
				}
				printf("%lld\n", all);
				not_done = false;
				mark[N-1] = 1;
			}
		} while (mark[N-1]==0);
		if (not_done)printf("NO\n");
	}
	return 0;
}
