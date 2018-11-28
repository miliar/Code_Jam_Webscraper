#include <stdio.h>

void process(int Problem)
{
	int n, k;
	int p = 1;
	scanf("%d %d", &n, &k);
	p <<= n;
	p--;
	k &= p;
	k ^= p;

	if( k == 0 ) 
	{
		printf("Case #%d: %s\n", Problem, "ON");
	}
	else
	{
		printf("Case #%d: %s\n", Problem, "OFF");
	}
}
int main()
{
	int T;
	freopen("A-small.in","r", stdin);
	freopen("output.txt","w", stdout);
	scanf("%d",&T);
	for(int i=1; i<=T; i++)
	{
		process(i);
	}
	return 0;
}