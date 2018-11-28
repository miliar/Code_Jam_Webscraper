# include <iostream>

using namespace std;
int n,l,h;
int a[128];

void solve()
{
	for(int i=l;i<=h;++i)
	{
		bool x = true;
		for(int j=0;j<n&&x;++j)
		{
			if(!(i%a[j]==0 || a[j]%i==0))
				x=false;
		}
		if(x)
		{
			cout<<i<<endl;
			return;
		}
	}
	cout<<"NO\n";
}

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;++i)
	{
		cin>>n>>l>>h;
		cout<<"Case #"<<i+1<<": ";
		for(int j=0;j<n;++j)
			cin>>a[j];
		solve();
	}
	return 0;
}
