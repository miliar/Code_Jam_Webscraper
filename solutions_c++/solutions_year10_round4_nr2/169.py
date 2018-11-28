#include <stdio.h>
#include <string.h>

#define MAX 10

int M[1<<MAX];
int P[1<<MAX];

int ans[1<<MAX][MAX];

int go(int v,int k,int l,int r) {
	if(l==r) return 0;
	if(ans[v][k]>=0) return ans[v][k];
	bool isZeros=false;
	for(int i=l;i<=r;++i)
		if(M[i]==k) {
			isZeros=true;
			break;
		}
	int res=P[v]+go(v<<1,k,l,(l+r)>>1)+go((v<<1)+1,k,((l+r)>>1)+1,r);
	if(!isZeros) {
		int tmp=go(v<<1,k+1,l,(l+r)>>1)+go((v<<1)+1,k+1,((l+r)>>1)+1,r);
		if(tmp<res) res=tmp;
	}
	ans[v][k]=res;
	return res;
}

int layers[MAX][1<<MAX];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tests;
	scanf("%d",&tests);
	for(int test=1;test<=tests;++test) {
		int n;
		scanf("%d",&n);
		int v=1;
		layers[0][0]=v;
		for(int i=1;i<n;++i) {
			for(int j=0;j<(1<<i);++j)
				layers[i][j]=++v;
		}
		for(int i=0;i<(1<<n);++i)
			scanf("%d",&M[i]);
		for(int i=0;i<n;++i) {
			for(int j=0;j<(1<<(n-1-i));++j)
				scanf("%d",&P[layers[n-1-i][j]]);
		}
		memset(ans,0xFF,sizeof(ans));
		printf("Case #%d: %d\n",test,go(1,0,0,(1<<n)-1));
	}
	return 0;
}
