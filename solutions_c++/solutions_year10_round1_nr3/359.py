#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

int win(int i , int j )
{
 double phi = ( 1 + sqrt(5.0) ) / 2;
 int val =  ceil( ( double ) i / phi );
 if( j < val )
   return 1;
 
 if( j >= val && j < val + i )
   return 0;
 
 return 1; 
}

int main()
{
  
 int t; 
  
 cin>>t;
 int num = t;
 while( t-- )
 {
  
  int a1 , a2 , b1 , b2 ;
  cin>>a1>>a2>>b1>>b2;
  long long count = 0;
  int cas = num - t;
  
  for(int i = a1 ; i <= a2 ; i++)
    for(int j = b1 ;  j <= b2 ; j++)
	if( win( i , j ) )
	  count++;
	
  cout<<"Case #"<<cas<<": "<<count<<endl;
  
 } 
  
  
 return 0; 
}