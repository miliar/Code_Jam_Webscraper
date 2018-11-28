#include <cstdio>

int c[1000];

int maximum(int a, int b){
	if(a>b)
		return a;
	return b;
}

int main() {

	int T;
	scanf("%d ", &T);
	for(int t=0; t<T; ++t) {

		int N;
		scanf("%d ", &N);
		for(int n=0; n<N; ++n) {
			scanf("%d ", &c[n]);
		}

		int best = -1;

		int max = (1<<N)-1; // -1 wegen not null
		for(int i=1; i<max; ++i) {
			int sum1 = 0, sum2 = 0;
			int xor1 = 0, xor2 = 0;
			for(int j=0; j<N; ++j) {
				//printf("%d", (i>>j)%2);
				if( (i>>j)%2==1 ) {
					sum1 += c[j];
					xor1 ^= c[j];
				} else {
					sum2 += c[j];
					xor2 ^= c[j];
				}
			}
			//printf(" erg: %d, best %d\n",  maximum(sum1, sum2), best);
			if(xor1==xor2) {
				best = maximum(best, maximum(sum1, sum2));
			}
		}
		
		printf("Case #%d:", t+1);
		if(best == -1)
			printf(" NO\n");
		else
			printf(" %d\n", best);
	}


	return 0;
}
