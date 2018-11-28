#include <stdio.h>
#include <string.h>

int cs, ct, base;
char s[100];
int mark[300];
long long ans;

int main()
{
	int i;
	scanf("%d", &cs);
	for (ct = 1; ct <= cs; ct++) {
		scanf("%s", s);
		memset(mark, -1, sizeof(mark));
		base = 0;
		for (i = 0; s[i]; i++)
		if (mark[s[i]] < 0) {
			if (base == 0) mark[s[i]] = 1;
			else if (base == 1) mark[s[i]] = 0;
			else mark[s[i]] = base;
			base++;
		}
		if (base == 1) base = 2;
		ans = 0;
		for (i = 0; s[i]; i++)
			ans = ans * base + mark[s[i]];
		printf("Case #%d: %lld\n", ct, ans);
	}
	return 0;
}
