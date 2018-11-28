#include<iostream>
using namespace std ;
#define MAXN 1002
#define MOD 10000
char in[MAXN],in2[25] = "welcome to code jam" ;
int n,m = 19 ;

int memo[MAXN][25] ;
int solve(int k1,int k2)
{
 if(in[k1] != in2[k2]) return 0 ;
 if(k2 == m-1) return 1 ;
 if(memo[k1][k2] != -1) return memo[k1][k2] ;
 int i,j,ret = 0 ;
 for(i=k1+1;i<n;i++)
 {
  ret += solve(i,k2+1) ;
  if(ret >= MOD) ret -= MOD ;
 }
 return memo[k1][k2] = ret ;
}

main()
{
 int i,j,k,runs ;
 freopen("in.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 scanf("%d\n",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  gets(in) ;
  n = strlen(in) ;
  memset(memo,255,sizeof memo) ;
  int ret = 0 ;
  for(i=0;i<n;i++)
  {
   ret += solve(i,0) ;
   if(ret >= MOD) ret -= MOD ;
  }
  printf("Case #%d: %04d\n",t,ret) ;
 }
// while(1) ;     
}
