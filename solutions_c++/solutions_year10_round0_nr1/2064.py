#include<stdio.h>
#include<string.h>

int main()
{
	int t, i, n, k;

	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	//freopen("A-big.in", "r", stdin);
	//freopen("A-big.out", "w", stdout);

	scanf("%d", &t);
	for(i=1; i<=t; i++){
		printf("Case #%d: ", i);
		scanf("%d %d", &n, &k);
		n = 1<<n;
		k = k%n;
		puts((k==n-1)?"ON":"OFF");
	}
	return 0;
}
