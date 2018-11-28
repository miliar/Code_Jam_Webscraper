#include<iostream>
using namespace std ;
#define MAXN 102
int ct,n,m,vis[MAXN][MAXN] ;
int in[MAXN][MAXN] ;

typedef pair<int,int> P ;
int dx[] = {-1,0,0,1} ;
int dy[] = {0,-1,1,0} ;

int flow(int x,int y)
{
 int ret = (int)1e9,k = -1 ;
 for(int i=0;i<4;i++)
 {
  int xx = x + dx[i] ;
  int yy = y + dy[i] ;
  if(xx < 0 || xx >= n || yy < 0 || yy >= m) continue ;
  if(in[xx][yy] >= in[x][y]) continue ;
  if(ret > in[xx][yy]) ret = in[xx][yy],k = i ;
 }
 return k ;
}

int dfs(int x,int y)
{
 if(vis[x][y] != -1) return vis[x][y] ;
 int d = flow(x,y) ;
 if(d == -1) return vis[x][y] = ct ++ ;
 return vis[x][y] = dfs(x+dx[d],y+dy[d]) ;
}

main()
{
 int i,j,k,runs ;
 
 freopen("in.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%d%d",&n,&m) ;
  for(i=0;i<n;i++)
   for(j=0;j<m;j++)
   scanf("%d",&in[i][j]) ;
  memset(vis,255,sizeof vis) ;
  ct = 0 ;
  
  for(i=0;i<n;i++)
   for(j=0;j<m;j++)
    if(vis[i][j] == -1)
     dfs(i,j) ;
  printf("Case #%d:\n",t) ;
  for(i=0;i<n;i++,printf("\n"))
   for(j=0;j<m;j++)
   {
    if(j) printf(" ") ;
    printf("%c",vis[i][j] + 'a') ;
   }
 }
// while(1) ;
}
