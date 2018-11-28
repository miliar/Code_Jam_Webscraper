
#include<iostream>
using namespace std;

bool play( int nbits,  long inputTimes);

long 
GetSquare( int n)
{
	 long sqr = 1;
	while(n--)
	{
	  sqr*=2;
	}
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
	if(n <= 0 || k <= 0 || run(n, k)== false)
		cout<<"OFF";
	else
		cout<<"ON";
	cout<<endl;
	i++;
 }
  
 return 0;
}

bool run( int n,  long k)
{
	long s;
	// the var "s" represents the number (or when all gadgets ON) when light will be ON
	s =	GetSquare(n) - 1;
	if( k < s)
		return false; //OFF STATE
	else if( k == s)
		return true; //ON State
	else
	{
	   // run thru loop when liht will b ON
	   // here s represents when LIGHT on
	   while( k > s)
		   k = k - ( s + 1);
	   

	   if( k == s)
		   return true; // ON State
	   else
		   return false; // Off State
	}
}