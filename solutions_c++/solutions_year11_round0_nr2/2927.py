#include <stdio.h>
#include <conio.h>

#define SAFE_DEL(x)	{if(x) {delete x; x = NULL;}}
#define SAFE_DEL_ARRAY(x)	{if(x) {delete[] x; x = NULL;}}
#define	SAFE_DEL_ARRAY_ARRAY(x, n)	{for(int i = 0; i < n; i++) SAFE_DEL_ARRAY(x[i]); SAFE_DEL_ARRAY(x);}

void main ()
{
	FILE* pRFile = fopen("B-small-attempt1.in", "rt");

	if(!pRFile)
	{
		printf("Cannot open file for reading");
		getch();
		return;
	}

	FILE* pWFile = fopen("B-small-attempt1.out", "wt");
	
	if(!pWFile)
	{
		printf("Cannot open file for writing");
		fclose(pRFile);
		getch();
		return;
	}

//trunk_________________

	int t, c, d, n, i, j, k, l, m, temp;
	int nMarkOPosition;	//number of elements of the array
	int *pMarkOPosition = NULL;	//array for marking opposition
	char *pC = NULL, *pD = NULL, *pN = NULL;	//store data read from file
	//this spends double memory but running faster________
	char **ppCompilation = NULL;	//store data for compilation
	char **ppOpposition = NULL;	//store data for opposition
	char **ppProduct = NULL;		//store product for compilation
	int *p_n_compilation = NULL;	//store number of compilation of a base element
	int *p_n_opposition = NULL;	//store number of opposition of a base element
	const int nELEMENTS = 26;
	const int n_BASE_ELEMENTS = 8;
	const char BASE_ELEMENTS[8] = {'A', 'D', 'E', 'F', 'Q', 'R', 'S', 'W'};
	const char ELEMENT_1ST = 'A';
	//________this spend double memory but running faster
	const int nCOMPILATION = 3;
	const int nOPPOSITION = 2;

	pC = new char[nCOMPILATION];	//init to store each compilation
	pD = new char[nOPPOSITION];		//init to store each opposition

	p_n_compilation = new int[nELEMENTS];	//init
	p_n_opposition = new int[nELEMENTS];	//init

	ppCompilation = new char*[nELEMENTS];	//init to store compilations
	for(i = 0; i < nELEMENTS; i++)	//set to NULL //for safety
		ppCompilation[i] = NULL;
	for(i = 0; i < n_BASE_ELEMENTS; i++)	//only init for base elements //save memory
		ppCompilation[BASE_ELEMENTS[i] - ELEMENT_1ST] = new char[n_BASE_ELEMENTS];

	ppProduct = new char*[nELEMENTS];	//init to store products of compilations
	for(i = 0; i < nELEMENTS; i++)	//set to NULL //for safety
		ppProduct[i] = NULL;
	for(i = 0; i < n_BASE_ELEMENTS; i++)	//only init for base elements //save memory
		ppProduct[BASE_ELEMENTS[i] - ELEMENT_1ST] = new char[n_BASE_ELEMENTS];

	ppOpposition = new char*[nELEMENTS]; //init to store oppositions
	for(i = 0; i < nELEMENTS; i++)	//set to NULL //for safety
		ppOpposition[i] = NULL;
	for(i = 0; i < n_BASE_ELEMENTS; i++)	//only init for base elements //save memory
		ppOpposition[BASE_ELEMENTS[i] - ELEMENT_1ST] = new char[n_BASE_ELEMENTS];;

	fscanf(pRFile, "%d", &t);

//	printf("t = %d", t);	//test

	for(i = 1; i <= t; i++)
	{
		//read c_____________
		fscanf(pRFile, "%d ", &c);

//		printf("\n\nc = %d ", c);	//test

		//reset number of compilation of a base element
		for(j = 0; j < n_BASE_ELEMENTS; j++)
			p_n_compilation[BASE_ELEMENTS[j] - ELEMENT_1ST] = 0;

		for(j = 0; j < c; j++)
		{
			for(k = 0; k < nCOMPILATION; k++)
			{
				fscanf(pRFile, "%c", &pC[k]);

//				printf("%c", pC[k]);	//test
			}
			fscanf(pRFile, "%c", &temp);	//remove the space between strings

			//store data for compilation
			k = pC[0] - ELEMENT_1ST;
			ppCompilation[k][p_n_compilation[k]] = pC[1];
			ppProduct[k][p_n_compilation[k]] = pC[2];
			p_n_compilation[k]++;


			if(pC[0] != pC[1])
			{
				k = pC[1] - ELEMENT_1ST;
				ppCompilation[k][p_n_compilation[k]] = pC[0];
				ppProduct[k][p_n_compilation[k]] = pC[2];
				p_n_compilation[k]++;
			}
		}

		//read d_____________
		fscanf(pRFile, "%d ", &d);

//		printf(" d = %d ", d);	//test

		//reset number of opposition of a base element
		for(j = 0; j < n_BASE_ELEMENTS; j++)
			p_n_opposition[BASE_ELEMENTS[j] - ELEMENT_1ST] = 0;

		for(j = 0; j < d; j++)
		{
			for(k = 0; k < nOPPOSITION; k++)
			{
				fscanf(pRFile, "%c", &pD[k]);

//				printf("%c", pD[k]);	//test
			}
			fscanf(pRFile, "%c", &temp);	//remove the space between strings

			//store data for opposition
			k = pD[0] - ELEMENT_1ST;
			ppOpposition[k][p_n_opposition[k]] = pD[1];
			p_n_opposition[k]++;

			if(pD[0] != pD[1])
			{
				k = pD[1] - ELEMENT_1ST;
				ppOpposition[k][p_n_opposition[k]] = pD[0];
				p_n_opposition[k]++;
			}
		}

		//read n_____________
		fscanf(pRFile, "%d ", &n);

//		printf(" n = %d ", n);	//test

		pN = new char[n];

		for(j = 0; j < n; j++)
		{
			fscanf(pRFile, "%c", &pN[j]);

//			printf("%c", pN[j]);	//test
		}

		/*/test_
		if(i == 100)
		{
			printf("\nCompilation");
			for(j = 0; j < nELEMENTS; j++)
			{
				if(p_n_compilation[j] > 0)
				{
					printf("\n%c\t", ELEMENT_1ST + j);
					for(k = 0; k < p_n_compilation[j]; k++)
						printf("%c ", ppCompilation[j][k]);
					printf("\nproduct\t");
					for(k = 0; k < p_n_compilation[j]; k++)
						printf("%c ", ppProduct[j][k]);
				}
			}
			printf("\nOpposition");
			for(j = 0; j < nELEMENTS; j++)
			{
				if(p_n_opposition[j] > 0)
				{
					printf("\n%c\t", ELEMENT_1ST + j);
					for(k = 0; k < p_n_opposition[j]; k++)
						printf("%c ", ppOpposition[j][k]);
				}
			}
		}
		//_test*/

		//calculate the result_____________

		pMarkOPosition = new int[n];
		nMarkOPosition = 0;

		/*/test_
		if(i == 100)
			int a = 0;
		//_test*/

		for(j = 0; j < n; j++)
		{
			//check compilation
			if(p_n_compilation[pN[j] - ELEMENT_1ST] > 0 && j > 0)
			{
				for(k = 0; k < p_n_compilation[pN[j] - ELEMENT_1ST]; k++)	//check the list
				{
					if(pN[j-1] == ppCompilation[pN[j] - ELEMENT_1ST][k])
					{
						//if pN[j-1] is marked opposition, remove it
						if(nMarkOPosition > 0
							&& pMarkOPosition[nMarkOPosition] == j)
						{
							nMarkOPosition--;
						}
						//replace the 2 ones by their compilation
						pN[j-1] = ppProduct[pN[j] - ELEMENT_1ST][k];
						//translate the pN
						for(l = j; l < n-1; l++)
							pN[l] = pN[l+1];
						//reset the number
						n--;
						j -= 1;	//not j -= 2
								//because i will check opposition of the next right now
						break;
					}
				}
			}
			//check opposition: if found, delete, if not, mark
			if(p_n_opposition[pN[j] - ELEMENT_1ST] > 0)
			{
				//if found, delete
				if(nMarkOPosition > 0)
				{
					for(k = 0; k < nMarkOPosition; k++)
						for(l = 0; l < p_n_opposition[pN[j] - ELEMENT_1ST]; l++)
						{
							if(pN[pMarkOPosition[k]] == ppOpposition[pN[j] - ELEMENT_1ST][l])
							{
								//delete
								if(j == n - 1)	//!this is a special case, the result is []
								{
									n = 0;
									break;
								}
								for(m = j + 1; m < n; m++)
									pN[m - j - 1] = pN[m];
								//reset the number
								n -= (j + 1);
								j = 0;	//this will check opposition of the next right now
								nMarkOPosition = 0;
							}
						}
				}
				//mark
				pMarkOPosition[nMarkOPosition] = j;
				nMarkOPosition++;
			}
			/*/test_
			if(i == 100)
			{
				for(k = 0; k < j; k++)
					printf("%c", pN[k]);
				printf("\n");
			}
			//_test*/
		}

		fprintf(pWFile, "Case #%d: [", i);
		for(j = 0; j < n-1; j++)
			fprintf(pWFile, "%c, ", pN[j]);
		if(n > 0)	//!this is a special case, the result is []
			fprintf(pWFile, "%c", pN[j]);
		fprintf(pWFile, "]\n");
		//_____________calculate the result

		SAFE_DEL_ARRAY(pN);
		SAFE_DEL_ARRAY(pMarkOPosition);

	}

//______________________

	SAFE_DEL_ARRAY(pC);
	SAFE_DEL_ARRAY(pD);
	SAFE_DEL_ARRAY(p_n_compilation);
	SAFE_DEL_ARRAY(p_n_opposition);
	SAFE_DEL_ARRAY_ARRAY(ppProduct, nELEMENTS);
	SAFE_DEL_ARRAY_ARRAY(ppCompilation, nELEMENTS);
	SAFE_DEL_ARRAY_ARRAY(ppOpposition, nELEMENTS);

	fclose(pRFile);
	fclose(pWFile);

	printf("\nSuccessful");
	getch();
}