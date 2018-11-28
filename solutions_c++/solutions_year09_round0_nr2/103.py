#include<vector>
#include<cstdio>
#include<iostream>
#include<set>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>
#include<string>
#include<cmath>
#include<map>
#include<fstream>

#define all(c) c.begin(), c.end()
#define allr(c) c.rbegin(), c.rend()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define INF (int)1e9

using namespace std ;

int g[102][102] ;
int dto[102][102] ;
int out[102][102] ;

int H , W ;
int curb = 0 ;

int dx[4] = { -1,0,0,1 } ;
int dy[4] = { 0,-1,1,0 } ;

void dfs2(int x,int y,int col)
{
   if(x<0 || y<0 || x>=H || y>=W) return ;
   if(out[x][y] >= 0) return ;
   if(dto[x][y] != col) return ;
   out[x][y] = curb ;
   for(int i=0;i<4;++i) dfs2(x+dx[i],y+dy[i],col) ;
   return ;
}

int dfs(int x,int y)
{
   if(x<0 || y<0 || x>=H || y>=W) return -1 ;
   if(dto[x][y] >= 0) return dto[x][y] ;
   int minx = x ;
   int miny = y ;
   int minval = g[x][y] ;
   for(int i=0;i<4;++i)
   {
      int cx = x + dx[i] ;
      int cy = y + dy[i] ;
      if(cx<0 || cy<0 || cx>=H || cy>=W) continue ;
      if(g[cx][cy] < minval)
      {
         minx = cx ;
         miny = cy ;
         minval = g[cx][cy] ;
      }
   }
   if(minval == g[x][y]) return y + x*W ;
   return dfs(minx,miny) ;
}


int main()
{
   int T ;
   freopen("B-large.in","r",stdin) ;
   freopen("out.txt","w",stdout) ;
   scanf("%d",&T) ;
   for(int runs=1;runs<=T;++runs)
   {
      scanf("%d%d",&H,&W) ;
      for(int i=0;i<H;++i) for(int j=0;j<W;++j) scanf("%d",&g[i][j]) ;
      memset(dto,-1,sizeof dto) ;
      for(int i=0;i<H;++i) for(int j=0;j<W;++j) if(dto[i][j] == -1) dto[i][j] = dfs(i,j) ;
      memset(out,-1,sizeof out) ;
      curb = 0 ;
      for(int i=0;i<H;++i) for(int j=0;j<W;++j) if(out[i][j] == -1) { dfs2(i,j,dto[i][j]) ; ++curb ; }
      printf("Case #%d:\n",runs) ;
      
      for(int i=0;i<H;++i)
      {
         for(int j=0;j<W;++j)
         {
            if(j>0) printf(" ") ;
            printf("%c",(char)(out[i][j]+'a')) ;
         }
         printf("\n") ;
      }
   }
   return 0 ;
}
