#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>

//#define LARGE

#ifdef LARGE
char *sFileIn = "./C-large.in";
char *sFileOut = "./C-large.out";
#else
char *sFileIn = "./C-small-attempt2.in";
char *sFileOut = "./C-small-attempt2.out";
#endif
#ifndef UINT
#define UINT unsigned _int64
#endif

const char g_sWelcome[] = "welcome to code jam";
unsigned int g_numFind=0;

int CalculateCountDynamic(std::string *pCaseIn);

int CalculateCount(std::string *pCaseIn);
void FindString(int posW, int posC, std::string * pCaseIn, int lenWelcome, int lenCaseIn);

UINT **New2DimInt(int numx, int numy);
void Release2DimInt(UINT **pDim, int numx, int numy);

int main(int argc, char *argv[])
{
	int i;
	std::ifstream inFile;
	inFile.open(sFileIn);

	std::ofstream outFile;
	outFile.open(sFileOut);

	
	int numCase;
	
	char sLine[1024];
	inFile.getline(sLine, 1023);
	sscanf(sLine, "%d", &numCase);

	std::string *psCaseIn = new std::string[numCase];

	for(i=0; i<numCase; i++)
	{
		inFile.getline(sLine, 1023);
		

		psCaseIn[i] = sLine;
		//printf("%s\n", sLine);
	}
	
	char sOut[256];
	int rlt = 0;
	for(i=0; i<numCase; i++)
	//for(i=1; i<2; i++)
	{
		printf("%s  length=%d\n", psCaseIn[i].c_str(), psCaseIn[i].length());
		
		//rlt = CalculateCount(&psCaseIn[i]);
		rlt = CalculateCountDynamic(&psCaseIn[i]);

		
		//printf("Case#%d: %04d\n", i+1, rlt%10000);
		printf("Case #%d: %04d\n", i+1, rlt);

		sprintf(sOut, "Case #%d: %04d\n", i+1, rlt);

		outFile<<sOut;
	}


	inFile.close();
	outFile.close();

	getchar();

	return 0;
}



int CalculateCountDynamic(std::string *pCaseIn)
{
	int i, j;
	int lenWelcome = strlen(g_sWelcome);
	int lenCaseIn = pCaseIn->length();

	UINT **pRlt = New2DimInt(lenWelcome, lenCaseIn);
	UINT **pRltEx = New2DimInt(lenWelcome, lenCaseIn);


	for(i=lenWelcome-1; i>=0; i--)
	{
		for(j=lenCaseIn-1; j>=0; j--)
		{
			if(i==lenWelcome-1)
			{
				pRlt[j][i]=0;
				if(j==lenCaseIn-1)
				{
					if(pCaseIn->c_str()[j]==g_sWelcome[i])
					{
						pRlt[j][i]++;
						
					}
				}
				else
				{
					pRlt[j][i]=pRlt[j+1][i];
					if(pCaseIn->c_str()[j]==g_sWelcome[i])
					{
						pRlt[j][i]++;
						//if(pRlt[j+1][i]!=0)	pRlt[j][i] = pRlt[j][i]*pRlt[j+1][i];
					}
				}
				pRltEx[j][i] = pRlt[j][i];
				
			}
			else
			{
				if(j==lenCaseIn-1)
				{
					pRlt[j][i]=0;

					/*
					if(pRlt[j][i+1])
					{
						if(pCaseIn->c_str()[j]==g_sWelcome[i])
						{
							pRlt[j][i]++;
							//pRlt[j][i] = pRlt[j][i]*pRlt[j+1][i];

						}
					}*/

					pRltEx[j][i] = pRlt[j][i];

				}
				else
				{
					pRlt[j][i]=pRlt[j+1][i];
					pRltEx[j][i] = pRltEx[j+1][i];
					if(pRlt[j+1][i+1]>0)
					{
						if(pCaseIn->c_str()[j]==g_sWelcome[i])
						{
							pRlt[j][i]++;
							//pRltEx[j][i] = pRlt[j][i]*pRltEx[j+1][i+1];
							pRltEx[j][i] += pRltEx[j+1][i+1];
							//if(pRlt[j+1][i]!=0)	pRlt[j][i] = pRlt[j][i]*pRlt[j+1][i];
							

						}
					}
					else
					{
						pRlt[j][i]=0;
						pRltEx[j][i]=0;
					}
				}
			}
			
		}
	}



	/*
	for(i=0; i<lenWelcome; i++)
	{
		for(j=0; j<lenCaseIn; j++)
		{
			printf("%d ", pRltEx[j][i]);
		}
		printf("\n");
	}
	printf("\n");
	for(i=0; i<lenWelcome; i++)
	{
		for(j=0; j<lenCaseIn; j++)
		{
			printf("%d ", pRlt[j][i]);
		}
		printf("\n");
	}
	*/

	g_numFind = pRltEx[0][0]%10000;
	//if(g_numFind<0)g_numFind=0;


	Release2DimInt(pRlt, lenWelcome, lenCaseIn);
	Release2DimInt(pRltEx, lenWelcome, lenCaseIn);
	return g_numFind;
}

int CalculateCount(std::string *pCaseIn)
{
	//int rlt=0;
	int lenWelcome = strlen(g_sWelcome);
	int lenCaseIn = pCaseIn->length();

	int posW = 0;
	int posC = 0;

	g_numFind=0;

	FindString(posW, posC, pCaseIn, lenWelcome, lenCaseIn);

	return g_numFind;
}

void FindString(int posW, int posC, std::string * pCaseIn, int lenWelcome, int lenCaseIn)
{
	if(posW>=lenWelcome)
	{
		g_numFind++;
		return;
	}
	if(posC>=lenCaseIn)
	{
		return;
	}

	int posF = pCaseIn->find(g_sWelcome[posW], posC);

	//printf("%c posF=%d \n", g_sWelcome[posW], posF);

	while(posF!=-1)
	{
		FindString(posW+1, posF+1, pCaseIn, lenWelcome, lenCaseIn);

		posF = pCaseIn->find(g_sWelcome[posW], posF+1);
	}
}

UINT **New2DimInt(int numx, int numy)
{
	UINT**pDim2 = NULL;
	pDim2 = new UINT*[numy];
	for(int i=0; i<numy; i++)
	{
		pDim2[i] = new UINT[numx];
		//memset(pDim2[i], 0, numx*4);
		for(int j=0; j<numx; j++)
		{
			pDim2[i][j] = 0;
		}
	}

	return pDim2;
}

void Release2DimInt(UINT **pDim, int numx, int numy)
{
	for(int i=0; i<numy; i++)
	{
		delete [] pDim[i];
	}

	delete [] pDim;
}