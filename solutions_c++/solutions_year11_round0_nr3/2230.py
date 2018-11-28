#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

int a[1100];
int cmp(int x,int y)
{
	return x>y;
}
int main()
{
    freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,t=1,i,n;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		int ans=0;
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			ans^=a[i];
		}
		if(ans!=0)
		{
			printf("Case #%d: NO\n",t++);
			continue;
		}
		sort(a+1,a+n+1,cmp);
		int sum=0;
		for(i=1;i<=n-1;i++)
			sum+=a[i];
		printf("Case #%d: %d\n",t++,sum);
	}
	return 0;
}