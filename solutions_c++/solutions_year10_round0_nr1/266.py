#include <stdio.h>

int main() {
	int ecase, ecount;
	int en,ek;
	int i;
	scanf("%d",&ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		scanf("%d%d",&en, &ek);
		int t = 1;
		for (i = 0; i < en; i++)
			t *= 2;
		if ((ek + 1) % t == 0)
			printf("Case #%d: ON\n", ecount);
		else
			printf("Case #%d: OFF\n", ecount);
	}
	return 0;
}
