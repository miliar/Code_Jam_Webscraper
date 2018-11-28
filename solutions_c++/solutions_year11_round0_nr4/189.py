#include <iostream>
#include <stdio.h>

using namespace std;

void work(int cc)
{
	int a, i, ans, n;
	scanf("%d",&n);
	ans=n;
    for(i=1;i<=n;i++)
	{
		scanf("%d",&a);
		if(a==i) ans--;
	}
	printf("Case #%d: %d.000000\n",cc,ans);
}

int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	int T;
	scanf("%d",&T);
	int i;
	for(i = 1 ; i <= T ; i++)
	{
		work(i);
	}
	return 0;
}
