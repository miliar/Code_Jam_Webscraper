#include <stdio.h>
int n,k,T;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		scanf("%d%d",&n,&k);
		int t = k & ((1 << n)-1);
		int res = 0;
		if (t == (1<<n)-1)
			res = 1;
		printf("Case #%d: %s\n",i+1,res?"ON":"OFF");
	}
	return 0;
}