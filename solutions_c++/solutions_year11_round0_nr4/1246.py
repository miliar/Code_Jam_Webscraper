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
#define INF 999666333111.0

using namespace std;
FILE *in; FILE *out;

double dyn[MAX];
double chance[MAX][MAX], ch[MAX][MAX];

double recurse(int rem)
{
	if (rem <= 1) return 0.0;
	if (dyn[rem] >= -3.14) return dyn[rem];
	
	double cur = 0.0;
	for (int fit = 1; fit <= rem; fit++)
		cur += chance[rem][fit] * (recurse(rem - fit) + 1.0);
	
	return dyn[rem] = (ch[rem][0] + cur - ch[rem][0] * cur) / (1.0 - ch[rem][0]);
}

void doWork(int testNum)
{
	int n, cur, cnt = 0;
	fscanf(in, "%d", &n);
	for (int i = 1; i <= n; i++)
	{
		fscanf(in, "%d", &cur);
		if (cur != i) cnt++;
	}
	fprintf(out, "%.9lf\n", recurse(cnt));
}

double der[MAX];
double tri[MAX][MAX];

void calcTri()
{
	tri[0][0] = 1.0;
	for (int i = 1; i < MAX; i++)
	{
		tri[i][0] = 1;
		for (int c = 1; c <= i; c++)
			tri[i][c] = tri[i - 1][c - 1] + tri[i - 1][c];
	}
}

void calcDer()
{
	der[0] = 1; der[1] = 0;
	for (int i = 2; i < MAX; i++)
		der[i] = (i - 1) * (der[i - 1] + der[i - 2]);
}

void calcChance()
{
	calcTri();
	calcDer();

	double fact = 1;
	for (int all = 0; all < MAX; all++)
	{
		if (all > 0) fact *= all;
		for (int fit = 0; fit <= all; fit++)
		{
			ch[all][fit] = tri[all][fit] * der[all - fit] / fact;
			chance[all][fit] = (tri[all][fit] * der[all - fit]) / (fact - der[all]);
		}
	}
	
	/*
	for (int size = 1; size <= 10; size++)
	{
		cout << "With size " << size << ":";
		for (int i = 0; i <= size; i++)
			cout << " " << chance[size][i];
		cout << endl;
	}
	system("pause");
	*/
	
	/*
	for (int len = 1; len < 10; len++)
	{
		vector <int> v;
		for (int i = 0; i < len; i++) v.push_back(i);
		
		int cnt = 0, all = 0;
		do
		{
			all++;
			int flag = 1;
			for (int i = 0; i < (int)v.size(); i++)
				if (v[i] == i) {flag = 0; break;}
			cnt += flag;
		} while(next_permutation(v.begin(), v.end()));
		cout << "With length = " << len << " there are " << cnt << " out of " << all << endl;
	}
	system("pause");
	*/
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("GoroSort.in", "rt");
	out = fopen("GoroSort.out", "wt");
	
	for (int i = 0; i < MAX; i++)
		dyn[i] = -42;
	calcChance();

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
