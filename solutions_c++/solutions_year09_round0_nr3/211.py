#include <stdio.h>
#include <string.h>

char text [1000];
int n;
int cont [100];
char welcome [100];
int main () {
	freopen ("C.in","r",stdin);
	freopen ("C.out","w",stdout);
	scanf ("%d", &n);
	strcpy (welcome, " welcome to code jam");
	 
	gets (text);
	for (int caso = 0; caso < n; ++caso) {
		for (int i = 1; welcome[i]; ++i) {
			cont[i] = 0;	
		}
		cont[0] = 1;
		gets(text);
		for (int i = 0; text[i]; ++i) {
			for (int j = 1; welcome[j]; ++j) {
				if (text[i] == welcome[j]) {
					cont[j] = (cont[j] + cont[j-1])%10000;	
				}
			}
		}
		printf ("Case #%d: %04d\n", caso+1, cont[19]);
	}
	return 0;	
}
