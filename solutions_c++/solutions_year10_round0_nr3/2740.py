#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>

#define NLIMIT 10
#define KLIMIT 100
#define	RLIMIT 1000

int working[KLIMIT];
int buffer[KLIMIT];

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

void main()
{
	int numOfTestCase=0;
	int maxSeats;
	int maxRuns;
	int numOfRiders;
	int i =0;
	int j=0;
	unsigned long total;

	FILE *fp, *out;

	clrscr();

	memset(buffer, 0, sizeof(buffer));


	fp = fopen("C-smal~1.in", "rt");
	out = fopen("output.txt", "wt");

	fscanf(fp, "%d", &numOfTestCase);

	for(j=0; j<numOfTestCase; j++)
	{

		fscanf(fp, "%d %d %d", &maxRuns, &maxSeats, &numOfRiders);


		for(i=0; i<numOfRiders; i++)
		{
			fscanf(fp, "%d", &buffer[i]);

		}

		total = TotalCost(maxRuns, maxSeats, numOfRiders);
		fprintf(out, "Case #%d: %lu\n", j+1, total);
	}


	fclose(fp);
	fclose(out);
	getch();

}
