#include <stdio.h>
#include <stdlib.h>

int main()
{
	int nn,ii,i,j,k;
	int w,h,r,a,b;
	int x[100];
	int y[100];
	int e[1000][1000];
	scanf("%d\n",&nn);
	for (ii=0;ii<nn;++ii)
	{
		scanf("%d %d %d",&h,&w,&r);
		for (i=0;i<r;++i)
		{
			scanf("%d %d",&a,&b);
			x[i]=a;
			y[i]=b;
		}
		e[0][0]=1;
		for (i=1;i<w;++i) e[0][w]=0;
		for (i=1;i<h;++i) for (j=0;j<w;++j)
		{
			e[i][j]=0;
			for (k=0;k<r;++k) if (i+1==x[k] && j+1==y[k]) break;
			if (k<r) continue;
			if (i>=2 && j>=1) e[i][j]=(e[i][j]+e[i-2][j-1])%10007;
			if (i>=1 && j>=2) e[i][j]=(e[i][j]+e[i-1][j-2])%10007;
		}
		printf("Case #%d: %d\n",ii+1,e[h-1][w-1]);
	}
	return 0;
}
