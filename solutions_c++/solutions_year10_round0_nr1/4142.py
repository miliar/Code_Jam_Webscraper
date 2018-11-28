#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cmath>
using namespace std;
int main()
{
	int n, k;
	double p, t, q;
	
	cin>>t;
	
	int t1=t;
	while(t-- !=0)
	{
		cin>>n;
		cin>>k;
		
		p = (1<<n) -1;
		
		if (p == 0)
			cout<<"Case #"<<t1-t<<": OFF\n";
		else
		{
			
			int multiplicand = p+1;
			int multiplier= k>>n;
			
			int product = 0;
                       while ((multiplier))
		       {
			      if(multiplier&01)
			     
			      {
				      product = product + multiplicand;
			      }

			      multiplicand<<=1;
			      multiplier>>=1;
		       }
		       
		       q = k- (product);
			if(q == p)
				cout<<"Case #"<<t1-t<<": ON\n";
			else
				cout<<"Case #"<<t1-t<<": OFF\n";
		}
	}
return 0;
}
	
