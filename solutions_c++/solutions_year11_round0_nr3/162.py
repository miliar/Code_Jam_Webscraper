#include<iostream>
using namespace std;
long long a[1001];
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("C_large.txt","wt",stdout);
	int TC,i,x,y,j,n;
	long long tot,ans;
	cin>>TC;
	for(int tc=0;tc<TC;tc++)
	{
		cin>>n;
		for(i=0;i<n;i++)
			cin>>a[i];
		
		ans = -1;

		for(i=0;i<n;i++)
		{
			tot = 0;
			x = 0;
			for(j=0;j<n;j++)
				if(i!=j){ x^=a[j]; tot+=a[j];}
			if( x == a[i] && tot>ans)
				ans = tot;

		}
		//for(i=1;i+1<(1<<n);i++)
		//{
		//	x = y = 0;
		//	tot = 0;
		//	for(j=0;j<n;j++)
		//		if(i&(1<<j))
		//		{
		//			x^=a[j];
		//			tot+=a[j];
		//		}
		//		else y^=a[j];

		//	if(x == y && ans< tot)
		//		ans = tot;
		//}
		cout<<"Case #"<<tc+1<<": ";
		if(ans == -1)
			cout<<"NO"<<endl;
		else cout<<ans<<endl;
	}
	return 0;
}