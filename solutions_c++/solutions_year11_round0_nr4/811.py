#include<iostream>
#include<cstdio>
using namespace std;
const int MAXN=1009;
int T,n,a,ans;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("d_l.out","w",stdout);
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%d",&n);	ans=0;
		for (int i=1;i<=n;i++)	
		{	
			scanf("%d",&a);	
			if (a!=i) ans++;
		}
		printf("Case #%d: %d.000000\n",t,ans);
	}
	return 0;
}

