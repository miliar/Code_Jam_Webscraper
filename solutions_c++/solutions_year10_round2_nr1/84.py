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

#define MAX 1024
#define MAX_BUFF 1024

using namespace std;
FILE *in; FILE *out;

char buff[MAX_BUFF];

void doWork(int testNum)
{
	int n, m;
	fscanf(in, "%d %d", &n, &m);
	set <string> have;
	have.insert("");
	
	int ans = 0;
	for (int i = 0; i < n; i++)
	{
		fscanf(in, "%s", buff);
		have.insert(buff);
	}
	for (int i = 0; i < m; i++)
	{
		fscanf(in, "%s", buff);
		int len = (int)strlen(buff);
		string str;
		buff[len++] = '/'; buff[len++] = 0;
		for (int c = 0; c < len; c++)
		{
			if (buff[c] == '/')
			{
				if (have.find(str) == have.end())
				{
					ans++;
					have.insert(str);
				}
				str += buff[c];
			}
			else str += buff[c];
		}
	}
	fprintf(out, "%d\n", ans);
	
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("fileFixIt.in", "rt");
	out = fopen("fileFixIt.out", "wt");
	
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
