#include <stdio.h>
#include <string>
using namespace std;

int candy[15];
int N;

void run(int fall){
	scanf("%d", &N);
	//printf("N: %d\n", N);
	for(int i=0; i<N; i++){
		scanf("%d", &candy[i]);
		//printf("candy[%d] = %d\n", i, candy[i]);
	}
	int best = 0;
	for(int mask=1; mask+1 < (1<<N); mask++){
		//printf("N %d mask %d\n", N, mask);
		int normalSum=0;
		int felSumA=0;
		int felSumB=0;
		for(int i=0; i<N; i++){
			if(mask&(1<<i)){
				normalSum += candy[i];
				felSumA ^= candy[i];
			} else {
				felSumB ^= candy[i];
			}
		}
		if(felSumA == felSumB && normalSum > best){
			best = normalSum;
		}
	}
	printf("Case #%d: ", fall+1);
	if(best){
		printf("%d\n", best);
	} else {
		printf("NO\n");
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for(int i=0; i<T; i++){
		run(i);
	}
}
