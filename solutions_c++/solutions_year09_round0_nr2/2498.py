#include <cstdio>
#include <cstring>
char co[20000];
int fa[200000];
int a[120][120];
int i,j,k,s,t,n,m,tx,ty;
int I,T;
const int fx[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
bool ok(int x,int y)
{
	return (0<=x && x<n && 0<=y && y<m);
}
int fat(int x)
{
    if (fa[x]==x)
        return fa[x];
	return fa[x]=fat(fa[x]);
}

int comb(int x,int y)
{
	int t1,t2;
	t1=fat(x);
	t2=fat(y);
	fa[t1]=t2;
}
main()
{
	scanf("%d",&T);
	for (I=1;I<=T;++I)
	{
		printf("Case #%d:\n",I);
		scanf("%d%d",&n,&m);
		for (i=0;i<n;++i)
		    for (j=0;j<m;++j)
		    {
		        scanf("%d",&a[i][j]);
		        fa[i*m+j]=i*m+j;
			}
		for (i=0;i<n;++i)
		    for (j=0;j<m;++j)
		    {
				int ma=10000000,mx,my;
				for (k=0;k<4;++k)
				{
					tx=i+fx[k][0];
					ty=j+fx[k][1];
					if (ok(tx,ty) && a[tx][ty]<ma)
					{
						ma=a[tx][ty];
						mx=tx;
						my=ty;
					}
				}
				if (ma<a[i][j])
				{
					comb(i*m+j,mx*m+my);
				}
			}
		memset(co,0,sizeof co);
		char tmp='a';
		for (i=0;i<n;++i)
		{
		    for (j=0;j<m;++j)
		    {
		        if (co[fat(i*m+j)]==0)
					co[fat(i*m+j)]=tmp++;
				printf("%c ",co[fat(i*m+j)]);
			}
			printf("\n");
		}
	}
	return 0;
}
