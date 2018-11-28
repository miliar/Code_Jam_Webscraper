#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void solve()
{
	int n;
	cin>>n;
	int t;
	int bs=0;
	int s=0;
	int min=10000000;


	for(int i=0;i<n;i++)
	{
		cin>>t;
		if(t<min)
			min=t;
		bs=bs^t;
		s+=t;
	}
	if(bs==0)
	{
		cout<<s-min;
	}
	else
	{
		cout<<"NO";
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		solve();
		cout<<endl;
	}
	return 0;
}