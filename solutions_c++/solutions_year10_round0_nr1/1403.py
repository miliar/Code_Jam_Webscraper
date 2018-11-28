#include <cstdio>
#include <cstdlib>


bool solve(int n, int k)
{
	int mask = (1<<n) - 1;
	//fprintf(stderr, "%d\n", mask);
	return (k & mask) == mask;
}

int main()
{
	freopen("A-large.in.txt", "r", stdin);
	
	int nbCases, c = 0;
	scanf("%d", &nbCases);
	while(c != nbCases)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		
		printf("Case #%d: %s\n", ++c, solve(n, k) ? "ON" : "OFF");	
	}
	
	return 0;
}