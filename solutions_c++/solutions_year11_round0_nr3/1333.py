#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

typedef long long int64;
int n,ca,num;

int main()
{
  freopen("C.in","r",stdin);
  //freopen("C.out","w",stdout);
	cin>>ca;
	for (int i=1; i<=ca; i++)
	{
		cout<<"Case #"<<i<<": ";
		int ret=0, MIN=100000000;
		int64 sum=0;
		cin>>n;
		for (int j=1; j<=n; j++)
		{
			cin>>num;
			MIN=min(MIN,num);
			ret^=num;
			sum+=num;
		}
		if (ret!=0) cout<<"NO"<<endl; else cout<<sum-MIN<<endl;
	}
}
