#include <algorithm>
#include <stdio.h>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t = 0, testCases;
	for (scanf("%d", &testCases); testCases; testCases--)
	{
		t++;
		int n, k;
		scanf("%d %d", &n, &k);

		n = (1 << n);

		printf("Case #%d: ",  t);
		if ((k + 1) % n == 0)
			printf("ON\n");
		else printf("OFF\n");
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
