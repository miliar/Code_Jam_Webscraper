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
#define pll(n) printf("%lld",n) 
#define ss(str) scanf("%s",str)
#define sf(n) scanf("%lf",&n)
#define pb push_back
#define LL long long int 
#define pi pair<int,int> 
#define fi first
#define se second
#define getBit(i,n) ((i>>n)&1)
#define FOR(i,a,b) for(int i = a ; i < b ; i++ )
using namespace std ;
int A[ 100001 ] ;
int main(int argc, char *argv[])
{
   int kases = 0 ;
   si( kases ) ;
   int numCases = 0 ;
   while( kases-- >  0 ){
      numCases++ ;
      //code goes here.	 	
      int n ;
      si(n);
      vector< pi > vi ;
      int d, l ;
      int L = 0 ;
      FOR(i,0,n){
	 si(d);
	 si(l);
	 vi.push_back( make_pair( d, l ) ) ;
	 A[i] = -1 ;
      }
      si( L ) ;
      bool flag = false ;
      queue< pair< int,int > > Q ;
      Q.push(make_pair( 0 ,vi[0].first ));	
      while ( !Q.empty()){
	int in = Q.front().first ;
        int md = Q.front().second ;
	if( vi[in].first + md >= L ){
	   flag = true ;
	   break ;
	}
	Q.pop();
	for( int j = in+ 1 ; j < n ; j++ ){
	   int jd = vi[j].first ;
	   int jl = vi[j].second ;
	   if(  md+vi[in].first >= jd ){
	        int val = min( jl, jd-vi[in].first ) ; 
		if( A[ j ] < val ){
		 Q.push(make_pair(j, min(jl,jd-vi[in].first)));
		 A[j] = val ;
		}
	   }
	}
      }
      if( flag ){
	printf("Case #%d: YES\n", numCases);
      }
      else{	
	printf("Case #%d: NO\n", numCases);
      }
   }
   return 0 ;
}
