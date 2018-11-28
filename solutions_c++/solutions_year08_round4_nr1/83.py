#include <stdio.h>
#include <vector>
using namespace std;
int T,nT;
int M,V;
int stat[10000][2];
int chg[10000][2];
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	scanf("%d",&T);
	nT=T;
	while (T--)
	{
		scanf("%d%d",&M,&V);
		int i,j,k,l;
		for (i=0;i<(M-1)/2;i++)
			scanf("%d%d",&stat[i][0],&stat[i][1]);
		for (;i<M;i++)
		{
			int t;
			scanf("%d",&t);
			chg[i][t]=0;
			chg[i][1-t]=-1;
		}
		for (i=(M-1)/2;i--;)
		{
			//for node i
			chg[i][0]=-1;
			chg[i][1]=-1;
			for (j=0;j<2;j++) if (chg[i*2+1][j]!=-1)
				for (k=0;k<2;k++) if (chg[i*2+2][k]!=-1)
				{
					if (stat[i][0]==1)
						l=j&k;
					else
						l=j|k;
					if (chg[i][l]==-1||chg[i][l]>chg[i*2+1][j]+chg[i*2+2][k])
						chg[i][l]=chg[i*2+1][j]+chg[i*2+2][k];
				}

			if (stat[i][1]==1)
			for (j=0;j<2;j++) if (chg[i*2+1][j]!=-1)
				for (k=0;k<2;k++) if (chg[i*2+2][k]!=-1)
				{
					if (stat[i][0]==1)
						l=j|k;
					else
						l=j&k;
					if (chg[i][l]==-1||chg[i][l]>chg[i*2+1][j]+chg[i*2+2][k]+1)
						chg[i][l]=chg[i*2+1][j]+chg[i*2+2][k]+1;
				}
		}

		printf("Case #%d: ",nT-T);
		if (chg[0][V]==-1) printf("IMPOSSIBLE\n");
		else printf("%d\n",chg[0][V]);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}