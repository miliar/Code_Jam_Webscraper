#include <stdio.h>

int casen;
int n;
int a[1111];

void solve()
{
	int ans=0;
	int sum=0;
	int min=99999999;
	for(int i=1;i<=n;i++)
	{
		ans^=a[i];
		sum+=a[i];
		if(a[i]<min) min=a[i];
	}
	if(ans!=0) printf("NO\n");
	else printf("%d\n",sum-min);
}

int main()
{
	scanf("%d",&casen);
	int j=0;
	while(casen--)
	{
		j++;
		printf("Case #%d: ",j);
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
			scanf("%d",&a[i]);
		solve();
	}
	return 0;
}
