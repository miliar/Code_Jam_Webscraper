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
 int t ;
 si(t);
 int l1 = 0 ;
 while( t -- > 0 ) 
 {
  l1++;
  int n ;
  int i ;
  si(n);
  int j ;
  vector< pi > x ;
  vector< pi > seqA ;
  vector< pi > seqB ;
  vector< int > dirX ;
  int pos ;
  char ch ;
  for( i = 0 ; i < n ; i++ )
  {
   scanf(" %c %d",&ch, &pos ); 
//   x.make_pair( ch , p ) ;
   if( ch == 'O' ) seqA.pb ( make_pair( pos, i ) ) ;
   else if( ch == 'B' ) seqB.pb ( make_pair( pos, i ) ) ;
  }
  int i1 = 0 ;
  int i2 = 0 ;
  int curA = 1 ;
  int curB = 1 ;
  int T = 0 ;
  while( i1 < seqA.size() || i2 < seqB.size()) 
  {
   if(i1 != seqA.size() && ( i2 == seqB.size() ||  seqA[i1].se < seqB[i2].se ))
   {
    int dist = abs( seqA[i1].fi - curA ) ;
    curA = seqA[i1].fi ;
    T = T + dist + 1 ;
    i1++;
    dist++;
    if( i2 < seqB.size())
    {
     int dist2 = abs( seqB[i2].fi - curB ) ;
     if( dist2 <= dist ) 
     {
      curB = seqB[i2].fi ;
     }
     else
     {
      if( seqB[i2].fi > curB ) 
      {
       curB = curB + dist ;
      }
      else
      {
       curB = curB - dist ;
      }
     }
    }
   }
   else
   {
    int dist = abs( seqB[i2].fi - curB ) ;
    curB = seqB[i2].fi ;
    T = T + dist + 1 ;
    i2++ ;
    dist++;
    if( i1 < seqA.size() ) 
    {
     int dist2 = abs( seqA[i1].fi - curA ) ;
     if( dist2 <= dist ) 
     {
      curA = seqA[i1].fi ;
     }
     else
     {
      if( seqA[ i1].fi > curA ) 
      {
       curA = curA + dist ;
      }
      else
      {
       curA = curA - dist ;
      }
     }
    }
   }
//   printf("A:%d B:%d T:%d\n",curA,curB,T);
  }
  printf("Case #%d: %d\n",l1,T);
 }
 return 0 ;
}
