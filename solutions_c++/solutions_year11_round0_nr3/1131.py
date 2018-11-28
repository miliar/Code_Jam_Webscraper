#include <iostream>

using namespace std;

int T;

int main()
{
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n,min=9999999,sum=0,x=0;
		cin>>n;
		while(n--)
		{
			int a;
			cin>>a;
			sum+=a;
			x^=a;
			if(min>a)min=a;
		}
		cout<<"Case #"<<t<<": ";
		if(x)cout<<"NO"<<endl;
		else cout<<sum-min<<endl;
	}
}
