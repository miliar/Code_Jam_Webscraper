#include <iostream>
using namespace std;

int main()
{
	long n,k,t;
	cin>>t;
	for (int i = 1;i<=t;i++)
	{
		cin>>n>>k;
		int cur = 1;
		for (int ii = 1;ii<=n;ii++)
		{
			cur= cur*2;
		}
		if (k % cur == cur-1)
		{
			cout<<"Case #"<<i<<": "<<"ON"<<endl;
		}
		else 
		{
			cout<<"Case #"<<i<<": "<<"OFF"<<endl;
		}

	}
	return 0;
}
