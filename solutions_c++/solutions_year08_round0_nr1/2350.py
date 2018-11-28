/*
 * Google Code Jam 2008
 * Problem 1 - Saving Universe 
 */


#include <stdio.h>
#include <map>
#include <vector>
#include <string>
#include <string.h>

#define	INPUT_FILE	"A-large.in"
#define	OUTPUT_FILE	"A-large.out"

using namespace std;


int N, S, Q;
vector<int> vQuery;
map<string, int> mapEngines;


int Search(int pos)
{
	int i, cnt = 0, flag[1000];


	for (i = 0; i < S; i++)
		flag[i] = -1;

	for (i = pos; i < vQuery.size(); i++)
	{
		if (flag[vQuery[i]] == -1)
		{
			flag[vQuery[i]] = i;
			cnt++;

			if (cnt == S)
				return vQuery[i];
		}
	}

	for (i = 0; i < S; i++)
		if (flag[i] == -1)						// nebifat
			return i;

	return -1;
}

int Solve()
{
	int i, one, sol = 0;

	one = Search(0);

	for (i = 0; i < vQuery.size(); i++)
	{
		if (vQuery[i] == one)
		{
			sol++;
			one = Search(i);
		}
	}

	return sol;
}


int main()
{
	int i, j;
	char sz[1024];


	freopen(OUTPUT_FILE, "wt", stdout);

	freopen(INPUT_FILE, "rt", stdin);

	scanf("%d\n", &N);

	for (i = 1; i <= N; i++)
	{
		vQuery.clear();
		mapEngines.clear();

		scanf("%d\n", &S);
		for (j = 0; j < S; j++)
		{
			gets(sz);

			string sEngine(sz);
			mapEngines[sEngine] = j;
		}

		scanf("%d\n", &Q);
		for (j = 0; j < Q; j++)
		{
			gets(sz);

			string sQuery(sz);
			vQuery.push_back(mapEngines[sQuery]);
		}

		printf("Case #%d: %d\n", i, Solve());
	}

	fclose(stdout);
	fclose(stdin);

	return 0;
}
