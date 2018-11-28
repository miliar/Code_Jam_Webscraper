#include <stdio.h>

long long x[600][600];
long long y[600][600];
long long z[600];

int main()
{
	int i,j,k;
	long long p;
	for (i=0;i<600;++i) 
	{
		y[i][0]=y[i][i]=1;
		for (j=1;j<i;++j) y[i][j]=(y[i-1][j-1]+y[i-1][j])%100003; 
	}
	for (i=2;i<600;++i) 
	{
		z[i]=1; x[i][1]=1;
		for (j=2;j<i;++j)
		{
			x[i][j]=0;
			for (k=1;k<j && k<=i-j;++k) 
			{
				p=x[j][j-k]*y[i-j-1][k-1];
				x[i][j]=(x[i][j]+p)%100003;
				z[i]=(z[i]+p)%100003;
			}
		}
	}
	scanf("%d",&j);
	k=0;
	while (scanf("%d",&j)==1) printf("Case #%d: %lld\n",++k,z[j]);
	return 0;
}
