#include<stdio.h>
#include<string.h>

int dp[100][100];
int map[100][100];
int num,n,h,w;
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int find(int x,int y)
{
    if(dp[x][y]!=-1) return dp[x][y];
    int i,j,k,xx,yy,x1,y1,o;
    o=0;
    for(i=0;i<4;i++)
    {
                    xx=x+dx[i];
                    yy=y+dy[i];
                    if(xx>=0&&xx<h&&yy>=0&&yy<w&&map[xx][yy]<map[x][y])
                    {
                                                                       if(o==0||map[xx][yy]<map[x1][y1])
                                                                       {
                                                                                                        o=1;
                                                                                                        x1=xx;
                                                                                                        y1=yy;
                                                                       }
                    }
    }
    if(o==0)
    return dp[x][y]=num++;
    else return dp[x][y]=find(x1,y1);
}
                                                
                    

int main()
{
    int i,j,k;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small.out","w",stdout);
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
                     scanf("%d%d",&h,&w);
                     for(j=0;j<h;j++)
                      for(k=0;k<w;k++)
                      scanf("%d",&map[j][k]);
                      memset(dp,-1,sizeof(dp));
                      num=0;
                      for(j=0;j<h;j++)
                       for(k=0;k<w;k++)
                       find(j,k);
                       printf("Case #%d:\n",i);
                      for(j=0;j<h;j++)
                        for(k=0;k<w;k++)
                          if(k==w-1) printf("%c\n",dp[j][k]+'a');
                          else printf("%c ",dp[j][k]+'a');
    }
    return 0;
}
                                                   
