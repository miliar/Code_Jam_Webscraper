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
string itoa( int x ){
   if( x == 0 ) return "0" ;
   char str[ 100 ] ;
   sprintf(str, "%d",x);
   return string(str);
}
bool check( int n, int m ){
   string source = itoa(n);
   for( int i = 0 ; i < source.size() ; i++ ){
      int val = 0 ;
      for( int j = 0 ; j < source.size() ; j++ ){
	 val = val * 10 + source[ (i+j)%(int)source.size()]-'0';
      }
      if( val == m ) return true ;
   }  
   return false ;
}
int M[ 2000001 ] ;
int main(int argc, char *argv[])
{
   int t ;
   si(t);
   int cs = 0 ;
   int lp = 0 ;
   while(t--){
      cs++;
      int a, b ;
      si(a);
      si(b);
      int count = 0 ;
      for( int n = a ; n <= b ; n++ ){
	 string source = itoa(n);
	 lp++;
	 for( int i = 0 ; i < source.size() ; i++ ){
	    int val = 0 ;
	    for( int j = 0 ; j < source.size() ; j++ ){
	       val = val * 10 + source[ (i+j)%(int)source.size()]-'0';
	    }
	    if( val >= a && val <= b && val > n &&M[ val ] != lp ){
	       M[ val ] = lp ;
	       count ++ ;
	    }

	 }
      }
      printf("Case #%d: %d\n",cs, count);
   }
   return 0 ;
}
