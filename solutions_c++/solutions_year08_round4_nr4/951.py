#include <iostream>
#include <algorithm>
using namespace std ;


int N, k ;
int re ;
int cas = 1 ;
char buf[1001] ;


int getG( int len, int *per )
{
  char tmp[len+1] ;
  for ( int i = 0 ; i < len ; ++i )  tmp[i] = buf[per[i%k]+i/k*k] ;

  int r = 1 ;
  char c = tmp[0] ;
  for ( int i = 1 ; i < len ; ){
    if ( c == tmp[i] ) ++i ;
    else {
      c = tmp[i] ;
      ++r ;
      ++i ;
    }
  }
  return r ;
}


int main( void )
{
  freopen( "in4-s.in", "r", stdin ) ;
  freopen( "out4-s.txt", "w", stdout ) ;

  cin >> N ;
  while (N--){
    cout << "Case #" << cas++ << ": " ;
    cin >> k ;
    scanf( "%s", buf ) ;
    int per[6] ;
    int len = strlen(buf) ;

    for ( int i = 0 ; i < k ; ++i )  per[i] = i ;
    re = getG( len, per ) ;

    while ( next_permutation( per, per+k ) ){
      int t = getG( len, per ) ;
      re = (re > t ? t : re) ;
    }
    cout << re << endl ;

  }

  return 0 ;
}
