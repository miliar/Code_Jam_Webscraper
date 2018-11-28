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
#include <cctype>

#define MAX 1024
#define POSSIBLE "Possible"
#define IMPOSSIBLE "Broken"

using namespace std;
FILE *in; FILE *out;

long long parseLong()
{
	char buff[32];
	fscanf(in, "%s", buff);
	long long ret = 0;
	for (int i = 0; i < (int)strlen(buff); i++)
		ret = ret * 10 + buff[i] - 48;
	return ret;
}

long long gcd(long long a, long long b)
{
	if (a < b) swap(a, b);
	while (b != 0)
	{
		a %= b;
		swap(a, b);
	}
	return a;
}

void doWork(int testNum)
{
	long long n, pd, pg;
	
	n = parseLong();
	pd = parseLong();
	pg = parseLong();
	
	if (pg == 0)
	{
		if (pd == 0)
			fprintf(out, "%s\n", POSSIBLE);
		else
			fprintf(out, "%s\n", IMPOSSIBLE);
		return;
	}
	
	if (pg == 100)
	{
		if (pd == 100)
			fprintf(out, "%s\n", POSSIBLE);
		else
			fprintf(out, "%s\n", IMPOSSIBLE);
		return;
	}
	
	long long g = gcd(pd, 100);
	if (n < 100 / g)
		fprintf(out, "%s\n", IMPOSSIBLE);
	else
		fprintf(out, "%s\n", POSSIBLE);
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("FreeCellStatistics.in", "rt");
	out = fopen("FreeCellStatistics.out", "wt");
	
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
