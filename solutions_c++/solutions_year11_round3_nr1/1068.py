#include<iostream>
#include<string.h>
#include<cstdio>
using namespace std;

char a[50][50] ;

int main()
{
  freopen("A.in","r",stdin) ;
  freopen("A.out","w",stdout) ; 
  int T ; 
  cin >> T ;
  for( int flag = 0 ; flag < T ; ++ flag )
    {
      int R , C ; 
      cin >> R >> C ; 
      for( int i = 0 ; i < R ; ++ i )
        for( int j  = 0 ; j < C ; ++ j )
          cin >> a[i][j] ; 
      
      bool ok = true ;
      for( int i = 0 ; i < R && ok ; ++ i )
        for( int j  = 0 ; j < C ; ++ j )
          if( a[i][j] == '#' ) 
            {
              a[i][j] = '/' ;
              if( j+1 < C && a[i][j+1] == '#' ) a[i][j+1] = '\\' ;
              else { ok = false ; break ; }
              if( i+1 < R && a[i+1][j] == '#' ) a[i+1][j] = '\\' ;
              else { ok = false ; break ; }
              if( a[i+1][j+1] == '#' ) a[i+1][j+1] = '/' ;
              else { ok = false ; break ; }
            }
      cout <<"Case #"<<flag+1<<":"<< endl ;
      if( ok ) for( int i = 0 ; i < R ; ++ i ) 
                 {
                 for( int j = 0 ; j < C ; ++ j )
                   cout << a[i][j] ;
                 cout << endl ;
                 }
      else cout << "Impossible" << endl ;
    }



  return 0 ;
}
 
