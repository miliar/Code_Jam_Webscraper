
#include <stdio.h>
#include <string.h>

int a[100][100];
int c[100][100];
int d[100][100];

int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
int n,m;

void print()
{
	return;
	int i,j;
	for (i=0;i<n;i++)
	{
		for (j=0;j<m;j++)
		{
			if (j) printf(" ");
			printf("%d",c[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

int get_dir(int x,int y,int lf)
{
	int i,x2,y2;
	int an=-1;
	int high=a[x][y];
	for (i=0;i<4;i++)
	{
		x2=x+dir[i][0];
		y2=y+dir[i][1];
		if (x2>=0 && y2>=0 && x2<n && y2<m)
		{
			if (a[x2][y2]<high)
			{
				high=a[x2][y2];
				an=i;
			}
			else 
			if (1==0)
			//if (a[x2][y2]==high && i==lf)
			{
				high=a[x2][y2];
				an=i;
			}
		}
	}
	return an;
}

void paint(int x,int y,int color)
{
	int i,x2,y2;
	int orc=c[x][y];
	c[x][y]=color;
	for (i=0;i<4;i++)
	{
		x2=x+dir[i][0];
		y2=y+dir[i][1];
		if (x2>=0 && y2>=0 && x2<n && y2<m)
		{
			if (c[x2][y2]==orc)
			{
				paint(x2,y2,color);
			}
		}
	}
}

void go(int x,int y,int lf)
{
	int f;
	do
	{
		f=get_dir(x,y,lf);
		if (f==-1)
		{
			return;
		}
		int x2=x+dir[f][0];
		int y2=y+dir[f][1];
		if (c[x2][y2]==0)
		{
			c[x2][y2]=c[x][y];
		}
		else
		{
			int orc=c[x2][y2];
			int i,j;
			for (i=0;i<n;i++)
			{
				for (j=0;j<m;j++)
				{
					if (c[i][j]==orc)
					{
						c[i][j]=c[x][y];
					}
				}
			}
//			paint(x2,y2,c[x][y]);
		}
		print();
//		go(x2,y2,f);
		lf=f;
		x=x2;y=y2;
	}
	while (1==1);
	
}

int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("B.out","w",stdout);

	int T;
	int tt;
	scanf("%d",&T);

	int i,j,k,l;
	int color;
	int finish;
	int f;
	
	for (tt=1;tt<=T;tt++ )
	{
		memset(c,0,sizeof(c));
		memset(d,0,sizeof(d));

		scanf("%d %d",&n,&m);
		int max=0;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				scanf("%d",&a[i][j]);
				if (a[i][j]>max) max=a[i][j];
			}
		}
		
		color=0;
		finish=0;
		int h;

		for (h=max;h>=0;h--)
		{
			for (i=0;i<n;i++)
			{
				for (j=0;j<m;j++)
				{
					if (a[i][j]==h && c[i][j]==0)
					{
						color++;
						c[i][j]=color;
						go(i,j,-1);
						print();
					}
				}
			}
		}

		memset(d,0,sizeof(d));
		int cc=0;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if (d[i][j]==0)
				{
					cc++;
					for (k=0;k<n;k++)
					{
						for (l=0;l<m;l++)
						{
							if (c[k][l]==c[i][j])
							{
								d[k][l]=cc;
							}
						}
					}
				}
			}
		}
		
		printf("Case #%d:\n",tt);
		print();
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if (j) printf(" ");
				printf("%c",d[i][j]+'a'-1);
			}
			printf("\n");
		}
	}

	return 0;
}
