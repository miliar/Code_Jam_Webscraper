#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct TIMENODE
{
	int nBeginTime;
	int nEndTime;
	int nBeUsed; 
	int nHasTrain; 
}STimeNode;

typedef struct TRAINNUM
{
	int nTrainA;
	int nTrainB;
}STrainNum;

int main()
{
	FILE *fpIn;
	FILE *fpOut;

	fpIn = fopen("B-large.in", "r");
	fpOut = fopen("B-large.out", "wb");

	int nCaseNum;
	char szCaseNum[10];
	fgets(szCaseNum, 10, fpIn);
	szCaseNum[strlen(szCaseNum) - 1] = '\0';
	nCaseNum = atoi(szCaseNum);

	STrainNum *psTrainNum;
	psTrainNum = (STrainNum *)malloc(sizeof(STrainNum) * nCaseNum);

	int nCount0;
	for(nCount0 = 0; nCount0 < nCaseNum; nCount0++)
	{
		int nTurnAroundTime;
		char szTurnAroundTime[10];
		fgets(szTurnAroundTime, 10, fpIn);
		szTurnAroundTime[strlen(szTurnAroundTime) - 1] = '\0';
		nTurnAroundTime = atoi(szTurnAroundTime);

		int nA;
		int nB;
		char szAB[20];
		fgets(szAB, 20, fpIn);
		szAB[strlen(szAB) - 1] = '\0';
		sscanf(szAB, "%d %d", &nA, &nB);

		STimeNode *psTimeNodeA, *psTimeNodeB;
		psTimeNodeA = (STimeNode *)malloc(sizeof(STimeNode) * nA);
		psTimeNodeB = (STimeNode *)malloc(sizeof(STimeNode) * nB);

		int nTemp0;
		for(nTemp0 = 0; nTemp0 < nA; nTemp0++)
		{
			char szTimeNode[20];
			fgets(szTimeNode, 20, fpIn);
			szTimeNode[strlen(szTimeNode) - 1] = '\0';
			int nBeginHour;
			int nBeginMinute;
			int nEndHour;
			int nEndMinute;
			sscanf(szTimeNode, "%d:%d %d:%d", &nBeginHour, &nBeginMinute, &nEndHour, &nEndMinute);
			// for debug : begin
			//printf("%d:%d  %d:%d\n", nBeginHour, nBeginMinute, nEndHour, nEndMinute);
			// for debug : end
			psTimeNodeA[nTemp0].nBeginTime = nBeginHour * 60 + nBeginMinute;
			psTimeNodeA[nTemp0].nEndTime = nEndHour * 60 + nEndMinute;
			psTimeNodeA[nTemp0].nBeUsed = 0;
			psTimeNodeA[nTemp0].nHasTrain = 1;
		}

		for(nTemp0 = 0; nTemp0 < nB; nTemp0++)
		{
			char szTimeNode[20];
			fgets(szTimeNode, 20, fpIn);
			szTimeNode[strlen(szTimeNode) - 1] = '\0';
			int nBeginHour;
			int nBeginMinute;
			int nEndHour;
			int nEndMinute;
			sscanf(szTimeNode, "%d:%d %d:%d", &nBeginHour, &nBeginMinute, &nEndHour, &nEndMinute);
			// for debug : begin
			//printf("%d:%d  %d:%d\n", nBeginHour, nBeginMinute, nEndHour, nEndMinute);
			// for debug : end
			psTimeNodeB[nTemp0].nBeginTime = nBeginHour * 60 + nBeginMinute;
			psTimeNodeB[nTemp0].nEndTime = nEndHour * 60 + nEndMinute;
			psTimeNodeB[nTemp0].nBeUsed = 0;
			psTimeNodeB[nTemp0].nHasTrain = 1;
		}

		for(nTemp0 = 0; nTemp0 < nA; nTemp0++)
		{
			int nTemp1 =  0;
			for(nTemp1 = 0; nTemp1 < nA - 1 - nTemp0; nTemp1++)
			{
				if(psTimeNodeA[nTemp1].nEndTime > psTimeNodeA[nTemp1 + 1].nEndTime)
				{
					STimeNode sTemp;
					sTemp.nBeginTime = psTimeNodeA[nTemp1].nBeginTime;
					sTemp.nEndTime = psTimeNodeA[nTemp1].nEndTime;
					sTemp.nBeUsed = psTimeNodeA[nTemp1].nBeUsed;
					sTemp.nHasTrain = psTimeNodeA[nTemp1].nHasTrain;

					psTimeNodeA[nTemp1].nBeginTime = psTimeNodeA[nTemp1 + 1].nBeginTime;
					psTimeNodeA[nTemp1].nEndTime = psTimeNodeA[nTemp1 + 1].nEndTime;
					psTimeNodeA[nTemp1].nBeUsed = psTimeNodeA[nTemp1 + 1].nBeUsed;
					psTimeNodeA[nTemp1].nHasTrain = psTimeNodeA[nTemp1 + 1].nHasTrain;

					psTimeNodeA[nTemp1 + 1].nBeginTime = sTemp.nBeginTime;
					psTimeNodeA[nTemp1 + 1].nEndTime = sTemp.nEndTime;
					psTimeNodeA[nTemp1 + 1].nBeUsed = sTemp.nBeUsed;
					psTimeNodeA[nTemp1 + 1].nHasTrain = sTemp.nHasTrain;
				}
			}
		} // END : for(nTemp0 = 0; nTemp0 < nA; nTemp0++)

		for(nTemp0 = 0; nTemp0 < nB; nTemp0++)
		{
			int nTemp1 =  0;
			for(nTemp1 = 0; nTemp1 < nB - 1 - nTemp0; nTemp1++)
			{
				if(psTimeNodeB[nTemp1].nEndTime > psTimeNodeB[nTemp1 + 1].nEndTime)
				{
					STimeNode sTemp;
					sTemp.nBeginTime = psTimeNodeB[nTemp1].nBeginTime;
					sTemp.nEndTime = psTimeNodeB[nTemp1].nEndTime;
					sTemp.nBeUsed = psTimeNodeB[nTemp1].nBeUsed;
					sTemp.nHasTrain = psTimeNodeB[nTemp1].nHasTrain;

					psTimeNodeB[nTemp1].nBeginTime = psTimeNodeB[nTemp1 + 1].nBeginTime;
					psTimeNodeB[nTemp1].nEndTime = psTimeNodeB[nTemp1 + 1].nEndTime;
					psTimeNodeB[nTemp1].nBeUsed = psTimeNodeB[nTemp1 + 1].nBeUsed;
					psTimeNodeB[nTemp1].nHasTrain = psTimeNodeB[nTemp1 + 1].nHasTrain;

					psTimeNodeB[nTemp1 + 1].nBeginTime = sTemp.nBeginTime;
					psTimeNodeB[nTemp1 + 1].nEndTime = sTemp.nEndTime;
					psTimeNodeB[nTemp1 + 1].nBeUsed = sTemp.nBeUsed;
					psTimeNodeB[nTemp1 + 1].nHasTrain = sTemp.nHasTrain;
				}
			}
		}// END : for(nTemp0 = 0; nTemp0 < nB; nTemp0++)

		//for debug : begin
		/*
		printf("case #%d\n", nCount0);
		for(nTemp0 = 0; nTemp0 < nA; nTemp0++)
		{
			printf("nBeginTime = %d, nEndTime = %d, nBeUsed = %d, nHasTrain = %d\n",
				psTimeNodeA[nTemp0].nBeginTime, psTimeNodeA[nTemp0].nEndTime,
				psTimeNodeA[nTemp0].nBeUsed, psTimeNodeA[nTemp0].nHasTrain);
		}
		for(nTemp0 = 0; nTemp0 < nB; nTemp0++)
		{
			printf("nBeginTime = %d, nEndTime = %d, nBeUsed = %d, nHasTrain = %d\n",
				psTimeNodeB[nTemp0].nBeginTime, psTimeNodeB[nTemp0].nEndTime,
				psTimeNodeB[nTemp0].nBeUsed, psTimeNodeB[nTemp0].nHasTrain);
		}
		*/
		//for debug : end

		
		for(nTemp0 = 0; nTemp0 < nB; nTemp0++)
		{
			int nBeginTimeB = psTimeNodeB[nTemp0].nBeginTime;
			int nTemp1;
			int nPointer = -1;
			int nBreakFlag = 0;
			for(nTemp1 = nA - 1; nTemp1 >= 0; nTemp1--)
			{
				if(psTimeNodeA[nTemp1].nBeUsed == 0) // 该火车未被B站使用
				{
					if(psTimeNodeA[nTemp1].nEndTime + nTurnAroundTime <= nBeginTimeB)
					{
						nPointer = nTemp1;
						nBreakFlag = 1;
					}
				}

				if(nBreakFlag > 0)
					break;
			}

			if(nPointer != -1)
			{
				psTimeNodeA[nPointer].nBeUsed = 1;
				psTimeNodeB[nTemp0].nHasTrain = 0;
			}
		}

		for(nTemp0 = 0; nTemp0 < nA; nTemp0++)
		{
			int nBeginTimeA = psTimeNodeA[nTemp0].nBeginTime;
			int nTemp1;
			int nPointer = -1;
			int nBreakFlag = 0;
			for(nTemp1 = nB - 1; nTemp1 >= 0; nTemp1--)
			{
				if(psTimeNodeB[nTemp1].nBeUsed == 0) // 该火车未被A站使用
				{
					if(psTimeNodeB[nTemp1].nEndTime + nTurnAroundTime <= nBeginTimeA)
					{
						nPointer = nTemp1;
						nBreakFlag = 1;
					}
				}

				if(nBreakFlag > 0)
					break;
			}

			if(nPointer != -1)
			{
				psTimeNodeB[nPointer].nBeUsed = 1;
				psTimeNodeA[nTemp0].nHasTrain = 0;
			}
		}

		int nTrainA = 0;
		for(nTemp0 = 0; nTemp0 < nA; nTemp0++)
		{
			nTrainA = nTrainA + psTimeNodeA[nTemp0].nHasTrain;
		}

		int nTrainB = 0;
		for(nTemp0 = 0; nTemp0 < nB; nTemp0++)
		{
			nTrainB = nTrainB + psTimeNodeB[nTemp0].nHasTrain;
		}

		psTrainNum[nCount0].nTrainA = nTrainA;
		psTrainNum[nCount0].nTrainB = nTrainB;
		
		free(psTimeNodeA);
		free(psTimeNodeB);

	} // END : for(nCount0 = 0; nCount0 < nCaseNum; nCount0++)

	
	for(nCount0 = 0; nCount0 < nCaseNum; nCount0++)
	{
		char szOutput[50];
		sprintf(szOutput, "Case #%d: %d %d\n", nCount0 + 1, psTrainNum[nCount0].nTrainA, psTrainNum[nCount0].nTrainB);	
		fwrite(szOutput, sizeof(char), strlen(szOutput), fpOut);
	}

	free(psTrainNum);

	fclose(fpIn);
	fclose(fpOut);

	return 0;
}