#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;

long long T,N,pD,pG;
long long gcd(long long a,long long b)
{
	return a?gcd(b%a,a):b;
}

int main()
{
	freopen("data.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int t;
	cin>>T;
	for(t=1;t<=T;++t)
	{
		cout<<"Case #"<<t<<": ";
		cin>>N>>pD>>pG;
		if(!pD && !pG)
		{
			cout<<"Possible"<<endl;
			continue;
		}
		else if(!pD && pG)
		{
			if(pG==100)
				cout<<"Broken"<<endl;
			else
				cout<<"Possible"<<endl;
			continue;
		}
		else if(pD && !pG)
		{
			cout<<"Broken"<<endl;
			continue;
		}
		long long n=100/gcd(pD,100);
		//cout<<n<<endl;
		if(n>N || (pD!=100 && pG==100)) cout<<"Broken"<<endl;
		else cout<<"Possible"<<endl;
	}

	return 0;
}
