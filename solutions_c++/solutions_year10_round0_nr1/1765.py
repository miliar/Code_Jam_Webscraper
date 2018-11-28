#include<cstdio>

int n,m;
int t,cases;

int main()
{
	for (scanf("%d",&t);t--;)
	{
		scanf("%d%d",&m,&n);
		n%=(1<<m);
		printf("Case #%d: %s\n",++cases,n==(1<<m)-1?"ON":"OFF");
	}
}
