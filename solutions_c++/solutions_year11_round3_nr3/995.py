#include<iostream>
#include<string.h>
#include<cstdio>
using namespace std;

int a[101] ;
int result[10001] ;
int gcd( int i , int j )
{
  if( j == 0 ) return i ; 
  return gcd( j , i % j ) ;
}

int main()
{
  freopen("B.in" ,"r" , stdin );
  freopen("B.out" , "w" , stdout ) ;
  int T ; 
    cin >> T ;
  for( int flag = 0 ; flag < T ; ++ flag )
    {
      int N , L , H ; 
      cin >> N >> L >> H ; 
      for( int i  = 0 ;i < N ; ++ i )
        cin >> a[i] ;
      
      memset( result , 0 , sizeof(result) ) ;
      for( int i = 0 ;i < N ; ++ i )
        {
          int temp = a[i] ;
          for( int j = 1 ; j <= temp ; ++ j )
            if( temp % j == 0 ) { result[j] ++ ; }
          for( int j = 2 ; j * a[i] <= H ; ++ j )
            result[j*a[i]] ++ ;
        }
      int point = -1 ;
      for( int i = L ; i <=H ; ++ i )
        if( result[i] == N ) { point = i ; break ;}
      cout << "Case #" << flag + 1 << ": " ;
      if( point != -1 ) cout << point << endl ;
      else cout << "NO" << endl ;

    }


  return 0 ;
}
