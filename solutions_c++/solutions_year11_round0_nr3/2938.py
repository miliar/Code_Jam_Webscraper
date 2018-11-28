#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdio>
#include<algorithm>

using namespace std;

const int maxn=1005;
int a[maxn];

int main()
{
freopen("a.in","r",stdin);
freopen("a.out","w",stdout);
	int cas;
	int ca=0;
	int n,i;
	scanf("%d",&cas);
	while (cas--)
	{
		ca++;
		int t=0;
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			t=t^a[i];
		}
		if (t==0)
		{
			int ans=0;
			sort(a,a+n);
			for (i=1;i<n;i++)
				ans+=a[i];
			printf("Case #%d: %d\n",ca,ans);
		}
		else
		{
			printf("Case #%d: NO\n",ca);
		}
	}


fclose(stdin);
fclose(stdout);
return 0;
}