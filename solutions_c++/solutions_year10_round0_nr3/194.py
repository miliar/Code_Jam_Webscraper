#include<stdio.h>
int in[1010],to[1010],at[1010],tt[1010];
long long sum[1010],as[1010],ts[1010];
int n;
inline void con(int *t1,long long *s1,int *t2,long long *s2,int *at,long long *as){
	int i;
	for(i=0;i<n;i++){
		at[i]=t2[t1[i]];
		as[i]=s1[i]+s2[t1[i]];
	}
}
int main(){
	int t,cas=1;
	scanf("%d",&t);
	while(t--){
		int r,k,i,j;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++)scanf("%d",&in[i]);
		for(i=0;i<n;i++){
			sum[i]=in[i];
			for(j=(i+1)%n;j!=i;j=(j+1)%n){
				if(sum[i]+in[j]>k)break;
				sum[i]+=in[j];
			}
			to[i]=j;
			at[i]=i;as[i]=0;
			//printf("sum[%d]=%I64d to[%d]=%d\n",i,sum[i],i,to[i]);
		}
		for(i=1;i<=r;i*=2){
			if(r&i){
				con(to,sum,at,as,tt,ts);
				for(j=0;j<n;j++){
					at[j]=tt[j];as[j]=ts[j];
				}
			}
			//for(j=0;j<n;j++)printf("%d sum[%d]=%I64d to[%d]=%d\n",i,j,sum[j],j,to[j]);
			con(to,sum,to,sum,tt,ts);
			for(j=0;j<n;j++){
				to[j]=tt[j];sum[j]=ts[j];
			}
		}
		printf("Case #%d: %I64d\n",cas++,as[0]);
	}
}
