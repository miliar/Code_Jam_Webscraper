#include <stdio.h>

int cs, ct;
long long n;
int pd, pg;

bool check()
{
	if (pd < 100 && pg == 100) return false;
	if (pd > 0 && pg == 0) return false;
	if (pd == 0) return true;

	int j;
	for (j = pd; j > 0; j--)
		if (pd % j == 0 && 100 % j == 0) break;

	if (n < 100 / j) return false;
	return true;
}

int main()
{
	scanf("%d", &ct);
	for (cs = 1; cs <= ct; cs++) {
		scanf("%lld%d%d", &n, &pd, &pg);
		printf("Case #%d: %s\n", cs, check() ? "Possible" : "Broken");
	}
	return 0;
}
