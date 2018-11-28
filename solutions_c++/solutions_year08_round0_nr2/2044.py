#include <stdio.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define SMALL 0	//bool: is small set?

#if SMALL>0
#define N_MAX 20
#define FIN "B-small.in"
#define FOUT "B-small.out"
#else
#define N_MAX 100
#define FIN "B-large.in"
#define FOUT "B-large.out"
#endif

typedef struct timetable_info
{
	int	ID;
	tm tmDprt;
	tm tmArrv;
	bool GotDprt;
	bool GotArrv;
} TT_INFO;

void Init_TT_INFO(TT_INFO* pInfo);
void CalcTrip(TT_INFO* infoA, TT_INFO* infoB, int iTurnAround,
			  int iNA, int iNB, int* iResultA, int* iResultB);
bool CompareTimeArrv(TT_INFO* pInfo, TT_INFO* pCompare, int p_size, 
				 int iTurnAround, int* iResult);

void main()
{
	TT_INFO infoA[N_MAX] = {0}, infoB[N_MAX] = {0};
	int iNum = 0, iLimit = 0, iTurnAround = 0;
	int iNA = 0, iNB = 0, iResultA = 0, iResultB = 0;
	FILE* fIn = fopen(FIN,"r");
	FILE* fOut = fopen(FOUT,"w");
	fscanf(fIn, "%d", &iLimit);
	while(iLimit)
	{
		iNum++;
		fscanf(fIn,"%d", &iTurnAround);
		fscanf(fIn,"%d %d", &iNA, &iNB);

		for(int i = 0; i< iNA; i++)
		{
			Init_TT_INFO(&infoA[i]);
			fscanf(fIn,"%d:%d %d:%d",
				&infoA[i].tmDprt.tm_hour, &infoA[i].tmDprt.tm_min, 
				&infoA[i].tmArrv.tm_hour, &infoA[i].tmArrv.tm_min);
		}
		for(i = 0; i< iNB; i++)
		{
			Init_TT_INFO(&infoB[i]);
			fscanf(fIn,"%d:%d %d:%d",
				&infoB[i].tmDprt.tm_hour, &infoB[i].tmDprt.tm_min, 
				&infoB[i].tmArrv.tm_hour, &infoB[i].tmArrv.tm_min);
		}

		CalcTrip(infoA, infoB, iTurnAround, iNA, iNB, &iResultA, &iResultB);
		fprintf(fOut,"Case #%d: %d %d\n", iNum, iResultA, iResultB);

		iLimit--;
	}

	fclose(fIn);
	fclose(fOut);
}

void Init_TT_INFO(TT_INFO* pInfo)
{
	tm time = {0};

	pInfo->ID = 0;
	pInfo->tmDprt = time;
	pInfo->tmArrv = pInfo->tmDprt;
	pInfo->GotArrv = pInfo->GotDprt = false;
}

void CalcTrip(TT_INFO* infoA, TT_INFO* infoB, int iTurnAround,
			  int iNA, int iNB, int* iResultA, int* iResultB)
{
	int iRA = 0, iRB = 0;

	for(int i = 0; i<iNA; i++)
	{
		if(CompareTimeArrv(&infoA[i], infoB, iNB, iTurnAround, &iRB))
			continue;
		else iRA++;
	}

	for(i = 0; i<iNB; i++)
	{
		if(CompareTimeArrv(&infoB[i], infoA, iNA, iTurnAround, &iRA))
			continue;
		else iRB++;
	}
	memcpy(iResultA, &iRA, sizeof(iRA));
	memcpy(iResultB, &iRB, sizeof(iRB));
}

bool CompareTimeArrv(TT_INFO* pInfo, TT_INFO* pCompare, int p_size, 
				 int iTurnAround, int* iResult)
{
	TT_INFO* pTemp = 0;
	int iDiff = -1;
	int t_Dprt = pInfo->tmDprt.tm_hour*60 + pInfo->tmDprt.tm_min;
	int t_Arrv = 0;

	if(pInfo->GotArrv)
		return true;

	//compare with another arrival
	for (int i = 0; i<p_size; i++)
	{
		if(pCompare[i].GotDprt)
			continue;

		t_Arrv = pCompare[i].tmArrv.tm_hour*60 + pCompare[i].tmArrv.tm_min;
		int iTime = t_Dprt - t_Arrv;
		if(iTime >= iTurnAround)
		{

			if(iDiff == -1 || iDiff > iTime)
			{
				
				iDiff = iTime;
				pTemp = &pCompare[i];
			}
			else continue;
		}
	}
	if(pTemp)
	{
		pTemp->GotDprt = pInfo->GotArrv = true;
		return true;
	}
	return false;
}