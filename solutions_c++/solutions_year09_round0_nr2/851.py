#include<cstdio>
#include<memory>
#include<algorithm>
using namespace std;

int h,i,j,k,n,m,t,a[102][102],b[10404],c[102][102],x,y,z,d[16384];

bool cmp(int i,int j)
{
	return a[i>>7][i&127]<a[j>>7][j&127];
}

int main()
{
	freopen("d:\\b.in","r",stdin);
	freopen("d:\\b.out","w",stdout);
	scanf("%d",&t);
	for(h=1;h<=t;h++)
	{
		memset(a,1,sizeof(a));
		scanf("%d%d",&n,&m);
		k=0;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				scanf("%d",&a[i][j]);
				b[k++]=(i<<7)|j;
			}
		sort(b,b+k,cmp);
		for(i=0;i<k;i++)
		{
			x=b[i]>>7;y=b[i]&127;
			c[x][y]=b[i];
			z=a[x][y];
			if(a[x-1][y]<z)
			{
				z=a[x-1][y];
				c[x][y]=c[x-1][y];
			}
			if(a[x][y-1]<z)
			{
				z=a[x][y-1];
				c[x][y]=c[x][y-1];
			}
			if(a[x][y+1]<z)
			{
				z=a[x][y+1];
				c[x][y]=c[x][y+1];
			}
			if(a[x+1][y]<z)
			{
				z=a[x+1][y];
				c[x][y]=c[x+1][y];
			}
		}
		memset(d,0,sizeof(d));
		printf("Case #%d:\n",h);
		k=97;
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
			{
				if(!d[c[i][j]])d[c[i][j]]=k++;
				printf("%c",d[c[i][j]]);
				if(j<m)printf(" ");
				else puts("");
			}
	}
	return 0;
}