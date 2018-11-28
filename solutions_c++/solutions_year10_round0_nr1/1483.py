#include <stdio.h>

int t;
int n;
int k;
int i;
int aux;

int main() {
	FILE* fp = fopen("attempt0.out", "w");
	i=1;
	scanf("%d", &t);	
	
	for (i=1; i<=t; i++) {
		scanf(" %d%d", &n, &k);

		aux = (1<<n);

		k = (k%aux);

		fprintf(fp, "Case #%d: ", i);

		if (k == (aux-1)) {
			fprintf(fp, "ON\n");
		} else {
			fprintf(fp, "OFF\n");
		}
	}
	
	fclose(fp);

	return 0;
}
