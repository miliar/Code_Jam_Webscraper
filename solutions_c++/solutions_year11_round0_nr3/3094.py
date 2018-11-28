#include <stdio.h>
#include <conio.h>

#define SAFE_DEL(x)	{if(x) {delete x; x = NULL;}}
#define SAFE_DEL_ARRAY(x)	{if(x) {delete[] x; x = NULL;}}
#define	SAFE_DEL_ARRAY_ARRAY(x, n)	{for(int i = 0; i < n; i++) SAFE_DEL_ARRAY(x[i]); SAFE_DEL_ARRAY(x);}

void main ()
{
	FILE* pRFile = fopen("C-large.in", "rt");

	if(!pRFile)
	{
		printf("Cannot open file for reading");
		getch();
		return;
	}

	FILE* pWFile = fopen("C-large.out", "wt");
	
	if(!pWFile)
	{
		printf("Cannot open file for writing");
		fclose(pRFile);
		getch();
		return;
	}

//trunk_________________
	int t, n, i, j, xorResult, min;
	int *pC = NULL;	//1 <= c[i] <= 10^6, so int (4 bytes) is enough
	unsigned int sum;	//make sure large enough

	fscanf(pRFile, "%d ", &t);

//	printf("%d\n", t);	//test

	for(i = 1; i <= t; i++)
	{
		fscanf(pRFile, "%d\n", &n);

//		printf("%d\n", n);	//test

		if(n <= 0)	//check the special case
		{
			fprintf(pWFile, "Case #%d: NO\n", i);
			continue;
		}

		pC = new int[n];

		for(j = 0; j < n-1; j++)
		{
			fscanf(pRFile, "%d ", &pC[j]);

//			printf("%d ", pC[j]);	//test
		}

		fscanf(pRFile, "%d\n", &pC[j]);

//		printf("%d\n", pC[j]);	//test

		//check if posibility
		xorResult = pC[0];

		for(j = 1; j < n; j++)
			xorResult ^= pC[j];

		if(xorResult != 0)
		{
			fprintf(pWFile, "Case #%d: NO\n", i);
			continue;
		}

		//it's posible, find the smallest candy
		sum = pC[0];
		min = pC[0];
		for(j = 1; j < n; j++)
		{
			sum += pC[j];

			if(min > pC[j])
				min = pC[j];
		}

//		printf("sum %u, min %d\n", sum, min);	//test

		sum -= min;

		fprintf(pWFile, "Case #%d: %u\n", i, sum);

		SAFE_DEL_ARRAY(pC);
	}
//_________________trunk

	SAFE_DEL_ARRAY(pC);

	fclose(pRFile);
	fclose(pWFile);

	printf("\nSuccessful");
	getch();
}