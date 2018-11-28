#include <stdio.h>

int gcd(int a, int b) {
	if (b == 0)
		return a;
	else
		return gcd(b, a%b);
}

char getState(int n) {
	if (n == 0)
		return '0';
	else if (n == 100)
		return '1';
	else
		return 'x';
}

int main() {
	int ecase, ecount;
	long long int en;
	int ed, eg;

	scanf("%d", &ecase);
	for (ecount = 1; ecount <= ecase; ecount++) {
		scanf("%I64d%d%d", &en, &ed, &eg);
		int min;
		if (ed == 0)
			min = 0;
		else
			min = 100 / gcd(ed, 100);

		if (min > en)
			printf("Case #%d: Broken\n", ecount);
		else {
			char sd = getState(ed);
			char sg = getState(eg);
			if (sd == 'x' && sg == '0')
				printf("Case #%d: Broken\n", ecount);
			else if (sd == '1' && sg == '0')
				printf("Case #%d: Broken\n", ecount);
			else if (sd == '0' && sg == '1')
				printf("Case #%d: Broken\n", ecount);
			else if (sd == 'x' && sg == '1')
				printf("Case #%d: Broken\n", ecount);
			else
				printf("Case #%d: Possible\n", ecount);
		}
	}

	return 0;
}
