#include"iostream"
#define INF 10010

using namespace std;

int h,w;
int atti[110][110];
int p[10010];
char visited[10010];

int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

int fd(int v)
{
	if(p[v]!=v)
		p[v]=fd(p[v]);
	return p[v];
}

void init()
{
	scanf("%d%d",&h,&w);
	int i,j;
	for(i=1;i<=h;i++)
	{
		for(j=1;j<=w;j++)
		{
			scanf("%d",atti[i]+j);
			p[(i-1)*w+j]=(i-1)*w+j;
		}
	}
	memset(visited,0,sizeof(visited));
}

bool ok(int x,int y)
{
	return x>0 && x<=h && y>0 && y<=w;
}

void work()
{
	static int cas=1;
	int i,j;
	int tx,ty,x,y;
	for(i=1;i<=h;i++)
	{
		for(j=1;j<=w;j++)
		{
			int min=atti[i][j];
			int k;
			for(k=0;k<4;k++)
			{
				x=i+move[k][0];
				y=j+move[k][1];
				if(ok(x,y) && atti[x][y]<min)
				{
					tx=x,ty=y;
					min=atti[x][y];
				}
			}
			if(min<atti[i][j])
			{
				p[fd((i-1)*w+j)]=fd((tx-1)*w+ty);
			}
		}
	}
	printf("Case #%d:\n",cas++);
	char ch='a';
	for(i=1;i<=h;i++)
	{
		for(j=1;j<=w;j++)
		{
			if(!visited[fd((i-1)*w+j)])
			{
				visited[fd((i-1)*w+j)]=ch++;
			}
			putchar(visited[fd((i-1)*w+j)]);
			if(j<w)
				putchar(' ');
			else
				putchar(10);
		}
	}
}


int main()
{
//	freopen("2.in","r",stdin);
//	freopen("2.out","w",stdout);
	int t;
	scanf("%d",&t);
	while(t--)
	{
		init();
		work();
	}
	return 0;
}