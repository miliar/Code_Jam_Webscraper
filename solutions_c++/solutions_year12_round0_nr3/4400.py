#include <cstdio>
#include <cstring>

int main() {
	int h, cases, i, j, count, a, b;
	char n[7], m[14];

	scanf("%d", &cases);

	for (h=0; h<cases; ++h) {
		scanf("%d %d", &a, &b);

		count = 0;

		for (i=a; i<=b; ++i) {
			for (j=i+1; j<=b; ++j) {
				sprintf(n, "%d", i);
				sprintf(m, "%d", j);
		
				strcat(m, m);
			
				if (strstr(m, n) != NULL) {
					//puts("MATCH");
					count += 1;
				}
			}
		}

		printf("Case #%d: %d\n", h+1, count);
	}
	

	return 0;
}
