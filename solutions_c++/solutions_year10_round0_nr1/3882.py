
#include<iostream.h>

long long int power(int x);
int main()
{
    //cout<<power(30);
	int cases;
	cin>>cases;
	for(int cCases = 0;cCases<cases;cCases++)
	{
		cout<<"Case #"<<cCases+1<<": ";
		int n;
		long long int k;
		cin>>n>>k;
		long long int no = power(n);
		if(k%no == no-1) 
			cout<<"ON";
		else
		cout<<"OFF";

		if(cCases != cases -1 ) cout<<"\n";
		

	}
	return 0;
}

long long int power(int x)
{
	if(x==0) return 1;
	if(x%2==0)
	{
		long long int y = power(x/2);
		return (y*y);

	}
	else
	{
		long long int y = power(x/2);
			return (2*y*y);
   }

}
