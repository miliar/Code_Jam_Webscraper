
#include <stdio.h>
#include <string.h>

#define MAX 505

char text[MAX];
char query[20] = "welcome to code jam";

int a[19][MAX]; //a(i,j)=number of apparitions of query[0-j] in text[0-i]


void resolver(int caso) {
	int l = strlen(text);
	int q = strlen(query);
	a[0][0] = (text[0] == query[0]) ? 1 : 0;
	for (int i=1; i<l; i++) {
		a[0][i] = a[0][i-1] + ((text[i] == query[0]) ? 1 : 0);
	}
	for (int i=1; i<q; i++) {
		for (int j=0; j<i; j++) {
			a[i][j] = 0;
		}
		for (int j=i; j<l; j++) {
			a[i][j] = a[i][j-1];
			if (text[j] == query[i]) {
				a[i][j] += a[i-1][j-1];
				a[i][j] %= 10000;
			}			
		}
	}	
	printf("Case #%i: %04i\n", caso, a[q-1][l-1]);
}

int main(int argc, char **argv) {
	int n;
	scanf("%i\n", &n);
	for (int i=0; i<n; i++) {
		gets(text);
		resolver(i+1);		
	}
	return 0;
}