#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>
#include<math.h>


int ncase;
FILE *pf;
FILE *pfOut;
char state[2][4] = {"OFF", "ON"};
int Toggle(int n, long k){
	long mask;
	mask = pow(2,n) -1;
	k %= (mask + 1);
	if(k == mask)
		return 1;
	else
		return 0;
}
void main(){
	long currK;
	int currN;
	int i;
	char out[2000];
	clrscr();
	pf = fopen("A-large.in", "rt");
	pfOut = fopen("A-large.out", "wt");
	fscanf(pf, "%d", &ncase);
	for(i=0;i<ncase;i++){
		fscanf(pf, "%d %ld", &currN, &currK);
		sprintf(out,"Case #%d: %s\n", i+1, state[Toggle(currN, currK)]);
		printf("%s", out);
		fprintf(pfOut, "%s", out);
	}
	fclose(pf);
	getch();
}
