#include <cstdio>

int opt[150][300];
int a[150];
int i,j,k,s,t,n,m,T,I,de,is;

int abs(int x)
{
	return x<0?-x:x;
}
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		scanf("%d%d%d%d",&de,&is,&m,&n);
	//	printf("%d %d %d %d\n",de,is,m,n);
		for (i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
		//	printf("%d ",a[i]);
		}
	//	printf("\n");
		for (i=0;i<n;++i)
			for (j=0;j<=255;++j)
				opt[i][j]=10000000;
		for (j=0;j<=255;++j)
			opt[0][j]=abs(j-a[0]);
		for (i=1;i<n;++i)
		{
			for (j=0;j<=255;++j)
			{
				for (k=0;k<=255;++k)
				{
					if (k!=j && m!=0)
						opt[i][k]<?=opt[i-1][j]+abs(k-a[i])+(abs(k-j)-1)/m*is;
					else if (k==j)
						opt[i][k]<?=opt[i-1][j]+abs(k-a[i]);
				}
				opt[i][j]<?=opt[i-1][j]+de;
				opt[i][j]<?=de*i+abs(j-a[i]);
				opt[i][j]<?=de*(i+1)+is;
			}
		}
		//printf("%d %d %d\n",opt[0][1],opt[1][3],opt[2][5]);
		int ans=100000000;
		for (j=0;j<=255;++j)
			if(opt[n-1][j]<ans) ans=opt[n-1][j];
		printf("Case #%d: %d\n",I,ans);
	}
	return 0;
}
