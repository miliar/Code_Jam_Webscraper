#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<stack>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<set>
#include<bitset>

using namespace std ;
#define INF (int)1e9 
typedef pair<int,int> P ;
#define MAXN 100000

int n,v ; 
int gate[MAXN],change[MAXN],value[MAXN] ;
int memo[MAXN][2] ;

int solve(int k,int val)
{
 if(value[k] != -1) return value[k] == val?0:INF ;
 if(memo[k][val] != -1) return memo[k][val] ;
 
 int ret = INF ;
 if(gate[k] == 1)
 {
  if(val == 1) ret <?= solve(2*k,1) + solve(2*k+1,1) ;
  else ret <?= (solve(2*k,0) <? solve(2*k+1,0)) ;   
  
  if(change[k])
  {
   if(val == 1) ret <?= 1 + (solve(2*k,1) <? solve(2*k+1,1)) ;
   else ret <?= 1 + solve(2*k,0) + solve(2*k+1,0) ;
  }          
 }
 else
 {
  if(val == 1) ret <?= (solve(2*k,1) <? solve(2*k+1,1)) ;
  else ret <?= solve(2*k,0) + solve(2*k+1,0) ;
  if(change[k])
  {
   if(val == 1) ret <?= 1 + solve(2*k,1) + solve(2*k+1,1) ;
   else ret <?= 1 + (solve(2*k,0) + solve(2*k+1,0)) ;
  }          
 }
 return memo[k][val] = ret ;
}

main()
{
 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;

 int i,j,k,runs ;
 
 
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  cin >> n >> v ;
 
  memset(change,0,sizeof change) ;
  memset(gate,0,sizeof gate) ;
  memset(value,255,sizeof value)  ;
   
  for(i=1;i<=(n-1)/2;i++) cin >> gate[i] >> change[i] ;
  for(j=0;j<(n+1)/2;j++) cin >> value[i++] ; 
  
  memset(memo,255,sizeof memo) ;
  int ret = solve(1,v) ;
  if(ret > 10000000) printf("Case #%d: IMPOSSIBLE\n",t) ;
  else printf("Case #%d: %d\n",t,ret) ;
 }
// while(1) ;      
}
