#include<stdio.h>
long long sum,tmp;
long long a[2001];//,sum[2001];
long long pos[1001];
long long cost[1001];
main(){
	long long t,i,j,k;
	long long N,T,K,R;
	scanf("%I64d",&T);
	for(t=1;t<=T;t++){
		scanf("%I64d%I64d%I64d",&R,&K,&N);
		sum=0;
		//sum[0]=0;
		for(i=0;i<N;i++){
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		/*for(i=1;i<N;i++){
			sum[i]=sum[i-1]+a[i];
		}*/
		for(i=0;i<N;i++){
			
			tmp=0;
			//while(K-tmp>=sum)tmp+=sum;
			k=0;
			for(j=i;;){
				if(k&&j==i)break;
				if(tmp+a[j]>K)break;
				tmp+=a[j];
				if(j==N-1){
					j=0;
					k=1;
				} else {
					j++;
				}
			}
			cost[i]=tmp;
			pos[i]=j;
		}
		k=0;
		sum=0;
		for(i=0;i<R;i++){
			sum+=cost[k];
			k=pos[k];
		}
		printf("Case #%I64d: %I64d\n",t,sum);
	}
}
