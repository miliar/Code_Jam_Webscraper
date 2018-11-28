#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int Test,Case,N,I,M,D,Dis[300][300],A[200],F[200][300];

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	for (scanf("%d",&Test);Test;--Test) {
		scanf("%d%d%d%d",&D,&I,&M,&N);
		memset(Dis,2,sizeof(Dis));
		for (int i=0;i<256;i++)
		for (int j=0;j<256;j++)
		if (abs(i-j)<=M) Dis[i][j]=I;
		for (int k=0;k<256;k++)
		for (int i=0;i<256;i++)
		for (int j=0;j<256;j++)
			Dis[i][j]<?=Dis[i][k]+Dis[k][j];
		for (int i=1;i<=N;i++)
			scanf("%d",&A[i]);
		int Ret=1000000000;
		memset(F,2,sizeof(F));
		for (int i=1;i<=N;i++) {
			for (int j=0;j<256;j++) {
				F[i][j]=(i-1)*D;
				for (int k=0;k<256;k++)
				if (abs(j-k)<=M) F[i][j]<?=F[i-1][k];
				F[i][j]+=abs(A[i]-j);
			}
			for (int v=0;v<256;v++)
			for (int j=0;j<256;j++)
			for (int k=0;k<256;k++)
				F[i][j]<?=F[i][k]+Dis[k][j];
		}
		for (int i=0;i<256;i++)
			Ret<?=F[N][i];
		printf("Case #%d: %d\n",++Case,Ret);
	}
	return 0;
}
