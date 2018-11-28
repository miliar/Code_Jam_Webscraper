#include <stdio.h>


int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,N;
	scanf("%d",&T);
	for(int i=0;i <T; i++){
		scanf("%d",&N);
		int sum =0, xor_sum = 0 ,min_el= -1,a;
		for(int j = 0; j<N;j ++){
			scanf("%d",&a);
			if(min_el==-1 || a<min_el)
				min_el = a;
			sum+=a;
			xor_sum^=a;
		}
		printf("Case #%d: ",i+1);
		if(xor_sum!=0)
			printf("NO\n");
		else
			printf("%d\n",sum - min_el);
	}

	return 0;
}