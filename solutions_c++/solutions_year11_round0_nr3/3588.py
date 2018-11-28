#include <stdio.h>
#include <string.h>

void solve()
{
	int sum = 0;
	int sum1 = 0;
	int n;
	int min = 100000000;
	int tmp;
	scanf("%d",&n);
	for(int i=0;i<n;++i)
	{
		scanf("%d",&tmp);
		if(tmp < min)
			min = tmp;
		sum ^= tmp;
		sum1 += tmp;
	}
	if(sum == 0)
		printf("%d\n",sum1 - min);
	else printf("NO\n");
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}

