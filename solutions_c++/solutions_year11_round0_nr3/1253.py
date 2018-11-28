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


void doWork(int testNum)
{
	int n;
	fscanf(in, "%d", &n);

	int minn = 999666333, sum = 0, xr = 0, cur;
	for (int i = 0; i < n; i++)
	{
		fscanf(in, "%d", &cur);
		xr ^= cur;
		minn = min(minn, cur);
		sum += cur;
	}
	if (xr != 0) fprintf(out, "NO\n");
	else fprintf(out, "%d\n", sum - minn);
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("CandySplitting.in", "rt");
	out = fopen("CandySplitting.out", "wt");
	
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
