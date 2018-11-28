#include<stdio.h>

int main()
{
//	freopen("t.txt","r",stdin);
	int T,N,S,p,i=0,j=0;
	int sure,sup,count;
	int t;
	scanf("%d",&T);
	while(i<T){
		count=0;
		scanf("%d %d %d",&N,&S,&p);
		if(0 == p){
			for(j=0;j<N;j++) scanf("%d",&t);
			printf("Case #%d: %d\n",i+1,N);
			i++;
			continue;
		}
		sure = p*3-2;
		sup = (1==p)?31:(p*3-4);
		for(j=0;j<N;j++){
			scanf("%d",&t);
			if(t >= sure){
				count++;
			}
			else{
				if(S > 0 && t >= sup){
					count++;
					S--;
				}
			}
		}
		printf("Case #%d: %d\n",i+1,count);
		i++;
	}
	return 0;
}

