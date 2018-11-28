#include<stdio.h>
#include<algorithm>

using namespace std;

int a[4];

int gcd(int x,int y)
{
	int z;
	if (x<y)
	{
		z=x;
		x=y;
		y=z;
	}
	while (x%y!=0)
	{
		z=x%y;
		x=y;
		y=z;
	}
	return y;
}

int main()
{
	int t,p;
	int n,i;
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	scanf("%d",&t);
	for (p=1;p<=t;p++)
	{
		scanf("%d",&n);
		for (i=1;i<=n;i++)
			scanf("%d",&a[i]);
		sort (a+1,a+n+1);
		bool flag=true;
		int s;
		for (i=2;i<=n;i++)
			if (a[i]!=a[i-1])
			{
				if (flag) s=a[i]-a[i-1]; 
				else s=gcd(s,a[i]-a[i-1]);
				flag=false;
			}
		if (a[1]%s==0) printf("Case #%d: 0\n",p);
		else printf("Case #%d: %d\n",p,s-a[1]%s);
	}
	return 0;
}