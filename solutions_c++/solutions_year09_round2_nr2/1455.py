#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int t, n, res;
char numero[32], numeroNuovo[32];
int cifre[9], cifreNuovo[9];

int nextNumber(int n) {
	sprintf(numero,"%d",n);

	for(int j=0; j<9; j++)
		cifre[j] = 0;

	for(int j=0; j<strlen(numero); j++)
		cifre[numero[j]-49]++;

	int j;

	for(j=n+1;;j++) {
		bool match=true;
		sprintf(numeroNuovo,"%d",j);
		//printf("%d\n", j);
		for(int k=0; k<9; k++)
			cifreNuovo[k] = 0;

		for(int k=0; k<strlen(numeroNuovo)&&match; k++) {
			cifreNuovo[numeroNuovo[k]-49]++;
		}
		
		for(int k=0; k<10&&match; k++)
			if(cifre[k]!=cifreNuovo[k])
				match=false;

		if(match) break;
	}

	return j;
}

int main() {
	FILE *fin=fopen("B-small-attempt2.in","r");
	FILE *fout=fopen("B.out","w");

	fscanf(fin, "%d", &t);

	for(int i=0; i<t; i++) {
		fscanf(fin, "%d", &n);
		res = nextNumber(n);
		//printf("%d Case #%d: %d\n", n, i+1, res);
		fprintf(fout, "Case #%d: %d\n",i+1, res);
	}
}
