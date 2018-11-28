#include<iostream>
#include<stdio.h>

using namespace std;


int gcd( int i , int j )
{
  if( j == 0 ) return i ;
  return gcd( j , i % j ) ;
}


int main()
{
 	freopen("A.in" , "r" , stdin ) ;
 	freopen("A.out" , "w" , stdout ) ; 
  bool flag = false ;
  int T ; 
  cin >> T ; 
  for( int i = 0 ; i < T ; ++ i ) 
    {
      int N , Pd , Pg ; 
      char c ;
	  int flag = 0 ; N = 0 ;
	  c = getchar() ;
	  while( c > '9' || c < '0' ) c= getchar() ;
      while( flag <= 3 && c != ' ' )
	   {  N = N * 10 + c - '0' ; c = getchar() ; flag ++;}
      while( c != ' ' ) c = getchar() ;
      cin >> Pd >> Pg ;
      if( Pd != 0 && Pg == 0 || Pd != 100 && Pg == 100 )
	  	  { cout << "Case #"<<i+1<<":" << " Broken" << endl ; continue; }
      int gcdd = gcd( 100 , Pd  ) ;
      int gcdg = gcd( 100 , Pg  ) ;
      
      int incrd = Pd / gcdd ; int mud = 100 / gcdd ;
      int incrg = Pg / gcdg ; int mug = 100 / gcdg ;
      cout << "Case #"<<i+1<<":" << " " ;
      if( N < mud ) cout << "Broken" << endl ;
      else cout << "Possible" << endl ;
    }
  return 0;
}
