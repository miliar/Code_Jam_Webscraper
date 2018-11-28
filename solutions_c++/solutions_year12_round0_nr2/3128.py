#include <algorithm>
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,n,s,p,ans,ss,no;
	int a[105];
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n>>s>>p;
		for(int i=0;i<n;i++)
			cin>>a[i];
		ans=0;
		ss=0;
		no=0;
		for(int i=0;i<n;i++)
		{
			if(a[i]-p<0)
				continue;
			if((a[i]-p)/2>=p-1)
				ans++;
			else if((a[i]-p)/2>=p-2)
				ss++;
			else
				no++;
		}
		cout<<"Case #"<<t<<": "<<ans+min(ss,s)<<endl;
	}
	return 0;
}
