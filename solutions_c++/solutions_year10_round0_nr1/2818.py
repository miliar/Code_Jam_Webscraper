#include<iostream>

using namespace std;

int main()
{
 	 int t;
 	 cin>>t;
 	 
 	 for(int i = 1; i <= t; i++)
 	 {
	  		 int n;
	  		 cin>>n;
	  		 
	  		 int k;
	  		 cin>>k;
	  		 
	  		 int min = (1<<n) - 1;
	  		 
	  		 if( k < min)
	  		 	 cout<<"Case #"<<i<<": OFF\n";
	  		 else if( k == min)
	  		 	 cout<<"Case #"<<i<<": ON\n";
	  		 else 
	  		 {
			  	 k = k - min;
			  	 //if(k & (k-1))
			  	 if(k % (min + 1) != 0)
			  	 	  cout<<"Case #"<<i<<": OFF\n";
  	 	  		 else
					  cout<<"Case #"<<i<<": ON\n";  
			 }
	 }	  		 
	 
	 return 0;
}
