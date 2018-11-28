
#include <iostream>

using namespace std;

int T;

int main()
{
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int n;
		cin>>n;
		double ans=n;
		for(int i=1;i<=n;i++)
		{
			int k;
			cin>>k;
			if(i==k)ans-=1;
		}
		cout<<"Case #"<<t<<": ";
		cout<<ans<<endl;
	}
}
