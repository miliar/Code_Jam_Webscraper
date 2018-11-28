#include <stdio.h>
#include <math.h>
int nT,T;
int N,M,A;
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	scanf("%d",&T);
	nT=T;
	while (T--){
		scanf("%d%d%d",&N,&M,&A);
		int i,j,k,l;
		for (i=0;i<=N;i++)
			for (j=0;j<=N;j++)
				for (k=0;k<=M;k++)
					for (l=0;l<=M;l++)
					{
						if (abs(i*l-j*k)==A)
							goto find;
					}

		printf("Case #%d: IMPOSSIBLE\n",nT-T);
		continue;
find:
		printf("Case #%d: 0 0 %d %d %d %d\n",nT-T,i,k,j,l);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;

}