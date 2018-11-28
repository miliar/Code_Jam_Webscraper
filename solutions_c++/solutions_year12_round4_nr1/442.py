#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<iostream>
#define N 25000
using namespace std;

int a[N],b[N],f[N];

int main()
{
	int t,n,i,j,ys=0;

	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
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
			printf("NO\n");
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

		if (f[n+1])
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}



