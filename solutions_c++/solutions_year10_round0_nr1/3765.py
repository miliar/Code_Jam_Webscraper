
#include<iostream>
using namespace std;

bool DoRun( int n,  long k);

 long 
GetSquare(  int n)
{
	long sqr = 1;
	while(n--)
		  sqr*=2;
	
	return sqr;
}

int main()
{
 int n,  testcases;
 long k;
   
 cin>>testcases;
 int i=1;
 while(i <= testcases)
 {
	cin>>n>>k;
	cout<<"Case #"<<i<<": ";
	if(n <= 0 || k <= 0 || DoRun(n, k)== false)
		cout<<"OFF";
	else
		cout<<"ON";
	cout<<endl;
	i++;
 }
  
 return 0;
}

bool DoRun( int n,  long k)
{
	 long s;
	s =	GetSquare(n) - 1;
	if( k < s)
		return false; //OFF STATE
	else if( k == s)
		return true; //ON State
	else
	{
	   while( k > s)
	   {
		   k = k - ( s + 1);
	   }

	   if( k == s)
		   return true; //ON
	   else
		   return false; //OFF
	}
}
