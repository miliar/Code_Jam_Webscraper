#include <iostream>
#include <iomanip>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>

#define MAX 1024
#define INF 999666333

using namespace std;
FILE *in; FILE *out;

int n, m;
vector <string> engines;
vector <string> queries;

int dyn[MAX][MAX];

int recurse(int cur, int engine)
{
	int i;
	int tmp, ans = INF;
	
	if (cur >= (int)queries.size()) return 0;
	if (dyn[cur][engine] != -1) return dyn[cur][engine];
	
	if (queries[cur] != engines[engine]) ans = recurse(cur + 1, engine);
	else
	{
		for (i=0; i<(int)engines.size(); i++)
		{
			if (engines[i] != queries[cur])
			{
				tmp = recurse(cur + 1, i) + 1;
				ans = min(ans, tmp);				
			}
		}
	}
	
	dyn[cur][engine] = ans;
	return ans;
}

/*
int beGreedy(void)
{
	int i, c, j;
	int ans = 0;
	string cur;
	
	if (queries.size() == 0) return 0;

	cur = queries[0];
	for (i=0; i<(int)queries.size(); i++)
	{
		if (cur == queries[i])
		{
			string next; int places = -1;

			for (c=0; c<(int)engines.size(); c++)
			{
				int curPlaces = -1;
				for (j=i; j<(int)queries.size(); j++)
				{
					if (queries[j] == engines[c]) break;
					else curPlaces = j;
				}
				if (curPlaces > places)
				{
					places = curPlaces;
					next = engines[c];
				}
			}
			cur = next; ans++;
		}
	}
	
	return ans - 1;
}
*/

void saveTheUniverse(int testCase)
{
	int i, c;
	int tmp, ans = INF;
	
	char buff[MAX];
	queries.clear(); engines.clear();
	
	fscanf(in, "%d", &n);
	fgets(buff, MAX, in);
	for (i=0; i<n; i++)
	{
		fgets(buff, MAX, in);
		buff[(int)strlen(buff)-1] = 0;
		engines.push_back(buff);
	}

	fscanf(in, "%d", &m);
	fgets(buff, MAX, in);
	for (i=0; i<m; i++)
	{
		fgets(buff, MAX, in);
		buff[(int)strlen(buff)-1] = 0;
		queries.push_back(buff);
	}
	
	memset(dyn, -1, sizeof(dyn));
	for (i=0; i<(int)engines.size(); i++)
	{
		tmp = recurse(0, i);
		ans = min(ans, tmp);
	}
	
//	ans = beGreedy();
	
	fprintf(out, "Case #%d: %d\n", testCase, ans);	
	return;
}


int main(void)
{
	int tests, i;
	
	in = fopen("SavingTheUniverse.in", "rt");
	out = fopen("SavingTheUniverse.out", "wt");
	
	fscanf(in, "%d", &tests);
	for (i=0; i<tests; i++) saveTheUniverse(i + 1);
	
	return 0;
}
