#include <iostream>
using namespace std;

int m[10001];
int d[10001];
int l[10001];
int n, t, total;

bool calculate()
{
	for(int i=1; i<=n; ++i)
		m[i]=-1;
	if(d[1]>l[1]) return false;
	m[1]=d[1];
	int j=2;
	for(int i=1; i<=n; ++i)
	{
		if(m[i]==-1) return false;
		int longest=d[i]+m[i];
		//cout<<m[i]<<" "<<longest<<endl;
		if(longest>=total) return true;
		for(; j<=n; ++j)
		{
			if(longest<d[j]) break;
			m[j]=d[j]-d[i];
			if(m[j]>l[j])
				m[j]=l[j];
		}
	}
	return false;
}

int main()
{
	cin>>t;
	for(int i=1; i<=t; ++i)
	{
		cin>>n;
		for(int j=1; j<=n; ++j)
			cin>>d[j]>>l[j];
		cin>>total;
		cout<<"Case #"<<i<<": ";
		if(calculate()) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}

