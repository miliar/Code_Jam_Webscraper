#include <string>
#include <limits>
#include <cstdlib>
#include <iostream>
using namespace std;
#define MAXENGINES 100
#define MAXQUERIES 1000

string engines[MAXENGINES];
string queries[MAXQUERIES];
int A[MAXENGINES][MAXQUERIES];

int main()
{
	int nCases;
	int nEngines;
	int nQueries;
	int c,i,j,k;
	int minSwitches;
	int INF = numeric_limits<int>::max();
	string param;
	getline(cin,param);
	nCases = atoi(param.c_str());
	for (c = 1; c <= nCases; c ++)
	{
		getline(cin,param);
		nEngines = atoi(param.c_str());
		for (i = 0; i < nEngines; i ++)
		{
			getline(cin,engines[i]);
		}
		getline(cin,param);
		nQueries = atoi(param.c_str());
		for (i = 0; i < nQueries;i ++)
		{
			getline(cin,queries[i]);
		}
		for (i = 0; i < nEngines; i ++)
		{
			if(queries[0] != engines[i])
				A[i][0] = 0;
			else
				A[i][0] = -1;
		}
		for (j = 0; j < nQueries; j ++)
		{
			for (i = 0; i < nEngines; i ++)
			{
				if (queries[j] == engines[i])
				{
					A[i][j] = -1;
				}
				else
				{
					minSwitches = INF;
					for (k = 0; k < nEngines; k ++)
					{
						if(A[k][j-1] == -1)
							continue;
						if(k != i)
						{
							if((A[k][j-1]+1)<minSwitches)
								minSwitches = A[k][j-1]+1;
						}
						else
						{
							if (A[k][j-1] < minSwitches)
								minSwitches = A[k][j-1];
						}
					}
					A[i][j] = minSwitches;
				}
			}
		}
		if(nQueries == 0)
			minSwitches = 0;
		else
		{
			minSwitches = INF;
			for (i = 0; i < nEngines; i ++)
			{
				if (A[i][nQueries-1] != -1 && A[i][nQueries-1] < minSwitches)
				{
					minSwitches = A[i][nQueries-1];
				}
			}
		}
		cout <<"Case #" << c << ": " << minSwitches << endl;
	}
	return 0;
}