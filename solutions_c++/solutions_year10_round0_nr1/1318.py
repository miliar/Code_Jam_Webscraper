#include <stdio.h>

int cases, caseno, n, m;

int main() {
	freopen("a3.in", "r", stdin);
	
	freopen("a.ans", "w", stdout);

	scanf("%d", &cases);
	while( cases-- ) {
		scanf("%d %d", &n, &m);
		m %= (1 << n);
		printf("Case #%d: ", ++caseno);
		if( m + 1 == (1 << n) ) puts("ON");
		else puts("OFF");
	}
	return 0;
}
