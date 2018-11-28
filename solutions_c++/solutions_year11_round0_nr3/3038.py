#include<cassert>
#include<set>
#include<math.h>
#include<stack>
#include<limits.h>
#include<map>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<utility>
#include<algorithm>
#define REP(i,n) for(i=0;i<n;i++)
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n) 
#define sd(n) scanf("%lf",&n)
#define pll(n) printf("%l64d",n) 
#define ss(str) scanf("%s",str)
#define sf(n) scanf("%lf",&n)
#define pb push_back
#define LL long long int 
#define pi pair<int,int> 
#define fi first
#define se second
#define FOR(i,a,b) for(i = a ; i < b ; i++ )
using namespace std ;
int main(int argc, char *argv[])
{
 int i ;
 int j ;
 int t ;
 si(t);
 int d = 0 ;
 while( t -- > 0 ) 
 {
  d++;
  int n ;
  si(n);
  bool flag = false ;
  vector<int> seq ;
  REP(i,n)
  {
   seq.pb(0);
   si(seq[i]);
  }
  int ansMax = 0 ;
  REP(i,(1<<n))
  {
   if( i == 0 ) continue ;
   int tempA = 0 ;
   int tempB = 0 ;
   int tempBc = 0 ;
   for( j = 0 ; j < n ; j ++ )
   {
    if( (( i >> j ) & 1 ) == 1 ) 
    {
     tempA = tempA ^ seq[j];
    }
    else
    {
     tempBc = tempBc ^ seq[j] ;
     tempB = tempB + seq[j];
    }
   }
   //printf("%d %d\n",tempA, tempB);
   if( tempA == tempBc ) 
   {
    flag = true ;
    ansMax = max(ansMax, tempB );
   }
  }
  printf("Case #%d: ",d);
  if( flag ) 
   printf("%d\n",ansMax ) ;
  else
   printf("NO\n");
 }
}
