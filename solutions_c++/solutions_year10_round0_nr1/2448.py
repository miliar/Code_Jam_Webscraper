#include <iostream>

using namespace std;


int main()
{
	int num_test;
	
	cin>>num_test;

	for(int i=0; i!=num_test; i++)
	{
		long int n;
		cin>>n;
	
		long int k;
		cin>>k;

		long int power=1;
		for(long int j=0; j!=n ;j++)
		power *= 2;

		
		cout<<"Case #"<<i+1<<": ";
		if( (k+1) % power == 0 )
		cout<<"ON";
		else
		cout<<"OFF";

		cout<<endl;
				
	}

		return 0;
}
