#include <iostream>
#include <algorithm>
using namespace std;
long long gcd(long long a,long long b)
{
	if (a<b)
	{
		swap(a,b);
	}
	if (b==0)
	{
		return a;
	}
	else
	{
		return gcd(b,a%b);
	}	
}
int main()
{
	int tt;
	long long t[10],r[10];
	cin>>tt;
	for (int kk=1;kk<=tt;++kk)
	{
		printf("Case #%d: ",kk);
		int n;
		cin>>n;
		for (int i=1;i<=n;++i)
		{
			cin>>t[i];
		}
		sort(t+1,t+n+1);
		for (int i=2;i<=n;++i)
		{
			r[i-1]=t[i]-t[i-1];
		}
		long long l=r[1];
		for (int i=2;i<n;++i)
		{
			l=gcd(l,r[i]);
		}
		if (t[1]/l*l==t[1])
		{
			cout<<0<<endl;
		}
		else
		{
			cout<<(t[1]/l+1)*l-t[1]<<endl;
		}
	}	
	return 0;
}