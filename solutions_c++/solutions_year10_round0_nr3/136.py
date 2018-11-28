#include <stdio.h>
#define MAX		1024

int g[MAX];
int people[MAX];
int nexthead[MAX]; //next head group of the line

int main(){
	int T,R,k,N;
	int tc,i,j,r,head,tail;
	unsigned long long euros, sum;

	scanf("%d", &T);
	for(tc=1;tc<=T;tc++){
		sum = 0;
		euros = 0;

		scanf("%d %d %d", &R, &k, &N);
		for(i=0;i<N;i++){
			scanf("%d", &g[i]);
			sum+=g[i];

			nexthead[i] = -1;
		}
		if(sum <= k){
			euros = sum * R;
			printf("Case #%d: %lld\n", tc, euros);
			continue;
		}
//		printf("sum=%lld\n",sum);

		head = 0;
		for(r=0;r<R;r++){
//			printf("head=%d\n", head);
			if(nexthead[head]<0){
				i = head;
				for(sum=0;sum+g[i]<=k;){
					sum+=g[i];
					i = (i==N-1)? 0:i+1;
				}
				euros += sum;
				people[head]=sum;
				nexthead[head] = i;
				head = i;
			}
			else {
				euros += people[head];
				head = nexthead[head];
			}
		}
		printf("Case #%d: %lld\n", tc, euros);

	}
    return 0;
}
