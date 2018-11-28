#include<iostream>
#include<string.h>
#include<cstdio>
using namespace std;

char a[100][100] ;
double wp[100] ; 
double wp1[100] ;
double owp[100] ;
double oowp[100] ;
int main()
{
 	freopen( "A.in" , "r" , stdin);
 	freopen( "A.out" , "w" , stdout);
  int T ; 
  int N ; 		
	 
  cin >> T ; 
  for( int i = 0 ; i < T ; ++ i )
  {
   cin >> N ; 
   for( int j = 0 ; j < N ; ++ j )
    for( int k = 0 ; k < N ; ++ k )
	cin >> a[j][k] ;  	   
   
   for( int j = 0 ; j < N ; ++ j )
   {
	  double win ;
	  int cont ;
	  win = 0 ; cont = 0 ;
	  wp[j] = 0 ;
	  for( int k = 0 ; k < N ; ++ k )
	  {
           if( a[j][k] != '.' ) cont ++ ; 
	  	   if( a[j][k] == '1' ) win ++ ;
      }
	  wp[j] = win / cont ;	   
   }
   
   for( int j = 0 ; j < N ; ++ j )
   {
	 	owp[j] = 0 ; 
   		int cont = 0 ;
   		for( int k = 0 ; k < N ; ++ k )
   		if( a[j][k] != '.' )
   		{
	 	 cont ++ ;
   	  	 double temp = 0 ; int contd = 0 ;
		 for( int m = 0  ; m < N ; ++ m )
		 {
		 if( a[k][m] != '.' && m != j )  contd ++ ; 
		 if( a[k][m] == '1' && m != j )  temp ++ ;
		 }
		 temp /= contd ;
		 owp[j] += temp ; 				   
		 }
		 owp[j] /= cont ;
   }
   for( int j = 0 ; j < N ; ++ j )
   {
   		oowp[j] = 0 ;
		int cont = 0 ;
		for( int k = 0 ; k < N ; ++ k )
		if( a[j][k] != '.' ) { oowp[j] += owp[k] ; cont ++ ; }		
		oowp[j] /= cont ;   
   }
   cout << "Case #" << i + 1 << ":" << endl ;
   for( int j = 0 ; j < N; ++ j )
   printf("%.12lf\n", 0.25 * wp[j] + 0.5 * owp[j] + 0.25 * oowp[j]);
  }	 
	 
  return 0 ;	 
}
