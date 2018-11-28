#include <cstdlib>
#include <cstdio>


int main()
{
	int casi;
	scanf("%d", &casi);
	for (int c = 1; c <= casi; c++)
	{
		int n, k;
		scanf("%d%d", &n, &k);
		if (k % (1<<n) == ((1<<n)-1))	printf("Case #%d: ON\n", c);
		else printf("Case #%d: OFF\n", c);
	}
	return 0;
}

