#include <stdio.h>
#include <stdlib.h>

int main () {
	int t, n, k;
	scanf ("%d", &t);
	
	int caso = 1;
	while (t--) {
		scanf ("%d%d", &n, &k);
		if (k && (1<<n)-1 == (k & ((1<<n) - 1))) printf ("Case #%d: ON\n", caso++);
		else printf ("Case #%d: OFF\n", caso++);
	}
	return 0;
}

