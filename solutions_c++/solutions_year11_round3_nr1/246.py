#include<stdio.h>
#include<cstring>
using namespace std;
int T,r,c,p;
char g[51][51];
inline bool check()
{
  int i,j,k;
  for(i=1;i<=r;i++)
    for(j=1;j<=c;j++)
      if(g[i][j]=='#'){
        if(j==c || i==r) return false;
        if( !(g[i][j+1]=='#' && g[i+1][j]=='#' && g[i+1][j+1]=='#') )
          return false;
        g[i][j]='/';g[i][j+1]='\\';g[i+1][j]='\\';g[i+1][j+1]='/';
      }
  return true;
}
int main()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
  int i,j,k;
  scanf("%d",&T);
  for(p=1;p<=T;p++){
    scanf("%d%d",&r,&c);
    for(i=1;i<=r;i++){
      scanf("\n");
      for(j=1;j<=c;j++)
        scanf("%c",&g[i][j]);
    }
    printf("Case #%d:\n",p);
    if(check()){
      for(i=1;i<=r;i++){
        for(j=1;j<=c;j++)
          printf("%c",g[i][j]);
        printf("\n");}
    }
    else 
      printf("Impossible\n");
  }
  scanf("%d",&T);
  return 0;
}
        
