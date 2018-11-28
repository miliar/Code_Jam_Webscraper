#include<iostream>
#include<cmath>
#include<string>
using namespace std;

char in1[40] , in2[40] , in3[40] ;
char op1[30] , op2[30] ;
char str[100] ;
int main()
{
   freopen("B.in" , "r" , stdin ) ;
   freopen("B.txt" , "w" , stdout ) ;
   int T ; 
   int C , D , N ;  int pot = 0 ;
   cin >> T ; 
   for( int flag = 0 ; flag < T ;)
   {
   	cin >> C ; char c1 , c2 , c3 ;
	for( int i = 0 ; i < C ; ++ i )	
	{
	 cin >> c1 >> c2 >> c3 ;
	 if( c1 > c2 ) swap( c1 , c2 ) ;
	 in1[i] = c1 ; in2[i] = c2 ; in3[i] = c3 ;  	 
    }	   
    cin >> D ; 
    for( int i = 0 ; i < D ; ++ i )
    {
	 cin >> c1 >> c2 ;
	 if( c1 > c2 ) swap(c1,c2) ;
	 op1[i] = c1 ; op2[i] = c2 ; 	 
    }
	cin >> N ; pot = 0 ;
	for( int i = 0 ; i < N ; ++ i )
	{
	 cin >> c1 ; str[pot] = c1 ; pot ++ ; 
	 if( pot <= 1 ) continue ;
	 
	 c1 = min( str[pot-1] , str[pot-2]) ;
	 c2 = max( str[pot-1] , str[pot-2]) ;	  	  
	 for( int i = 0 ; i < C ; ++ i )		
	 if( in1[i] == c1 && in2[i] == c2 ) 
	 {
	   str[pot-2] = in3[i] ; pot -- ;
	   goto label ; 	 
     }		
	 for( int i = 0 ; i < pot-1  ; ++ i ) 
	  for( int m = 0 ; m < D ; ++ m ) 
	  {
	  c1 = min( str[i] , str[pot-1]) ;
	  c2 = max( str[i] , str[pot-1]) ; 	   
	  if( c1 == op1[m] && c2 == op2[m] ) 
	  {pot = 0; goto label ; }
	  } 
	 label: ;      	 
    } 
	cout << "Case #"<< ++flag <<": [" ; 
	for( int i = 0 ; i < pot-1 ; ++ i ) cout << str[i] << ", ";
	if( pot-1>=0 )cout << str[pot-1]; cout << "]"<< endl ; 	   		   
   } 	
	 return 0;	 
}
