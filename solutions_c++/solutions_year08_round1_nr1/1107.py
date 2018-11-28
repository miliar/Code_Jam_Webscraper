#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <assert.h>
using namespace std;

int g_nMinProduct = 0;
int nVec[2][800];
int g_nDim = 0;
bool g_usedFlag[2][900];

map<int, int> minProductMap;

int GenStringKey()
{
	int key = 0;
	int a[2] = {0, 0};
	

	for (int i=0; i<2; i++)
	{
		for (int j=0; j<g_nDim; j++)
		{
			if (g_usedFlag[i][j])
			{
				a[i] |= (1 << j);
			}
		}
	}

	key = (a[0] << 16) + a[1];
	
	return key;
}

int CalcMiniProduct(int nDim)
{
	if (nDim == 0)
	{
		return 0;
	}

	int key = GenStringKey();
	if (minProductMap.find(key) != minProductMap.end())
	{
		return minProductMap[key];
	}


	int minProduct = 0x7fffffff;
	for (int i=0; i<g_nDim; i++)
	{
		if (g_usedFlag[0][i])
		{
			continue;
		}
		g_usedFlag[0][i] = true;

		for (int j=0; j<g_nDim; j++)
		{
			if (g_usedFlag[1][j])
			{
				continue;
			}
			g_usedFlag[1][j] = true;			

			int product = nVec[0][i]*nVec[1][j] + CalcMiniProduct(nDim-1);
			if (product < minProduct)
			{
				minProduct = product;
			}

			g_usedFlag[1][j] = false;			
		}

		g_usedFlag[0][i] = false;
	}

	minProductMap[key] = minProduct;
	return minProduct;
}

int main(int argc, char **argv)
{
	char szVec[7000];
	char seps[]   = " ,\t\n";
	char *token = NULL;

	FILE *fp = fopen(argv[1], "rt");

	int N = 1;
	fscanf(fp, "%d\n", &N);

	for (int nCase=0; nCase<N; nCase++)
	{
		fscanf(fp, "%d\n", &g_nDim);		

		for (int i = 0; i<2; i++)
		{
			fgets(szVec, 7000, fp);

			token = strtok(szVec, seps);
			int j = 0;
			while (token != NULL)
			{
				nVec[i][j] = atoi(token);
				token = strtok( NULL, seps );
				j++;
			}

			assert(j == g_nDim);
		}
		minProductMap.clear();
		memset(g_usedFlag[0], 0, sizeof(bool) * 900);
		memset(g_usedFlag[1], 0, sizeof(bool) * 900);
		int nMinProduct = CalcMiniProduct(g_nDim);		

		printf("Case #%d: %d\n", nCase+1, nMinProduct);
	}


	fclose(fp);
	return 0;
}