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

#define MAX 64

using namespace std;
FILE *in; FILE *out;

int n;
string a[MAX];

void doWork(int testNum)
{
	fscanf(in, "%d", &n);
	for (int i=0; i<n; i++)
	{
		char buff[MAX];
		fscanf(in, "%s", buff);
		a[i] = buff;
	}
	
	int ans = 0;
	for (int i=0; i<n; i++)
	{
		int who = i;
		for (int c=i; c<n; c++)
		{
			int flag = 1;
			for (int j=i+1; j<n; j++)
				if (a[c][j] == '1') {flag = 0; break;}
			if (flag) {who = c; break;}
		}
		while (who > i) {ans++; swap(a[who-1], a[who]); who--;}
	}
	fprintf(out, "%d\n", ans);
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("CrazyRows.in", "rt");
	out = fopen("CrazyRows.out", "wt");
	
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
