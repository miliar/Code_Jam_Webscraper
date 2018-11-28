#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<cmath>

using namespace std;

struct zib
{
	string s;
};

bool operator < ( zib a, zib b)
{
	int k=a.s.size();
	int i;
	for(i=k;i>=0;--i)
	{
		if(a.s[i]=='1' && b.s[i]=='0')
			return false;
		if(a.s[i]=='0' && b.s[i]=='1')
			return true;
	}
	return true;
}

int main()
{
	freopen("output.txt","w",stdout);
	zib a[50];
	zib b[50];
	int l,t,n,i,j,ans;
	zib cur;
	
	int ii;
	cin>>t;
	for(l=0;l<t;++l)
	{
		ans=0;
		cin>>n;
		for(i=0;i<n;++i)
		{
			cin>>a[i].s;
			b[i].s.resize(n);
			for(j=0;j<=i;++j)
				b[i].s[j]='1';
			for(;j<n;++j)
				b[i].s[j]='0';
		}
		for(i=0;i<n;++i)
		{
			for(j=i;!(a[j]<b[i]);++j);
			ans+=j-i;
			while(j>i)
			{
				swap(a[j],a[j-1]);
				--j;
			}
			
		}
		cout<<"Case #"<<l+1<<": "<<ans<<endl;
	}
	return 0;
}