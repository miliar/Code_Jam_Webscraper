#include <cstdio>
#include <algorithm>

using namespace std;

int candies[1200];

int main(){
	int T,CASE=1;
	int N;
	scanf("%d\n",&T);
	int xorSumLeft, xorSumRight;
	long long int sum, maxSum;
	while(T--){
		scanf("%d\n", &N);
		for(int i=0; i<N;i++){
			scanf("%d\n",&candies[i]);
		}
		sort(candies, candies+N);
		
		maxSum = -1;
		for(int i=N-1; i>0; i--){
			sum = 0;
			xorSumLeft = 0;
			xorSumRight = 0;
			for(int j=0; j<i; j++){
				xorSumLeft ^= candies[j];
			}
			for(int j=i;j<N;j++){
				xorSumRight ^= candies[j];
				sum += (long long int)candies[j];
			}
			if(xorSumLeft == xorSumRight && sum > maxSum){
				maxSum = sum;
			}
		}
		
		printf("Case #%d: ",CASE++);
		
		if(maxSum>0){
			printf("%lld\n",maxSum);
		}else{
			printf("NO\n");
		}
	}
}

