#include<cstdio>

void func()
{
	int ans = 0;
	int n,s,p;
	scanf("%d%d%d",&n,&s,&p);
	int k = 3*p - 2;
	for(int c=1;c<=n;c++)
	{
		int i;
		scanf("%d",&i);
		if( i >= k ) ans ++;
		else if( i >= ( k - 2 ) and s > 0 and p != 1 )
		{
			ans ++;
			s --;
		}
	}

	printf("%d",ans);
}

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		printf("Case #%d: ",c);
		func();
		if( c != t ) printf("\n");
	}
}
