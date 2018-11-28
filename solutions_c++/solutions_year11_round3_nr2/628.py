
#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int a[10000],c[10000],dd[1100];

int main()
{
	int t;
	int n,l,i,j,time,m;
	freopen("C.out","w",stdout);
	scanf("%d",&t);
	int d = 1;
	while(t--)
	{
		scanf("%d %d %d %d",&l,&time,&n,&m);
		for(i=0;i<m;i++)
			scanf("%d",&a[i]);
		printf("Case #%d: ",d++);
		long long ans = 0;
		j = 0;
		int k = 0;
		for(i=0;i<n;i++)
		{
			if(ans > time)
			{
				dd[k++] = a[j];
			}
			else
			{
				ans += a[j]*2;
				if(ans > time)
				{
					dd[k++] = (ans-time)/2;
					ans = time;
				}
			}
			j++;
			if(j == m)j=0;
		}
		sort(dd,dd+k);
		for(i=k-1;i>=0;i--)
		{
			if(l)
			{
				ans += dd[i];l--;
			}
			else
				ans += dd[i]*2;
		}
		printf("%lld\n",ans);
	}
	return 0;
}