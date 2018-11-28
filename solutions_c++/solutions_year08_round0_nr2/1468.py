#include "stdio.h"
#include "string"

using namespace std;

class CTrainEntry
{
public:
	int time;
	int station;
	bool isArr;
};


void SwapTrn(CTrainEntry** a, CTrainEntry** b)
{
	CTrainEntry* t = NULL;
	if( (*a)->time >  (*b)->time) 
	{
		t = *a;
		*a = *b;
		*b = t;
	}
	else if( (*a)->time ==  (*b)->time) 
	{
		if( !(*a)->isArr && (*b)->isArr) 
		{
			t = *a;
			*a = *b;
			*b = t;
		}
	}
}


int main()
{

	FILE* fp = NULL;
	fp = fopen("Download B-small.in","ra");
	
	char sInput[100];
	int inTestCase = 0;

	fgets(sInput, 100, fp);
	inTestCase = atoi(sInput);


	for(int i = 0; i < inTestCase; i++)
	{
		fgets(sInput, 100, fp);
		int iTurnTime = atoi(sInput);
		
		char str[102];
		str[101] = NULL;
		fgets(str,101, fp);
		
		int nA, nB, arrH, arrM, depH, depM;
		sscanf(str, "%d %d", &nA, &nB);

		CTrainEntry** pTrn = new CTrainEntry*[(nA+nB)*2];
		int iTrnEntry = 0;

		for(int j = 0; j < nA; j++)
		{
			fgets(str,101, fp);
			sscanf(str, "%d:%d %d:%d", &depH, &depM, &arrH, &arrM);
			
			pTrn[iTrnEntry] = new CTrainEntry;
			pTrn[iTrnEntry]->time = depH * 100 + depM;
			pTrn[iTrnEntry]->station = 0;
			pTrn[iTrnEntry]->isArr = false;
			iTrnEntry++;

			pTrn[iTrnEntry] = new CTrainEntry;
			arrH = arrH + (arrM+iTurnTime)/60;
			arrM = (arrM+iTurnTime)%60;
			pTrn[iTrnEntry]->time = arrH * 100 + arrM;
			pTrn[iTrnEntry]->station = 1;
			pTrn[iTrnEntry]->isArr = true;
			iTrnEntry++;
		}

		for(j = 0; j < nB; j++)
		{
			fgets(str,101, fp);
			sscanf(str, "%d:%d %d:%d", &depH, &depM, &arrH, &arrM);

			pTrn[iTrnEntry] = new CTrainEntry;
			pTrn[iTrnEntry]->time = depH * 100 + depM;
			pTrn[iTrnEntry]->station = 1;
			pTrn[iTrnEntry]->isArr = false;
			iTrnEntry++;

			pTrn[iTrnEntry] = new CTrainEntry;
			arrH = arrH + (arrM+iTurnTime)/60;
			arrM = (arrM+iTurnTime)%60;
			pTrn[iTrnEntry]->time = arrH * 100 + arrM;
			pTrn[iTrnEntry]->station = 0;
			pTrn[iTrnEntry]->isArr = true;
			iTrnEntry++;
		}

		//sort
		for(int m = 0; m < iTrnEntry; m++)
		{
			for(int n = m+1; n < iTrnEntry; n++)
			{
				SwapTrn(&pTrn[m], &pTrn[n]);	
			}
		}

		int av[2] ={0};
		int tt[2] ={0};

		for(m = 0; m < iTrnEntry; m++)
		{
			if(!pTrn[m]->isArr)
			{
				if( av[ pTrn[m]->station ] )
				{
					av[ pTrn[m]->station ]--;
				}
				else
				{
					tt[ pTrn[m]->station ]++;
				}
			}
			else
			{
				av[ pTrn[m]->station ]++;
			}
		}
		
		printf("Case #%d: %d %d\n", i+1, tt[0], tt[1]);

		for(j = 0; j < (nA+nB)*2; j++)
		{
			pTrn[j] = NULL;
			delete pTrn[j];
		}
		delete pTrn;

		pTrn = NULL;
	}

	return 0;
}
