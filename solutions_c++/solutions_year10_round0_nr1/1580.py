#include "iostream"
#include "math.h"
using namespace std;
int main(void) 
{
	unsigned long int n,k,t,i,temp;
	cin>>t;
	for (i = 1; i <= t; i++)
	{
		cin>>n;
		cin>>k;
		temp = pow(2,n);
		k=k%temp;
		temp--;
		if(k==temp)
			cout<<"Case #"<<i<<": ON\n";
		else
			cout<<"Case #"<<i<<": OFF\n";
	}
	return 0;
}
