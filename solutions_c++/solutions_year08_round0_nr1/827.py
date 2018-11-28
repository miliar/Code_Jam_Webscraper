#include <stdio.h>
#include <string>
#include <vector>
using namespace std;

int g_nMinSwitch = 0x7fffffff;
int g_cost[100][1000];

int GetSwitchCount(
	vector<string> &srchEngines, 
	vector<string> &querys, 
	int nEngineIndex, 
	int nBeginPos)
{
	if (nBeginPos == querys.size())
	{
		return 0;
	}
	if (g_cost[nEngineIndex][nBeginPos] != -1)
	{
		return g_cost[nEngineIndex][nBeginPos];
	}

	if (srchEngines[nEngineIndex] != querys[nBeginPos])
	{
		return GetSwitchCount(srchEngines, querys, nEngineIndex, nBeginPos+1);
	}
	else
	{
		int nMinSwitchCount = 0x7fffffff;
		for (int i=0; i<srchEngines.size(); i++)
		{
			if (i != nEngineIndex)
			{
				int nSwitchCount = GetSwitchCount(srchEngines, querys, i, nBeginPos+1)+1;
				if (nSwitchCount < nMinSwitchCount)
				{
					nMinSwitchCount = nSwitchCount;
				}
			}
		}
		
		g_cost[nEngineIndex][nBeginPos] = nMinSwitchCount;
		return nMinSwitchCount;		
	}
}


int main(int argc, char **argv)
{
	char szEngineName[256];
	char szQuery[256];

	vector<string> srchEngines;
	vector<string> inputs;
	vector<string> querys;

	int nSwitchNum = 0;

	FILE *fp = fopen(argv[1], "rt");

	int N = 1;
	fscanf(fp, "%d", &N);

	for (int nCase=0; nCase<N; nCase++)
	{
		srchEngines.clear();
		inputs.clear();
		querys.clear();

		int nEngineNum = 0;
		fscanf(fp, "%d\n", &nEngineNum);
		for (int i=0; i<nEngineNum; i++)
		{
			fgets(szEngineName, 256, fp);
			srchEngines.push_back(szEngineName);
		}

		int nQueryNum = 0;
		fscanf(fp, "%d\n", &nQueryNum);
		for (int i=0; i<nQueryNum; i++)
		{
			fgets(szQuery, 256, fp);
			inputs.push_back(szQuery);
		}

		for (int i=0; i<inputs.size(); i++)
		{
			if (querys.empty() || querys[querys.size()-1] != inputs[i])
			{
				querys.push_back(inputs[i]);
			}
		}

		for (int i=0; i<srchEngines.size(); i++)
		{
			for (int j=0; j<querys.size(); j++)
			{
				g_cost[i][j] = -1;
			}
		}

		g_nMinSwitch = 0x7fffffff;
		for (int i=0; i<srchEngines.size(); i++)
		{
			int nMinSwitch = GetSwitchCount(srchEngines, querys, i, 0);

			if (g_nMinSwitch > nMinSwitch)
			{
				g_nMinSwitch = nMinSwitch;
			}
		}

		printf("Case #%d: %d\n", nCase+1, g_nMinSwitch);
		g_nMinSwitch = 0x7fffffff;
	}


	fclose(fp);
	return 0;
}