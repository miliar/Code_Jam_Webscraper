#include <cstdio>
#include <cstring>
char a[60][60];
int i,j,k,s,t,n,m,T,I,K,x,y;
int fx[4][2]={{0,1},{1,0},{1,1},{1,-1}};
bool ans[3];

bool ok(int x,int y)
{
	return x>=0 && x<n && y>=0 && y<n;
}
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		memset(ans,0,sizeof ans);
		scanf("%d%d\n",&n,&K);
		for (i=0;i<n;++i)
			gets(a[i]);
		for (i=0;i<n;++i)
		{
			k=n-1;
			for (j=n-1;j>=0;--j)
				if (a[i][j]!='.')
				{
					a[i][k]=a[i][j];
					--k;
				}
			for (j=k;j>=0;--j)
				a[i][j]='.';
		}
		for (i=0;i<n;++i)
		{
			for (j=0;j<n;++j)
			if (a[i][j]!='.')
			{
				if (a[i][j]=='R') m=1; else m=2;
				if (ans[m]) continue;
				for (k=0;k<4;++k)
				{
					x=i;y=j;
				//	printf("%d %d:\n",i,j);
					bool pan=1;
					for (t=1;t<K;++t)
					{
						x=x+fx[k][0];
						y=y+fx[k][1];
					//	printf("%d %d\n",x,y);
						if (!(ok(x,y) && a[x][y]==a[i][j]))
						{
							pan=0;
							break;
						}
					}
					if (pan)
						ans[m]=1;
				}
			}
		}
		printf("Case #%d: ",I);
		if (ans[1] && ans[2]) printf("Both\n");
		else if (ans[1]) printf("Red\n");
		else if (ans[2]) printf("Blue\n");
		else printf("Neither\n");
	}
}
							
				
	
