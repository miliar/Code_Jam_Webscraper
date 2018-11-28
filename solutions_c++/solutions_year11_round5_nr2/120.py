#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#pragma warning (disable:4996)

const int M=10000;

int a[10001],b[10001];


int q[10002];
int main()
{
	int t,T=0,front,rear;
	int i,j,n,l,m,r,ans;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	for(scanf("%d",&t);t--;)
	{
		scanf("%d",&n);
		for(i=1;i<=10000;++i) a[i]=0;
		for(i=1;i<=n;++i) scanf("%d",&j), ++a[j];

		ans=n;
		rear=0;
		front=0;
		for(i=0;i<=M+1;++i)
		{
			if(a[i]>a[i-1])
			{
				for(j=1;j<=a[i]-a[i-1];++j)
					q[++rear]=i;
			}
			else if(a[i]<a[i-1])
			{
				for(j=1;j<=a[i-1]-a[i];++j)
				{
					++front;
					if(i-q[front]<ans) ans=i-q[front];
				}
			}
		}

		printf("Case #%d: %d\n",++T,ans);
	}
	return 0;
}
