#include <stdio.h>

int main()
{
	int t, n, k, z;

	z = 1;
	scanf("%d", &t);
	while(t > 0)
	{
		scanf("%d %d", &n, &k);
		k %= (1 << n);
		k = (k == ((1 << n) - 1));
		printf("Case #%d: %s\n", z++, (k==1) ? "ON" : "OFF");
		t--;
	}

	return 0;
}