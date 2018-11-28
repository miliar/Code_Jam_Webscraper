#include<iostream>
#include<cstring>
#include<vector>
using namespace std;

int dx[]={-1,0,0,1},dy[]={0,-1,1,0};

typedef struct
{
	int x,y;
}
pt;
typedef struct
{
	pt son;
	vector<pt> f;
}
ad;
int map[110][110];
ad a[110][110];
bool v[110][110];
int h,w;
char ans[110][110];

void dfs(int x,int y,char c)
{
	int i,tx,ty;
	if(v[x][y]) return ;
    ans[x][y]=c;
	v[x][y]=true;
	if(a[x][y].son.x!=-1)
	dfs(a[x][y].son.x,a[x][y].son.y,c);
	for(i=0;i<a[x][y].f.size();i++)
	{
		tx=a[x][y].f[i].x;
		ty=a[x][y].f[i].y;
		dfs(tx,ty,c);
	}
}


int main()
{
	int t,i,j,k,m,tx,ty;
	freopen("B-large.in","r",stdin);
	freopen("b-l.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&h,&w);
		for(j=0;j<h;j++)
			for(k=0;k<w;k++) scanf("%d",&map[j][k]);
		int s=0;
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
			{
				a[j][k].son.x=-1;
				a[j][k].son.y=-1;
				a[j][k].f.clear();
			}
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
			{
				int temp=map[j][k];
				int x,y;
				for(m=0;m<4;m++)
				{
					tx=j+dx[m];
					ty=k+dy[m];
					if(tx>=0&&tx<h&&ty>=0&&ty<w)
					{
						if(map[tx][ty]<temp)
						{
							temp=map[tx][ty];
							x=tx;
							y=ty;
						}
					}

				}
				if(temp<map[j][k])
				{
					a[j][k].son.x=x;
					a[j][k].son.y=y;
					pt tt;
					tt.x=j;
					tt.y=k;
					a[x][y].f.push_back(tt);
				}
			}
   memset(v,false,sizeof(v));
   char c='a';
   for(j=0;j<h;j++)
	   for(k=0;k<w;k++)
		   if(!v[j][k])
		   {
			   dfs(j,k,c);
			   c++;
		   }
	   printf("Case #%d:\n",i);
	   for(j=0;j<h;j++)
	   {
		   printf("%c",ans[j][0]);
		   for(k=1;k<w;k++) printf(" %c",ans[j][k]);
		   printf("\n");
	   }
	}
	return 0;
}




