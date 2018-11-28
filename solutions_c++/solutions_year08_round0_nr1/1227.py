#include "stdafx.h"
#include "math.h"
#include "string.h"
#include "stdlib.h"
#include "stdio.h"
#include <vector>
#include <algorithm>
using namespace std;

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
	int i = 0;
	for (i = 0; i < nCaseNum; i++)
	{
		fgets(strLine, nMaxLineBuf, fp);
		int nEngineNum = atoi(strLine);
		vector <string> engineNames;
		vector <string> queryNames;
		int j = 0;
		for (j = 0; j < nEngineNum; j++)
		{
			fgets(strLine, nMaxLineBuf, fp);
			string tmp = strLine;
			engineNames.push_back(tmp);
		}

		fgets(strLine, nMaxLineBuf, fp);
		int nQueryNum = atoi(strLine);
		for (j = 0; j < nQueryNum; j++)
		{
			fgets(strLine, nMaxLineBuf, fp);
			string tmp = strLine;
			queryNames.push_back(tmp);
		}

		int nSwitch = 0;
		vector <string> tmpEngineNames;
		tmpEngineNames.clear();
		tmpEngineNames = engineNames;
		for (vector <string>::iterator itq = queryNames.begin(); itq != queryNames.end(); itq++)
		{
			for (vector <string>::iterator ite = tmpEngineNames.begin(); ite != tmpEngineNames.end(); ite++)
			{
				//printf("??? group candidate ??? %s", ((string)*ite).c_str());
				if(!((string)*ite).compare((string)*itq) )
				{
					tmpEngineNames.erase(ite);
					int nTempEngineSize = tmpEngineNames.size();
					if (nTempEngineSize == 1)
					{
						//printf("!!! group leader !!! %s", tmpEngineNames.front().c_str());
					}
					else if (nTempEngineSize == 0)
					{
						nSwitch++;
						tmpEngineNames.clear();
						tmpEngineNames = engineNames;
						itq--;
						//printf("==== group ====\n");
					}
					break;
				}
			}
			//printf("%s", ((string)*itq).c_str());
		}
		//printf("Case #%d: %d\n\n\n\n", i+1, nSwitch);
		fprintf(fp2, "Case #%d: %d\n", i+1, nSwitch);
	}
	fclose(fp);
	fclose(fp2);
	return 0;
}

