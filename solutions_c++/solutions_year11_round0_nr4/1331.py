#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int n,m,ca,num;

int main()
{
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);
	cin>>ca;
	for (int i=1; i<=ca; i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>n; int ans=0;
		for (int j=1; j<=n; j++)
		{
			cin>>num;
			if (num!=j) ++ans;
		}
		cout<<ans<<".000000"<<endl;
	}
}
