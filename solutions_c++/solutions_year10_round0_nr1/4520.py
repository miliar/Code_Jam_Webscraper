#include <iostream>
#include <conio.h>

using namespace std;

bool isOn( bool set[] , int n )
{
 	 for( int i=0; i<n; i++ ) 
	 	  if( !set[i] ) return false;
	 	  
	 return true; 
}

//void print( bool set[] , int n )
//{
// 	 for( int i=0; i<n; i++ )
// 	 	  cout << set[i];
//	  cout << endl;
//}

int main()
{
 	freopen( "input.in" , "r", stdin); 
 	freopen( "output.txt" , "w", stdout); 
 	int t,n,k;
 	int pow=1;
 	bool set[30];
 	char* state[2]={ "ON" , "OFF" };
 	
 	cin >> t;
 	
 	for( int count=0; count<t; count++ )
 	{
	 	 cin >> n;
	 	 cin >> k;
	 	 pow=1;
	 	 for( int i=0; i<n; i++ ) set[i]=false;
		 
		 for( int i=0; i<k; i++ )
	  	 {
		  	  for( int p=0; p<pow; p++ ) set[p]=!set[p];
		  	  for( int p=0; p<n; p++ )
			  {
			   	   if( !set[p] || p==n-1 )	{
				   	   		   pow=p+1;
				   	   		   break;
  				   }
		   	  }
		   	  
	  	 }
//		 getch();
		 cout << "Case #" << count+1 << ": ";
	 	 if( isOn( set , n ) ) cout << state[0] << endl;
	 	 else cout << state[1] << endl;
	}
 	
// 	system("pause");
 	return 0;
 	
 	
 	
 	
 	
}
