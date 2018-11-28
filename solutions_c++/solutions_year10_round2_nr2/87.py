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

int n, k, b, t;
int a[MAX], v[MAX];

void doWork(int testNum)
{
	fscanf(in, "%d %d %d %d", &n, &k, &b, &t);
	for (int i = 0; i < n; i++) fscanf(in, "%d", &a[i]);
	for (int i = 0; i < n; i++) fscanf(in, "%d", &v[i]);
	
	int ans = 0, swp = 0, rem = k;
	for (int i = n - 1; i >= 0; i--)
	{
		long long dist = b - a[i];
		long long req = dist / v[i] + !!(dist % v[i]);
		if (req <= t) {ans += swp; rem--; if (rem <= 0) break;}
		else swp++;
	}
	if (rem > 0) fprintf(out, "IMPOSSIBLE\n");
	else fprintf(out, "%d\n", ans);	
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("PickingUpChicks.in", "rt");
	out = fopen("PickingUpChicks.out", "wt");
	
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
