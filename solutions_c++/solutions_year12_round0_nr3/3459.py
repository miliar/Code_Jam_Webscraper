#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main() {
	int size, count = 1;
	char n[10];
	char m[10];
	char x[10];
	int a, b;
	int i, j;
	int ln, lm;
	int r;
	short flag;
	scanf("%d", &size);
	while(size--) {
		r = 0;
		scanf("%d %d", &a, &b);
		for(i = a + 1; i <= b; i++) {
			for(j = a; j < i; j++) {
				sprintf(n,"%d",j);
				sprintf(m,"%d",i);
				ln = strlen(n);
				lm = strlen(m);
				if(ln == lm) {
					while(--ln) {
						memcpy(x, n + (lm - ln), ln);
						memcpy(x + ln, n, lm - ln);
						if(!memcmp(x, m, lm)) {
							r++;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n", count++, r);
	}
	return 0;
}