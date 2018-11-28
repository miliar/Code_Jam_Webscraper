# include <cstring>
# include <cstdlib>
# include <cstdio>
# include <iostream>
using namespace std;
# define N 20550
int a[N],b[N],f[N];
int main (void)
{
	int t,n,ys=0;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	cin>>t;
	while (t--)
	{
		memset(f,0,sizeof(f));
		cin>>n;
		for (int i=1;i<=n;i++)
			cin>>a[i]>>b[i];
		cin>>a[n+1];
		b[n+1]=100;
		printf("Case #%d: ",++ys);
		if (a[1]>b[1])
		{
			cout<<"NO"<<endl;
			continue;
		}
		f[1]=a[1];
		for (int i=1;i<=n;i++)
			for (int j=i+1;j<=n+1;j++)
				if (a[i]+f[i]>=a[j])
				{
					int d=a[j]-a[i];
					f[j]=max(f[j],min(d,b[j]));
				}
				else break;
		//~ for (int i=1;i<=n+1;i++)
			//~ cout<<f[i]<<endl;
		if (f[n+1])
			cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	return 0;
}
