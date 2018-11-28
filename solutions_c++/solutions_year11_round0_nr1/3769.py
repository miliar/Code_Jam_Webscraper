#include<iostream>
#include<cmath>
using namespace std;

int main()
{
//	freopen("a.txt" , "w" , stdout) ;
//	freopen("b.in" , "r" , stdin) ;
  	int T ; 
  	int N , p ;
  	char r ;
  	int time_o , time_b , ans_o , ans_b ;
	cin >> T ; 
	for( int flag = 0 ; flag < T ; )
	{
	 cin >> N ; 
	 int cont = 0 ; 
	 time_o = 0 ; time_b = 0 ; ans_o = 1 ; ans_b = 1 ; 
	 for( int i = 0 ; i < N ; ++ i ) 	 
	 {
	  	cin >> r >> p ; 
		if( r == 'O' )   
		{
		int temp = abs(p-ans_o)+1 ;
		ans_o = p ;
		time_o += temp ;	 	
		if( time_o <= time_b ) time_o = time_b + 1 ;	 
	    }	
	    else
	    {
		int temp = abs(p-ans_b)+1;
		ans_b = p ;
		time_b += temp ;
		if( time_b <= time_o ) time_b = time_o + 1 ; 	
	    }
	 }	  
	 cout << "Case #" << ++ flag  << ": " << max(time_b , time_o) << endl ; 		  
    } 
    return 0;
}
