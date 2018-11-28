#include<iostream>
using namespace std;
int p[10050][2];
int v,g[10050],c[10050],cn,ci;
int m,n,i,j;

int minx(int x,int y)
{
  if (x==-1) return y;
  if (y==-1) return x;
  if (x<y) return x;
  return y;
}

void dfs(int x)
{
  if (x>m) return;
  dfs(x*2);
  dfs(x*2+1);
  int tmp;
  if (g[x]) // AND
  {
    p[x][0]=minx(p[x*2][0],p[x*2+1][0]);
    if (p[x*2][1]!=-1 && p[x*2+1][1]!=-1) p[x][1]=p[x*2][1]+p[x*2+1][1];
    else p[x][1]=-1;
    if (c[x])
    {
      tmp=minx(p[x*2][1],p[x*2+1][1]);
      if (tmp!=-1)
      {
        tmp++;
        p[x][1]=minx(p[x][1],tmp);
      }
    }
  }
  else // OR
  {
    p[x][1]=minx(p[x*2][1],p[x*2+1][1]);
    if (p[x*2][0]!=-1 && p[x*2+1][0]!=-1) p[x][0]=p[x*2][0]+p[x*2+1][0];
    else p[x][0]=-1;
    if (c[x])
    {
      tmp=minx(p[x*2][0],p[x*2+1][0]);
      if (tmp!=-1)
      {
        tmp++;
        p[x][0]=minx(p[x][0],tmp);
      }
    }
  }
}

int main()
{
  freopen("a_large.out","w",stdout);
  scanf("%d",&cn);
  ci=0;
  while (cn--)
  {
    ci++;
    scanf("%d %d",&n,&v);
    m=n/2;
    for (i=1;i<=m;i++) scanf("%d %d",&g[i],&c[i]);
    for (i=m+1;i<=n;i++) 
    {
      scanf("%d",&j);
      p[i][j]=0;
      p[i][1-j]=-1;
    }
    dfs(1);
    printf("Case #%d: ",ci);
    if (p[1][v]==-1) printf("IMPOSSIBLE\n");
    else printf("%d\n",p[1][v]);
  }
  return 0;
}