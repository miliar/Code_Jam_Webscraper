#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <map>

using namespace std;

int s, q;
map<string, int> engine;
vector<string> query;
vector< vector<int> > dTable;

int solution;

void solve(void)
{
	if (q == 0)
	{
		solution = 0;
		return;
	}

	dTable.push_back(vector<int>());
	for (int i = 0 ; i < s ; ++i)
	{
		if (engine[query[0]] != i)
		{
			dTable[0].push_back(0);
		}
		else
		{
			dTable[0].push_back(-1);
		}
	}

	for (int i = 1 ; i < q ; ++i)
	{
		dTable.push_back(vector<int>());
		int qId = engine[query[i]];

		for (int j = 0 ; j < s ; ++j)
		{
			if (qId == j)
			{
				dTable[i].push_back(-1);
			}
			else
			{
				int val = -1;

				for (int k = 0 ; k < s ; ++k)
				{
					if (dTable[i - 1][k] == -1) continue;

					int newVal = dTable[i - 1][k];
					if (j != k) ++newVal;
					if (val == -1 || newVal < val)
					{
						val = newVal;
					}
				}

				dTable[i].push_back(val);
			}
		}
	}

	if (q == 0)
	{
		solution = 0;
	}
	else
	{
		for (int i = 0 ; i < s ; ++i)
		{
			if (dTable[q - 1][i] != -1 && dTable[q - 1][i] < solution)
			{
				solution = dTable[q - 1][i];
			}
		}
	}
}

int main(void)
{
	FILE *fin = fopen("a.in", "r");
	FILE *fout = fopen("a.out", "w");

	int T;
	fscanf(fin, "%d ", &T);

	for (int t = 1 ; t <= T ; ++t)
	{
		solution = 999999;
		engine.clear();
		query.clear();
		dTable.clear();

		fscanf(fin, "%d ", &s);
		for (int i = 0 ; i < s ; ++i)
		{
			char temp[151];
			fgets(temp, 150, fin);
			engine[temp] = i;
		}

		fscanf(fin, "%d ", &q);
		for (int i = 0 ; i < q ; ++i)
		{
			char temp[151];
			fgets(temp, 150, fin);
			query.push_back(temp);
		}

		solve();

		fprintf(fout, "Case #%d: %d\n", t, solution);
	}

	fclose(fin);
	fclose(fout);
}