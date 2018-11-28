#include<iostream>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<sstream>
using namespace std ;
#define MAXN 502
#define MOD 100003
int memo[MAXN][MAXN] ;
int ncr[MAXN][MAXN] ;
int solve(int k,int n)
{
 if(k == 0) return 1 ;
 if(n == 1) return k == 0 ? 1 : 0 ;
 if(memo[k][n] != -1) return memo[k][n] ;
 int i,j,ret = 0 ;
 for(i=0;i<=n-k-2 && i <= k;i++)
 {
  ret += (1LL*solve(k - i - 1,k+1)*ncr[n - k - 2][i])%MOD ;
 }
 ret %= MOD ;
 return memo[k][n] = ret ;
}

int main()
{
 int i,j,k,runs ;
 
 ncr[0][0] = 1 ;
 for(i=1;i<MAXN;i++)
 {
  ncr[i][0] = ncr[i][i] = 1 ;
  for(j=1;j<i;j++)
   ncr[i][j] = (ncr[i-1][j] + ncr[i-1][j-1])%MOD ;
 }
 
 memset(memo,255,sizeof memo) ;
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  cin >> k ;
  int ret = 0 ;
  for(i=0;i+1<k;i++) ret = (ret + solve(i,k))%MOD ;
  printf("Case #%d: %d\n",t,ret) ;
 }  
}
