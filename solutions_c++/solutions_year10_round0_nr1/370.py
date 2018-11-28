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

using namespace std;
FILE *in; FILE *out;

long long parseLong()
{
	char buff[MAX];
	fscanf(in, "%s", buff);
	long long ret = 0;
	for (int i = 0; i < (int)strlen(buff); i++)
		ret = ret * 10 + buff[i] - 48;
	return ret;
}

void doWork(int testNum)
{
	long long n, k;
	n = parseLong(); k = parseLong();
	
	if (k <= (1 << n) - 1)
	{
		if (k < (1 << n) - 1) fprintf(out, "OFF\n");
		else fprintf(out, "ON\n");
		return;
	}
	k -= (1 << n) - 1;
	if (k % (1 << n) == 0) fprintf(out, "ON\n");
	else fprintf(out, "OFF\n");
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("SnapperChain.in", "rt");
	out = fopen("SnapperChain.out", "wt");
	
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
