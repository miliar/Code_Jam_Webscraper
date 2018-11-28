#include <iostream>
#include <stdio.h>

using namespace std;


int main() {
	int N,T,K,on,i,solve[31];
	scanf("%d",&N);
	solve[0] = 0;
	for (i = 1 ; i <= 30 ; i++)
		solve[i] = 2*solve[i-1]+1;

	for (i =1 ; i <= N ; i++) {
		scanf("%d %d",&T,&K);
		printf("Case #%d: ",i);	
		if (solve[T] > K)
			printf("OFF");	
		else if (solve[T] == K)
			printf("ON");
		else if ((K-solve[T])%(1+solve[T]) == 0)
			printf("ON");
		else
			printf("OFF");
		printf("\n");	

	}
	return 0;
}
