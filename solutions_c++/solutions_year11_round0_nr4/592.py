#include<iostream>
using namespace std;
int main()
{
//	freopen("D-large.in","r",stdin);
//	freopen("D.out","w",stdout);
	int ct,i,ans,n,tt=0;
	int a;
	scanf("%d",&ct);
	while(ct--)
	{
		scanf("%d",&n);
		ans=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a);
			if(a==i)ans++;
		}
		printf("Case #%d: %d.000000\n",++tt,(n-ans));
	}
	return 0;
}