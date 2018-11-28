#include<stdio.h>

typedef __int64 LL;

#define MAX 100

int n,k;
LL b,t;
LL x[MAX], v[MAX];

int main(){

	int T,N;
	int i,miss,cnt,swp;

	scanf("%d",&T);
	for(N=1;N<=T;N++){
	
		scanf("%d%d%I64d%I64d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
			scanf("%d",&x[i]);
		for(i=0;i<n;i++)
			scanf("%d",&v[i]);

		miss = cnt = swp = 0;
		for(i=n-1;i>=0 && cnt<k;i--){
			if(x[i]+t*v[i]>=b){
				swp += miss;
				cnt++;
			}
			else{
				miss++;
			}
		}
		if(cnt==k)
			printf("Case #%d: %d\n",N,swp);
		else
			printf("Case #%d: IMPOSSIBLE\n",N);
	}

	return 0;
}