#include<iostream>
using namespace std;
int a[10001];
int b[10001];
int min(int x,int y)
{
	if(x>=y)
		return y;
	else
		return x;
}
int max(int x,int y)
{
	if(x>=y)
		return x;
	else
		return y;
}
int main()
{
	int t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	int x=0;
	int n;
	while(t--)
	{
		scanf("%d",&n);
		int i;
		for(i=1;i<=n;i++)
		{
			scanf("%d%d",&a[i],&b[i]);
		}
		int ans=0;
		int j,k;
		for(i=1;i<=n;i++)
			for(j=i+1;j<=n;j++)
			{
				int x=min(a[i],b[i]);
				int y=max(a[i],b[i]);

				int h=min(a[j],b[j]);
				int g=max(a[j],b[j]);
				if(a[i]*b[j]!=b[i]*a[j])
				{
					if((a[i]>a[j]&&b[i]>b[j])||(a[i]<a[j]&&b[i]<b[j]))
						continue;
					else
					ans++;
				}
			}
		printf("Case #%d: %d\n",++x,ans);
	}
	return 0;
}



