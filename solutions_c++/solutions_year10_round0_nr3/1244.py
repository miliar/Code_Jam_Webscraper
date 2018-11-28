#include <iostream>
#include "stdio.h"
#include <map>
using namespace std;

//#define DBGOUT printf
void DBGOUT(...) { } 

typedef map<int, int> MapInt;
typedef map<int, int>::iterator MapIntIt;
typedef map<int, MapInt*> MapTable;
typedef map<int, MapInt*>::iterator MapTableIt;

MapTable	rvTable; 		// for memory
unsigned long vv[20000]; 	// for memory
int vvc;

unsigned long gg[2000];
unsigned long RR, kk, NN;

int findResult(int s, int e)
{
	MapInt	*pList;
	int v;

	if (pList = rvTable[s])
		if (v = (*pList)[e])
			return v;

	return 0;
}

int storeResult(int s, int e, int v)
{
	MapInt	*pList;

	pList = rvTable[s];
	if (!pList)
	{
		pList = new MapInt;
		rvTable[s] = pList;
	}

	if ((*pList)[e] == 0)
		(*pList)[e] = v;

	return 0;
}

void clearStoredResult()
{
	MapTableIt	tit;

//	printf("Clear\n");
	for(tit = rvTable.begin(); tit != rvTable.end(); tit++)
	{
		MapInt*		pList = (*tit).second;
		MapIntIt	it;

//		for(it = pList->begin(); it != pList->end(); it++)
//			cout <<  (*it).first << endl;

		delete pList;
	}
	rvTable.clear();
}

unsigned long findSolution()
{
	unsigned long ret = 0;

	int i, j;
	int cur = 0;
	int start = 0;
	int end = 0;
	unsigned long people = 0;
	int jump = 0;

	// check sum of people
	unsigned long tmp = 0;
	for (j = 0; j < NN; j++)
		tmp += gg[j];

	if (tmp < kk)
		return tmp * RR;

	// go
	for (i = 0; i < RR; i++)
	{
		DBGOUT("Round:%09d ", i+1);

		people = 0;
		start = cur;

		for (j = 0; j < NN; j++)
		{
			if (people + gg[cur] > kk)
				break;

			people += gg[cur];
			DBGOUT("[%lu]", gg[cur]);
			end = cur;
			cur = (cur + 1) % NN;
		}
		DBGOUT(" = %lu, total=%lu\n", people,ret);

		if (i < 20000)
			vv[i] = people;

		if (!jump)
		{
			if (findResult(start, end) > 0)
			{
				// detect loop
				DBGOUT("detect loop ");
				int ii = findResult(start, end) - 1;
				if (ii < i && i < 20000)
				{
					int k;
					unsigned long partTot = 0;
	
					jump = 1;
					// ex) ii = 110, i = 120, R= 9990
					int loop = (RR - i) / (i - ii);
					if (loop > 0)
					{
						for (k = ii; k < i ; k++)
							partTot += vv[k];
						DBGOUT("ii=%d,i=%d,parTot=%lu\n", ii, i, partTot);

						DBGOUT("loop jump %d\n", loop);
						ret += partTot * loop;
						i += loop * (i - ii) - 1;
						cur = start;
						continue;
					}
				}
			}
			else
				storeResult(start, end, i + 1);
		}

		ret += people;
	}

	// clear memory table
	clearStoredResult();	

	return ret;
}

int main()
{
	int caseCount;
	int i,j;

	scanf("%d", &caseCount);
	for (i = 0; i < caseCount; i++)
	{
		scanf("%lu %lu %lu", &RR, &kk, &NN);
		memset(gg, 0, sizeof(unsigned long)*2000);
		for (j = 0; j < NN; j++)
			scanf("%lu", &gg[j]);

		printf("Case #%d: ", i+1);
		DBGOUT("\n");
		printf("%lu\n", findSolution());


	}
}




