#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	int n,t,m,i,j,k,ans;

	freopen("dl.in","r",stdin);
	freopen("dl.out","w",stdout);
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d",&n);
		ans=n;
		for(j=1;j<=n;j++)
		{
			scanf("%d",&k);
			if (k==j) ans--;
		}
		printf("Case #%d: %d.000000\n",i,ans);
	}
	//system("pause");
	return 0;
}