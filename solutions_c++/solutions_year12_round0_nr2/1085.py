#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
	return *(int *)b - *(int *)a;
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;				//t cases
	int i,j;				//loop varibles
	int n, s, p;		//N Googler, S -- number of surprising triplets of scores, a best result of at least P
	int Googler[200];
	int count;
	scanf("%d",&t);
	for( i = 1; i <= t; i++) {
		scanf("%d %d %d", &n, &s, &p);
		for(j = 0; j < n; j++) {
			scanf("%d",&Googler[j]);
		}

		qsort(Googler,n,sizeof(Googler[0]),cmp);
		/*for(j = 0; j < n; j++) {
			printf("%d ", Googler[j]);
		}
		printf("\n");*/
		count = 0;
		for(j = 0; j < n; j++) {
			if((Googler[j] + 2) / 3 >= p) {
				count++;
			} else {
				if((Googler[j] % 3 != 1) && ((Googler[j] + 2) / 3) == p - 1 && s >= 1 && (Googler[j] + 2) / 3 >= 1) {
					count++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n",i,count);
	}
	return 0;
}