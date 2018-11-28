#include <iostream>
using namespace std ;

int cases = 1 ;
int N, P, K, L ;
int cha[2001] ;

int main( void )
{
  freopen( "in1-l", "r", stdin ) ;
  freopen( "out1-l", "w", stdout ) ;

  cin >> N ;
  while ( N-- ){
    cout << "Case #" << cases++ << ": " ;
    cin >> P >> K >> L ;
    long long re = 0 ;
    for ( int i = 0 ; i < L ; ++i )  cin >> cha[i] ;
    bool used[1001] ;
    int pos = 1, num = 0 ;
    memset( used, 0, sizeof(used) ) ;
    for ( int i = 0 ; i < L ; ++i ){
      int max = -1 ;
      int ptr = 0 ;
      for ( int j = 0 ; j < L ; ++j ){
	if ( !used[j] && max < cha[j] ){
	  max = cha[j] ;
	  ptr = j ;
	}
      }
      used[ptr] = true ;
      ++num ;
      if ( num > K ){
	num = 1 ;
	++pos ;
      }
      //cout << cha[ptr] << " " << pos << endl ;
      re += (long long)(cha[ptr])*pos ;
    }
    cout << re << endl ;
  }

  return 0 ;
}
