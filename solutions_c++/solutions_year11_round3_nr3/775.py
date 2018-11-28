#include <iostream>
using namespace std;
__int64 fre[10001];
__int64 gcd(__int64 a,__int64 b)
{
	if (b==0)
		return a;
	else return gcd(b,a%b);
}
int main()
{
	int t,n,l,h;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>n>>l>>h;
		int g;
		for (int j=0;j<n;j++)
		{
			cin>>fre[j];
		}
		bool flag=0;
		__int64 ans;
		for (int k=l;k<=h;k++)
		{
			bool can=1;
			for (int j=0;j<n;j++)
			{
				if (k%fre[j]==0||fre[j]%k==0)
				{
					;
				}
				else
				{
					can=0;
					break;
				}
			}
			if (can==1)
			{
				flag=1;
				ans=k;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if (flag==0)
			cout<<"NO"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}