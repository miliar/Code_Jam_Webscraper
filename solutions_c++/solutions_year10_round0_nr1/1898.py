#include <stdio.h>

int main(int argc, char* argv[])
{
	FILE* is = freopen(argv[1], "r", stdin);
	FILE* os = freopen(argv[2], "w", stdout);

	int t;

	scanf("%d", &t);

	int n, k;

	for (int i = 1; i<=t; i++)
	{
	scanf("%d%d", &n, &k);
	
	unsigned int uk = k;
	unsigned int base = 1;
	base = base << n;
	uk = uk % base;
	if ( uk+1 == base )
		printf("Case #%d: ON\n", i);
	else
		printf("Case #%d: OFF\n", i);

	}


	fclose(is);
	fclose(os);
	return 0;
}