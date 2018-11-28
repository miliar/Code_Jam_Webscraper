#include<stdio.h>
#include<string.h>
const int mxn =101*101;
int p[mxn]={0},rank[mxn]={0};
int pile;
bool flag[101][101];
char ans[101*101];
int mp[101][101];
int H,W;
char C;

void init()
{
	memset(p,0,sizeof(p));
	memset(rank,0,sizeof(rank));
	memset(flag,0,sizeof(flag));
	memset(ans,0,sizeof(ans));
	pile = 0;
}
void makeset(int x)
{
	rank[x]=0;
	p[x]=x;
	pile++;
}
int findset(int x)
{
	int px=x,i;
	while (px!=p[px]) px=p[px]; 
	while (x!=px)
	{
		i=p[x];
		p[x]=px;
		x=i;
	}
	return px;
}

void unionset (int x , int y)
{
	x = findset(x);
	y = findset(y);
	if (x!=y)
	{
		pile--;
		if( rank[x] > rank[y]) p[y]=x;
		else
		{
			p[x]=y;
			if( rank[x]==rank[y]) rank[y]++;
		}
	}
}

void handle(int x,int y)
{
	int h = x*W+y+1;
	int f= findset(h);
	if (ans[f])
		ans[h] = ans[f];
	else
	{
		ans[h] = C++;
		ans[f] = ans[h];
	}
}

void solve(int x,int y)
{
	int dir[4][2] ={-1,0,0,-1,0,1,1,0};
	while(1)
	{
		flag[x][y] = 1;
		int minV = mp[x][y];
		int minD = -1;
		for (int i=0;i<4;i++)
		{
			int X = x+dir[i][0];
			int Y = y+dir[i][1];
			if (X>=0 && X<H && Y>=0 && Y<W)
			{
				if (mp[X][Y]<minV)
				{
					minV = mp[X][Y];
					minD = i;
				}
			}
		}
		if (minD>=0)
		{
			int X = x+dir[minD][0];
			int Y = y+dir[minD][1];
			int p1 = x*W+y+1;
			int p2 = X*W+Y+1;
			unionset(p1,p2);
			x = X;
			y = Y;
		}else break;
	}
}

int main()
{
	int T;
	
//	freopen("R:\\in2.txt","r",stdin);
//	freopen("R:\\out2.txt","w",stdout);
	scanf("%d",&T);
	for(int I=0;I<T;I++)
	{
		C='a';
		scanf("%d %d",&H,&W);
		init();
		for (int i=0;i<H;i++)
			for (int j=0;j<W;j++)
			{
				scanf("%d",&mp[i][j]);
				makeset(i*W+j+1);
			}
		for (int i=0;i<H;i++)
			for (int j=0;j<W;j++)
			{
				if (!flag[i][j]) solve(i,j);
			}

		for (int i=0;i<H;i++)
			for (int j=0;j<W;j++)
			{
				handle(i,j);
			}
			printf("Case #%d:\n",I+1);
			for (int i=0;i<H;i++)
				for (int j=0;j<W;j++)
				{
					if (j)
						putchar(' ');
					putchar(ans[i*W+j+1]);
					if (j==W-1)
						putchar('\n');
				}
	}
	return 0;
}
