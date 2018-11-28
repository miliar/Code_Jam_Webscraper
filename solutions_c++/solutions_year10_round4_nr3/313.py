#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <math.h>

using namespace std;

int p[300][300];

int main()
{
	int case_c,r,i,j,k,l,m,x,y,x2,y2;
	scanf("%d",&case_c);
	case_c=0;
	while (scanf("%d",&r)==1)
	{
		memset(p,0,sizeof(p));
		for (i=0;i<r;++i)
		{
			scanf("%d %d %d %d",&x,&y,&x2,&y2);
			for (j=x;j<=x2;++j)	for (k=y;k<=y2;++k) p[j][k]=1;
		}
		l=0;
		while (1)
		{
			m=0;
			/*for (i=0;i<10;++i) { for (j=0;j<10;++j) if (p[j][i]==1) printf("X"); else printf("_"); printf("\n");}
			printf("\n");*/
			for (i=300;i>0;--i) for (j=300;j>0;--j) if (p[i][j])
			{
				++m;
				if (p[i-1][j]==0 && p[i][j-1]==0) p[i][j]=0;
			} else
			{
				if (p[i-1][j]==1 && p[i][j-1]==1) p[i][j]=1;
			}
			for (i=300;i>0;--i) if (p[i][0]) { ++m; p[i][0]=0; }
			for (i=300;i>0;--i) if (p[0][i]) { ++m; p[0][i]=0; }
			if (m==0) break;
			++l;
		}
		printf("Case #%d: %d\n",++case_c,l);
	}
	return 0;
}
