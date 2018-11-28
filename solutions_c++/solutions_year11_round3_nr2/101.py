#include <stdio.h>
#include <algorithm>

#define MM 1000000

int T,C,N,P[MM+1],L;
__int64 t;
__int64 ans;

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int main(void){
	int test,i,n;
	__int64 sum;
	fscanf(in,"%d",&T);
	for(test=1;test<=T;test++){
		fscanf(in,"%d%I64d%d%d",&L,&t,&N,&C);
		for(i=N-1;i>=N-C;i--){
			fscanf(in,"%d",&P[i]);
		}
		for(i=N-C-1;i>=0;i--){
			P[i]=P[i+C];
		}
		sum=0;
		for(i=N-1;i>=0;i--){
			if(sum+P[i]>t/2)break;
			sum+=P[i];
		}
		if(i!=-1){
			P[i]=P[i]-t/2+sum;
			P[N++]=t/2-sum;
			n=i+1;
			std::sort(P,P+n);
			sum=0;
			for(i=n-1;i>=n-L&&i>=0;i--){
				sum+=P[i];
				P[i]=0;
			}
		}else sum=0;
		ans=0;
		for(i=0;i<N;i++){
			ans+=P[i]*2;
		}ans+=sum;
		fprintf(out,"Case #%d: %I64d\n",test,ans);
	}
	return 0;
}