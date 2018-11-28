#include<iostream>
using namespace std;
bool cmp(int a,int b)
{
	return a>b;
}
long long a[809],b[809],ans;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.in.out","w",stdout);
	int ca;
	scanf("%d",&ca);
	int tca=0;
	while(tca++<ca)
	{
		int n;
		scanf("%d",&n);
		int i,j;
		for(i=1;i<=n;i++)
		{
			scanf("%I64d",&a[i]);
		}
		for(j=1;j<=n;j++)
		{
			scanf("%I64d",&b[j]);
		}
		sort(a+1,a+n+1);
		sort(b+1,b+n+1,cmp);
		ans=0;
		for(i=1;i<=n;i++)
		{
			ans+=a[i]*b[i];
		}
		printf("Case #%d: %I64d\n",tca,ans);
	}
}
