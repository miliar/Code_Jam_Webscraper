#include <stdio.h>
#include <string.h>

#define maxn 110
int a[maxn];
int n;

bool test(int m)
{
	for(int i=0;i<n;++i)
		if(m%a[i] != 0 && a[i] % m != 0)
			return false;
	return true;
}

void solve()
{
	int l,r;
	scanf("%d%d%d",&n,&l,&r);
	for(int i=0;i<n;++i)
		scanf("%d",&a[i]);
	for(int i=l;i<=r;++i)
		if(test(i))
		{
			printf("%d\n",i);
			return ;
		}
	puts("NO");
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

