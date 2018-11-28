#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int T,N,ci[1001],i,tmp,j,sum[32],total,minp;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		memset(sum,0,sizeof(sum));
		total=0;minp=100000000;
		scanf("%d",&N);
		for(i=0;i<N;i++){
			scanf("%d",&ci[i]);
			total+=ci[i];
			if(minp>ci[i])minp=ci[i];
			tmp=ci[i];j=0;
			while(tmp!=0){
				if((tmp & 1)==1)sum[j]++;
				tmp>>=1;j++;
			}
		}
		for(i=0;i<32;i++){
			if(sum[i]%2)break;
		}
		if(i<32)printf("Case #%d: NO\n",t);
		else printf("Case #%d: %d\n",t,total-minp);
	}
	
	return 0;
}
