#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std ;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef  long long int lli ;
typedef long double ld ;

int
main ( )
{
  freopen ( "tt.in" , "r" , stdin ) ;
  freopen ( "ll.out" , "w" , stdout ) ;
  int test ;
  scanf ( "%d" , &test ) ;
  int array[2000] ;
  for ( int tt = 1 ; tt <= test ; tt ++ )
    {
      int number ;
      scanf ( "%d" , &number ) ;
      double ncp = 0 ;
      for ( int i = 0 ; i < number ; i ++ )
        {
          cin >> array[i] ;
          if ( i + 1 != array[i] )ncp ++ ;
        }
      printf ( "Case #%d: %6lf\n" , tt , ncp ) ;
    }
  return 0 ;
}
