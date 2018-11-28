#include  "iostream" 
#include  "string.h"
#include  "sstream"
#include  "cstdio"

using namespace std;

int main()
{	

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small.out", "w", stdout);

	int ca;
	cin>>ca;
	for(int i=1;i<=ca;i++)
	{
		long long  k,n,mod;
		cin>>n>>k;
		cout<<"Case #"<<i<<": ";
		mod=(1LL<<n);
		if(k==0)
		{
			cout<<"OFF"<<endl;
		}
		else
		{
			if((k+1)%mod==0)
				cout<<"ON"<<endl;
			else
				cout<<"OFF"<<endl;
		}
	}
	return 0;
}