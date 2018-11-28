#include "stdafx.h"
#include "math.h"
#include "string.h"
#include "stdlib.h"
#include "stdio.h"
#include <vector>
#include <algorithm>
using namespace std;

struct TripSched{
	int nStart;
	int nEnd;
};

bool smallStartTime(TripSched elem1, TripSched elem2)
{
	return elem1.nStart <= elem2.nStart;
}

bool smallEndTime(TripSched elem1, TripSched elem2)
{
	return elem1.nEnd <= elem2.nEnd;
}

void arrange(bool bStartFromA, TripSched sched, int nTurnAround, int &nNeedA, int &nNeedB, int &nAvaA, int &nAvaB, vector <TripSched> & onTripAB, vector <TripSched> & onTripBA)
{
	if (bStartFromA)
	{
		sort(onTripBA.begin(), onTripBA.end(), smallEndTime);
		if (!onTripBA.empty() && onTripBA.front().nEnd + nTurnAround <= sched.nStart)
		{
			onTripBA.erase(onTripBA.begin());
			nAvaA ++;
		}
		if (nAvaA)
		{
			nAvaA --;
		}
		else
		{
			nNeedA ++;
		}
	}
	else
	{
		sort(onTripAB.begin(), onTripAB.end(), smallEndTime);
		if (!onTripAB.empty() && onTripAB.front().nEnd + nTurnAround <= sched.nStart)
		{
			onTripAB.erase(onTripAB.begin());
			nAvaB ++;
		}
		if (nAvaB)
		{
			nAvaB --;
		}
		else
		{
			nNeedB ++;
		}
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp;
	FILE *fp2;
	char strFilename1[_MAX_FNAME] = {0};
	char strFilename2[_MAX_FNAME] = {0};
	if (argc >= 2)
	{
		strcpy(strFilename1, argv[1]);
		sprintf(strFilename2, "r_%s", strFilename1);
	}
	else
	{
		strcpy(strFilename1, "test.in");
		strcpy(strFilename2, "r_test.in");
	}
	fp=fopen(strFilename1, "r");
	fp2=fopen(strFilename2, "w");

	const int nMaxLineBuf = 1024;
	char strLine[nMaxLineBuf+1]={0};
	fgets(strLine, nMaxLineBuf, fp);

	int nCaseNum = atoi(strLine);
	int i;
	for (i = 0; i < nCaseNum; i++)
	{
		fgets(strLine, nMaxLineBuf, fp);
		int nTurnAroundTime = atoi(strLine);
		fgets(strLine, nMaxLineBuf, fp);
		int nSchedAB = 0;
		int nSchedBA =0;
		sscanf(strLine, "%d %d", &nSchedAB, &nSchedBA);

		vector <TripSched> schedAB;
		vector <TripSched> schedBA;
		vector <TripSched> onTripAB;
		vector <TripSched> onTripBA;
		// parse input
		int j;
		int startH = 0;
		int startM = 0;
		int endH = 0;
		int endM = 0;
		for (j = 0; j < nSchedAB; j++)
		{
			fgets(strLine, nMaxLineBuf, fp);
			sscanf(strLine, "%d:%d %d:%d", &startH, &startM, &endH, &endM);
			TripSched tmp;
			tmp.nStart = 60*startH + startM;
			tmp.nEnd = 60*endH + endM;
			schedAB.push_back(tmp);
		}
		for (j = 0; j < nSchedBA; j++)
		{
			fgets(strLine, nMaxLineBuf, fp);
			sscanf(strLine, "%d:%d %d:%d", &startH, &startM, &endH, &endM);
			TripSched tmp;
			tmp.nStart = 60*startH + startM;
			tmp.nEnd = 60*endH + endM;
			schedBA.push_back(tmp);
		}
		

		sort(schedAB.begin(), schedAB.end(), smallStartTime);
		sort(schedBA.begin(), schedBA.end(), smallStartTime);

//		for (j = 0; j < nSchedAB; j++)
//		{
//			printf("%d->%d\n", schedAB.at(j).nStart,  schedAB.at(j).nEnd);
//		}
//		for (j = 0; j < nSchedBA; j++)
//		{
//			printf("%d->%d\n", schedBA.at(j).nStart,  schedBA.at(j).nEnd);
//		}

		int nNeedA = 0;
		int nAvaA = nNeedA;
		int nNeedB = 0;
		int nAvaB = nNeedB;
		int nSizeAB = schedAB.size();
		int nSizeBA = schedBA.size();
		while(nSizeAB || nSizeBA)
		{
			if (!nSizeAB)
			{
				TripSched ba = schedBA.front();
				arrange(false, ba, nTurnAroundTime, nNeedA, nNeedB, nAvaA, nAvaB, onTripAB, onTripBA);
				onTripBA.push_back(ba);
				schedBA.erase(schedBA.begin());
			}
			else if (!nSizeBA)
			{
				TripSched ab = schedAB.front();
				arrange(true, ab, nTurnAroundTime, nNeedA, nNeedB, nAvaA, nAvaB, onTripAB, onTripBA);
				onTripAB.push_back(ab);
				schedAB.erase(schedAB.begin());
			}
			else
			{
				TripSched ab;
				TripSched ba;
				ab = schedAB.front() ;
				ba = schedBA.front();
				if (ab.nStart <= ba.nStart)
				{
					arrange(true, ab, nTurnAroundTime, nNeedA, nNeedB, nAvaA, nAvaB, onTripAB, onTripBA);
					onTripAB.push_back(ab);
					schedAB.erase(schedAB.begin());
				}
				else
				{
					arrange(false, ba, nTurnAroundTime, nNeedA, nNeedB, nAvaA, nAvaB, onTripAB, onTripBA);
					onTripBA.push_back(ba);
					schedBA.erase(schedBA.begin());
				}
			}
			nSizeAB = schedAB.size();
			nSizeBA = schedBA.size();
		}
		fprintf(fp2, "Case #%d: %d %d\n", i+1, nNeedA, nNeedB);
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}

