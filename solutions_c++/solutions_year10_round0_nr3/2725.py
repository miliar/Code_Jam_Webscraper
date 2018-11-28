#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<string.h>

#define NLIMIT 10
#define KLIMIT 100
#define	RLIMIT 1000
#define FILENAME "C-small-attempt0.in"

int working[KLIMIT];
int buffer[KLIMIT];
int ncase;
char kbIn[1000];
FILE *pf;
FILE *pfOut;

long sumk(int n){
	long tmp = 0, i;
	for(i=0;i<=n;i++)
		tmp += (long) working[i];
	return tmp;
}

unsigned long TotalCost(int r, int k, int n){
	int ir;
	long sk = 0;
	unsigned long sr = 0;
	int pBuff=0, pWork = 0, pFirst=0;
	for(ir = 0; ir < r; ir++){
		while(sk + (long) buffer[pBuff] <= k){
			working[pWork] = buffer[pBuff];
			if(sumk(pWork) <= k){
				sk = sumk(pWork);
				pWork++;
				pBuff = (pBuff + 1) % n;
			}
			if(pFirst == pBuff) break;
		}
		pFirst = pBuff;
		pWork = 0;
		sr += sk;
		sk = 0;
	}
	return sr;
}
void main(){
	int currR, currK, currN;
	int i,j;
	char out[2000];
	clrscr();
	pf = fopen("C-smal~1.in", "rt");
	pfOut = fopen("CS_a1a.out", "wt");
	memset(kbIn,0,1000);
//	fgets(kbIn, 1000, pf);
//	ncase = atoi(kbIn);
	fscanf(pf, "%d", &ncase);
	for(i=0;i<ncase;i++){
		fscanf(pf, "%d %d %d", &currR, &currK, &currN);
		for(j=0;j<currN;j++)
			fscanf(pf, "%d", &buffer[j]);
		sprintf(out,"Case #%d: %lu\n", i+1, TotalCost(currR, currK, currN));
		printf("%s", out);
		fprintf(pfOut, "%s", out);
	}
	fclose(pf);
	getch();
}
