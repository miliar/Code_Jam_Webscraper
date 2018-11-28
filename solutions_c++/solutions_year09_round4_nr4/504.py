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
#include <ctime>

#define MAX 1024
#define INF 999666333

using namespace std;
FILE *in; FILE *out;
int n;
double a[MAX][3];

double dist(int idx1, int idx2)
{
	return sqrt ( (a[idx1][0] - a[idx2][0]) * (a[idx1][0] - a[idx2][0]) +
				  (a[idx1][1] - a[idx2][1]) * (a[idx1][1] - a[idx2][1]) );
}

void doWork(int testNum)
{
	fscanf(in, "%d", &n);
	for (int i=0; i<n; i++) fscanf(in, "%lf %lf %lf", &a[i][0], &a[i][1], &a[i][2]);
	
	double ans = INF;
	if (n == 1) {fprintf(out, "%.6lf\n", (double)a[0][2]); return;}
	if (n == 2) {fprintf(out, "%.6lf\n", max(a[0][2], a[1][2])); return;}	
	/*
	for (int i=0; i<n; i++)
	{
		for (int c=i+1; c<n; c++)
		{
			double cur = dist(i, c) + a[i][2] + a[c][2];
			if (ans < cur) continue;

			int can = 1;
			
			int 
			
			if (can) ans = min(ans, cur);
		}
	}
	*/
	
	// 0 and 1
	double cur = dist(0, 1) + a[0][2] + a[1][2]; ans = min(ans, cur);
	// 0 and 2
	cur = dist(0, 2) + a[0][2] + a[2][2]; ans = min(ans, cur);
	// 1 and 2
	cur = dist(1, 2) + a[1][2] + a[2][2]; ans = min(ans, cur);

	for (int i=0; i<n; i++) ans = max(ans, a[i][2]);	
	fprintf(out, "%.6lf\n", ans / 2.0);
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("WateringPlants.in", "rt");
	out = fopen("WateringPlants.out", "wt");
	
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
