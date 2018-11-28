#include <cstdio>

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int test,t,n,k;
	scanf("%d",&test);
	for(t=1;t<=test;t++)
	{
		scanf("%d%d",&n,&k);
		if(k%(1<<n)==((1<<n)-1))
			printf("Case #%d: ON\n",t);else
			printf("Case #%d: OFF\n",t);
	}
	return 0;
}
