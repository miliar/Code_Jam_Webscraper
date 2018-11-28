#include <iostream>

#define MAXN 30

typedef unsigned State;

int main()
{
	freopen("output.txt","wt",stdout);
	freopen("input.txt","rt",stdin);

	int nTest,n,k;
	scanf("%d",&nTest);
	for(int i = 1; i <= nTest; i++)
	{
		scanf("%d %d",&n,&k);
		printf("Case #%d: %s\n",i,(((1<<n)-1) == (k&((1<<n)-1)))? "ON" : "OFF");
	}
	return 0;
}
