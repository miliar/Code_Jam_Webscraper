#include <iostream>
using namespace std;
int main()
{
	long long t,n,k;
	int tt;
	cin>>tt;
	for (int i=1;i<=tt;++i)
	{
		printf("Case #%d: ",i);
		cin>>n>>k;
		t=long long(1)<<n;
		if (k%t==t-1)
		{
			cout<<"ON"<<endl;
		}
		else
		{
			cout<<"OFF"<<endl;
		}
	}
	return 0;
}