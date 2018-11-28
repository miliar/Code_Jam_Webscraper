#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define inf 10000000000000LL
int Test,N,M,C[1030],P[12][1030];
long long F[12][1030][1030];

inline long long Calc(int k,int l,int r,int d)
{
	if (F[k][l][r]>=0) return F[k][l][r];
	F[k][l][r]=inf;
	if (d==1) {
		if (k>=C[l] && k>=C[r]) return F[k][l][r]=0;
		if (k+1>=C[l] && k+1>=C[r]) return F[k][l][r]=P[d][l];
		return F[k][l][r];
	}
	int m=(l+r)>>1;
	F[k][l][r]<?=Calc(k,l,m,d-1)+Calc(k,m+1,r,d-1);
	F[k][l][r]<?=Calc(k+1,l,m,d-1)+Calc(k+1,m+1,r,d-1)+P[d][l];
	return F[k][l][r];
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&Test);
	for (int Case=1;Case<=Test;Case++) {
		scanf("%d",&N);M=1<<N;
		for (int i=0;i<M;i++) {
			scanf("%d",&C[i]);
			C[i]=N-C[i];
		}
		for (int i=1;i<=N;i++)
		for (int j=0;j<M;j+=1<<i)
			scanf("%d",&P[i][j]);
		memset(F,-1,sizeof(F));
		printf("Case #%d: %I64d\n",Case,Calc(0,0,M-1,N));
	}
	return 0;
}
