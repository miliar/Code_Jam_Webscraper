#include <stdio.h>
#include <string.h>

inline int transform(int b, int exp)
{
	return (b%10 * exp) + b/10;
}

long long int answer(int a, int b, int exp, int it)
{
	long long int ans = 0;
	int i, j;
	for(i = a; i <= b; ++i)
	{
		int k = i;
		for(j = 0; j < it; ++j)
		{
			k = transform(k,exp);
			if(k > b || i >= k) continue;
			//printf("%lld (%d,%d)\n",ans,i,k);
			ans++;
		}
	}
	return ans;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t, j, exp, a, b, it;
	scanf("%d",&t);
	for(j = 1; j <= t; ++j)
	{
		scanf("%d %d",&a,&b);
		for(exp = 1, it = 0; a/exp >= 10; exp *= 10, it++);
		printf("Case #%d: ",j);		
		if(exp == 1) printf("0\n");
		else printf("%lld\n",answer(a,b,exp,it));
	}
	return 0;
}
