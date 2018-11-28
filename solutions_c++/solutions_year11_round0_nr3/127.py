#include <stdio.h>
#include <string.h>

int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,N;
	scanf("%d",&T);
	for (int t = 1;t <= T;t++){
		scanf("%d",&N);
		int S = 0,R = 0;
		int min = 0x7fffffff,x;
		for (int i = 0;i < N;i++){
			scanf("%d",&x);
			if (x < min) min = x;
			S += x;
			R ^= x;
		}
		printf("Case #%d: ",t);
		if (R)
			puts("NO");
		else
			printf("%d\n",S-min);
	}
	//while(1);
	return 0;
}
