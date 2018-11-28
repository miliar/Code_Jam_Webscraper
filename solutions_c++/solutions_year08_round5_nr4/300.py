#include<cstdio>
#include<memory>

int a[111][111],b[111][111],g,h,w,r,i,j,k,t;

int main()
{
	freopen("d.in.txt","r",stdin);
	freopen("d.out","w",stdout);
	scanf("%d",&t);
	for(g=0;g++<t;)
	{
		memset(b,0,sizeof(b));
		scanf("%d%d%d",&h,&w,&r);
		for(i=0;i<r;i++)
		{
			scanf("%d%d",&j,&k);
			b[j][k]=1;
		}
		memset(a,0,sizeof(a));
		a[1][1]=1;
		for(i=2;i<=h;i++)
			for(j=2;j<=w;j++)
				if(!b[i][j])a[i][j]=(a[i-1][j-2]+a[i-2][j-1])%10007;
		printf("Case #%d: %d\n",g,a[h][w]);
	}
	return 0;
}