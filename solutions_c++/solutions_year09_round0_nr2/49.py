#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int map[103][103];
int flow[103][103];
int ans[103][103];
int T,h,w;

void TBM(int x,int y,int l)
{
  if((flow[x][y]==1||flow[x-1][y]==4)&&(!ans[x-1][y]))
  {
    ans[x-1][y]=l;
    TBM(x-1,y,l);
  }
  if((flow[x][y]==2||flow[x][y-1]==3)&&(!ans[x][y-1]))
  {
    ans[x][y-1]=l;
    TBM(x,y-1,l);
  }
  if((flow[x][y]==3||flow[x][y+1]==2)&&(!ans[x][y+1]))
  {
    ans[x][y+1]=l;
    TBM(x,y+1,l);
  }
  if((flow[x][y]==4||flow[x+1][y]==1)&&(!ans[x+1][y]))
  {
    ans[x+1][y]=l;
    TBM(x+1,y,l);
  }
}

int main()
{
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout); 
  scanf("%d",&T);
  for(int i=1;i<=T;i++)
  {
    int now='a'-1;
    memset(map,-1,sizeof(map));
    memset(ans,0,sizeof(ans));
    scanf("%d%d",&h,&w);
    for(int j=1;j<=h;j++)
      for(int k=1;k<=w;k++)
	scanf("%d",&map[j][k]);
    for(int j=1;j<=h;j++)
      for(int k=1;k<=w;k++)
      {
	int MIN=map[j][k];
	if(map[j-1][k]!=-1&&map[j-1][k]<MIN)
	  MIN=map[j-1][k];
	if(map[j+1][k]!=-1&&map[j+1][k]<MIN)
	  MIN=map[j+1][k];
	if(map[j][k-1]!=-1&&map[j][k-1]<MIN)
	  MIN=map[j][k-1];
	if(map[j][k+1]!=-1&&map[j][k+1]<MIN)
	  MIN=map[j][k+1];
	if(map[j][k]==MIN)
	  flow[j][k]=0;
	else
	{
	  if(map[j-1][k]==MIN)
	  {
	    flow[j][k]=1;
	    continue;
	  }
	  if(map[j][k-1]==MIN)
	  {
	    flow[j][k]=2;
	    continue;
	  }
	  if(map[j][k+1]==MIN)
	  {
	    flow[j][k]=3;
	    continue;
	  }
	  flow[j][k]=4;
	}
      }
    for(int j=1;j<=h;j++)
      for(int k=1;k<=w;k++)
      {
	if(!ans[j][k])
	{
	  ans[j][k]=++now;
	  TBM(j,k,now);
	}
      }
    printf("Case #%d:\n",i);
    for(int j=1;j<=h;j++)
      for(int k=1;k<=w;k++)
      {
	if(k==w)
	  printf("%c\n",ans[j][k]);
	else
	  printf("%c ",ans[j][k]);
      }
  }
  return 0;
}


	

