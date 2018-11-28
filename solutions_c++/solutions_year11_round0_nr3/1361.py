#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int t,n,m,a[1005],i,j,s,min;

    freopen("cl.in","r",stdin);
	freopen("cl.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for(j=1;j<=n;j++)
			scanf("%d",&a[j]);
		s=a[1]^a[2];
		for(j=3;j<=n;j++) s=s^a[j];
		if (s!=0) printf("Case #%d: NO\n",i);
		else
		{
			s=0;
			for(j=1;j<=n;j++) s+=a[j];
			min=10000001;
			for(j=1;j<=n;j++)
				if (a[j]<min) min=a[j];
			printf("Case #%d: %d\n",i,s-min);
		}
	}
	//system("pause");
	return 0;
}