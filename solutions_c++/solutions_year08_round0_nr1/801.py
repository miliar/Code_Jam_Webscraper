#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE *fpIn;
	FILE *fpOut;

	fpIn = fopen("A-large.in", "r");
	//for debug : beign
	//if(NULL == fpIn)
	//	printf("fail to call fopen(\"A-small.in\", \"r\")");
	//for debug : end
	fpOut = fopen("A-large.out", "wb");

	int nCaseNum;
	char szCaseNum[10];
	fgets(szCaseNum, 10, fpIn);
	szCaseNum[strlen(szCaseNum) - 1] = '\0';
	nCaseNum = atoi(szCaseNum);



	int *nOutput;
	nOutput = (int *)malloc(sizeof(int) * nCaseNum);

	int nCount0;
	for(nCount0 = 0; nCount0 < nCaseNum; nCount0++)
	{
		int nEngineNum;
		char szEngineNum[10];
		fgets(szEngineNum, 10, fpIn);
		szEngineNum[strlen(szEngineNum) - 1] = '\0';
		nEngineNum = atoi(szEngineNum);
		// for debug : begin
		//printf("nEngineNum = %d\n", nEngineNum);
		// for debug : end
		
		char *szEngineName;
		szEngineName = (char *)malloc( sizeof(char) * 128 * nEngineNum);
		
		int nTemp0;
		for(nTemp0 = 0; nTemp0 < nEngineNum; nTemp0++)
		{
			fgets(&szEngineName[128 * nTemp0], 128, fpIn);
			int nTemp1 = strlen(&szEngineName[128 * nTemp0]);
			szEngineName[128 * nTemp0 + nTemp1 - 1] = '\0';
			// for debug : begin
			//printf("len = %d\n", strlen(&szEngineName[128 * nTemp0]));
			// for debug : end
		}

		int *aEngineFlag;
		aEngineFlag = (int *)malloc(sizeof(int) * nEngineNum);

		for(nTemp0 = 0; nTemp0 < nEngineNum; nTemp0++)
		{
			aEngineFlag[nTemp0] = 0;
		}

		int nQueryNum;
		char szQueryNum[10];
		fgets(szQueryNum, 10, fpIn);
		szQueryNum[strlen(szQueryNum) - 1] = '\0';
		nQueryNum = atoi(szQueryNum);

		int nCount1;
		int nSwitch = 0;
		int nHitEngineNum = 0;
		for(nCount1 = 0; nCount1 < nQueryNum; nCount1++)
		{
			char szQueryName[128];
			fgets(szQueryName, 128, fpIn);
			int nTemp1 = strlen(szQueryName);
			szQueryName[nTemp1 - 1] = '\0';

			for(nTemp1 = 0; nTemp1 < nEngineNum; nTemp1++)
			{
				if(0 == strcmp(szQueryName, &szEngineName[128 * nTemp1]) )
				{
					if(aEngineFlag[nTemp1] == 0)
					{
						aEngineFlag[nTemp1] = 1;
						nHitEngineNum++;
					}
					break;
				}
			}

			if(nHitEngineNum >= nEngineNum)
			{
				nSwitch++;
				int nTemp2;
				for(nTemp2 = 0; nTemp2 < nEngineNum; nTemp2++)
				{
					aEngineFlag[nTemp2] = 0;
				}
				aEngineFlag[nTemp1] = 1;
				nHitEngineNum = 1;
			}
		} // END : for(nCount1 = 0; nCount1 < nQueryNum; nCount1++)

		nOutput[nCount0] = nSwitch;

		free(szEngineName);
		free(aEngineFlag);
	} // END : for(nCount0 = 0; nCount0 < nCaseNum; nCount0++)

	for(nCount0 = 0; nCount0 < nCaseNum; nCount0++)
	{
		char szOutput[50];
		sprintf(szOutput, "Case #%d: %d\n", nCount0 + 1, nOutput[nCount0]);	
		fwrite(szOutput, sizeof(char), strlen(szOutput), fpOut);
	}

	fclose(fpIn);
	fclose(fpOut);

	return 0;
}