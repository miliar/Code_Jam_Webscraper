#include <iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;

	for(int i = 0; i < t; ++i)
	{
		unsigned int n, k;
		cin>>n>>k;

		if((k % (1<<n))==((1<<n) - 1))
			cout<<"Case #"<<i+1<<": ON"<<endl;
		else
			cout<<"Case #"<<i+1<<": OFF"<<endl;
	}
	return 0;
}