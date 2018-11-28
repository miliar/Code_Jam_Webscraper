#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int a[1000],r[20];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,n,x,k,ok,sum;
	scanf("%d",&t);
	for(int tt = 0; tt < t; tt++)
	{
		memset(r,0,sizeof(r));
		scanf("%d",&n);
		for(int i = 0; i < n; i++)
		{
			scanf("%d",&a[i]);
			x = a[i];
			k = 0;
			while(x > 0)
			{
				r[k] += x % 2;
				x /= 2;
				++k;
			}			
		}
		ok = 0;
		for(int i = 0; i < 20; i++)
			if (r[i] % 2)
			{
				ok = 1;
				break;
			}
		if (ok) 
		{
			printf("Case #%d: NO\n",tt + 1);
			continue;
		}
		sort(a,a + n);
		sum = 0;
		for(int j = 1; j < n; j++)
			sum += a[j];
		printf("Case #%d: %d\n",tt + 1,sum);
	}
	return 0;
}
