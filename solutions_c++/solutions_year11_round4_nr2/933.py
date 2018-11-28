#include <iostream>
using namespace std;
int map[15][15];
char ch;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("outb.txt","w",stdout);
	int i,j,k,t,n,m,x,y,d,s,ok,maxx,co=1;
	scanf("%d",&t);
	while (t--)
	{
		maxx=-1;
		scanf("%d%d%d",&n,&m,&d);
		getchar();
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{	
				scanf("%c",&ch);
				map[i][j]=ch-'0'+d;
			}
			getchar();
		}
		for (i=0;i<n;i++)
			for (j=0;j<m;j++)
				for (k=1;k+i<=n&&k+j<=m;k++)
				{
					
					s=0;
					ok=1;
					if (k%2==1)
					{
						for (x=0;x<(k/2);x++)
							for (y=0;y<k;y++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s-=map[x+i][y+j]*(k/2-x);
							}
						for (x=(k+1)/2;x<k;x++)
							for (y=0;y<k;y++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s+=map[x+i][y+j]*(x-k/2);
							}
					}
					else
					{
						for (x=0;x<(k/2);x++)
							for (y=0;y<k;y++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s-=map[x+i][y+j]*(k-x*2-1);
							}
						for (x=k/2;x<k;x++)
							for (y=0;y<k;y++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s+=map[x+i][y+j]*(x*2-k+1);
							}
					}
					if (0!=s)
						ok=0;
					s=0;
					if (k%2==1)
					{
						for (y=0;y<(k/2);y++)
							for (x=0;x<k;x++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s-=map[x+i][y+j]*(k/2-y);
							}
						for (y=(k+1)/2;y<k;y++)
							for (x=0;x<k;x++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s+=map[x+i][y+j]*(y-k/2);
							}
					}
					else
					{
						for (y=0;y<(k/2);y++)
							for (x=0;x<k;x++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s-=map[x+i][y+j]*(k-y*2-1);
							}
						for (y=k/2;y<k;y++)
							for (x=0;x<k;x++)
							{
								if (x==0&&y==0)
								continue;
							if (x==0&&y==k-1)
								continue;
							if (x==k-1&&y==k-1)
								continue;
							if (x==k-1&&y==0)
								continue;
								s+=map[x+i][y+j]*(y*2-k+1);
							}
					}
					if (0!=s)
						ok=0;
					if (ok==1&&maxx<k)
						maxx=k;
				}
		if (maxx<3)
			printf("Case #%d: IMPOSSIBLE\n",co++);
		else
		printf("Case #%d: %d\n",co++,maxx);
	}
	return 0;
}