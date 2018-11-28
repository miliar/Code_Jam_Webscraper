#include <iostream>
using namespace std;
int gcd(int a,int b)
{
	if (b==0)
	{
		return a;
	}
	return gcd(b,a%b);
}
int main()
{
	int t;
	int n,m[1005];
	int a,b,c;
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	int i,j;
	for (i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for (j=1;j<=n;j++)
		{
			scanf("%d",&m[j]);
		}
		int ans;
		if (n==2)
		{
			a=abs(m[1]-m[2]);
			ans=a;
		}
		else if (n==3)
		{
			a=abs(m[1]-m[2]);
			b=abs(m[2]-m[3]);
			c=abs(m[1]-m[3]);
//			cout<<a<<" "<<b<<" "<<c<<endl;
				ans=gcd(a,b);
	//	cout<<ans<<endl;
		ans=gcd(ans,c);
		}
	
	//	cout<<ans<<endl;
		printf("Case #%d: %d\n",i,(ans-(m[1]%ans))%ans);
	}
	return 0;
}