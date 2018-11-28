#include <cstdio>

typedef long long LL;

const int N=1001;

int A[N];
LL sum[N];
int nxt[N];

int main(){
	int cas,ic;
	scanf("%d",&cas);
	for(ic=1;ic<=cas;ic++){
		int i,j,r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(i=0;i<n;i++) scanf("%d",&A[i]);
		for(i=n;i<2*n;i++) A[i]=A[i-n];
		for(i=0;i<n;i++){
			LL s=A[i];
			for(j=i+1;j<i+n&&s+A[j]<=k;j++) s+=A[j];
			sum[i]=s;
			nxt[i]=j%n;
		}
		LL ans=0;
		int pos=0;
		for(i=0;i<r;i++){
			ans+=sum[pos];
			pos=nxt[pos];
		}
		printf("Case #%d: %I64d\n",ic,ans);
	}
	return 0;
}
