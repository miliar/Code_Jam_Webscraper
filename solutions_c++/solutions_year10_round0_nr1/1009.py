#include <stdio.h>

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	int cas = 0;
	int n , k;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d: ",++cas);
		scanf("%d%d",&n,&k);
		int x = 1<<n;
		if(k%x == x-1) printf("ON\n");else printf("OFF\n");
	}
	return 0;
}
