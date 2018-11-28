#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int a[1500];

int main()
{
	int t,n,i,sum,res;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for (int cnt=1;cnt<=t;cnt++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		res=0;
		sum=0;
		for (i=0;i<n;i++)
		{
			res^=a[i];
			sum+=a[i];
		}
		printf("Case #%d: ",cnt);
		if (res) printf("NO\n");
		else printf("%d\n",sum-a[0]);
	}
	return 0;
}