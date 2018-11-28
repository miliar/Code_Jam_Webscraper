#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <stack>

#define MAX 256

using namespace std;
FILE *in; FILE *out;

int n, m, k;
char a[MAX];
char opp[MAX][MAX];
char comb[MAX][MAX];

void doWork(int testNum)
{
	memset(opp, 0, sizeof(opp));
	memset(comb, 0, sizeof(comb));
	
	fscanf(in, "%d", &m);
	for (int i = 0; i < m; i++)
	{
		char buff[32];
		fscanf(in, "%s", buff);
		comb[(int)buff[0]][(int)buff[1]] = buff[2];
		comb[(int)buff[1]][(int)buff[0]] = buff[2];
	}
	
	fscanf(in, "%d", &k);
	for (int i = 0; i < k; i++)
	{
		char buff[32];
		fscanf(in, "%s", buff);
		opp[(int)buff[0]][(int)buff[1]] = 1;
		opp[(int)buff[1]][(int)buff[0]] = 1;
	}
	
	fscanf(in, "%d", &n);
	fscanf(in, "%s", a);
	
	vector <char> ans;
	for (int i = 0; i < n; i++)
	{
		ans.push_back(a[i]);
		while (ans.size() > 1)
		{
			char c1 = ans[ans.size() - 1];
			char c2 = ans[ans.size() - 2];
			if (comb[(int)c1][(int)c2])
			{
				ans.resize(ans.size() - 2);
				ans.push_back(comb[(int)c1][(int)c2]);
			}
			else break;
		}
		for (int i = 0; i < (int)ans.size() - 1; i++)
			if (opp[(int)ans[i]][(int)ans[ans.size() - 1]])
				ans.clear();
	}
	fprintf(out, "[");
	for (int i = 0; i < (int)ans.size(); i++)
	{
		fprintf(out, "%c", ans[i]);
		if (i + 1 < (int)ans.size()) fprintf(out, ", ");
	}
	fprintf(out, "]\n");
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("Magicka.in", "rt");
	out = fopen("Magicka.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	for (int test = 1; test <= numTests; test++)
	{
		fprintf(stderr, "Currently executing testcase %d...\n", test);
		fprintf(out, "Case #%d: ", test);
		doWork(test);
	}
	
	fprintf(stderr, "Total execution time %.3lf seconds.\n", (double)(clock() - sTime) / (double)CLOCKS_PER_SEC);
	system("pause");
	return 0;
}
