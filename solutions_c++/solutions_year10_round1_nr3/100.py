#include <cstdio>
#include <iostream>

using namespace std;
int a[1100000];
int i,j,k,s,t,n,m,a1,a2,b1,b2,T,I;

main()
{
	a[2]=1;
	a[3]=1;
	a[4]=2;
	
	for (i=3;i<=1000000;++i)
	{
		if (a[a[i-1]+1]<i-(a[i-1]+1))
			a[i]=a[i-1]+1;
		else
			a[i]=a[i-1];
	}

	scanf("%d",&T);
	
	for (I=1;I<=T;++I)
	{
		long long ans=0;
		scanf("%d%d",&a1,&a2);
		scanf("%d%d",&b1,&b2);
		for (i=a1;i<=a2;++i)
		{
			if (a[i]>b2)
				ans=ans+(long long)(b2-b1+1);
			else if (a[i]>=b1)	
				ans=ans+(long long)(a[i]-b1+1);

		}
		for (i=b1;i<=b2;++i)
		{
			if (a[i]>a2)
				ans=ans+(long long)(a2-a1+1);
			else if (a[i]>=a1)	
				ans=ans+(long long)(a[i]-a1+1);
		}
		cout<<"Case #"<<I<<": "<<ans<<endl;
	}
}
