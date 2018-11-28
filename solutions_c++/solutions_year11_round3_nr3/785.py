#include <iostream>
using namespace std;

int main()
{
	int t,n,l,h,i,j,k;
	int a[110];
	bool s;
	cin>>t;
	for(j=1;j<=t;j++)
	{
		cin>>n>>l>>h;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(k=l;k<=h;k++)
		{
			s=1;
			for(i=0;i<n;i++)
			{
				if(a[i]%k!=0 && k%a[i]!=0)
				{
					s=0;break;
				}
			}
			if(s) break;
		}
		if(s)
			cout<<"Case #"<<j<<": "<<k<<endl;
			else cout<<"Case #"<<j<<": "<<"NO"<<endl;
	}
}
