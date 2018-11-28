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

int r, k, n;
int a[MAX];
long long dyn[MAX][2];

string toString(long long num)
{
	if (num == 0) return "0";
	string ret;
	while (num) {ret.push_back(num % 10 + 48); num /= 10;}
	reverse(ret.begin(), ret.end());
	return ret;
}

void doWork(int testNum)
{
	fscanf(in, "%d %d %d", &r, &k, &n);
	for (int i = 0; i < n; i++) fscanf(in, "%d", &a[i]);
	
	memset(dyn, -1, sizeof(dyn));
	
	queue <int> q;
	for (int i = 0; i < n; i++) q.push(i);
	
	int run = 0, flag = 0;
	long long ans = 0;
	while (run < r)
	{
		if (dyn[q.front()][0] != -1 && !flag)
		{
			flag = 1;
			long long cycle = run - dyn[q.front()][0];
			long long price = ans - dyn[q.front()][1];
			long long numCycles = (r - run) / cycle;
			ans += numCycles * price;
			run += numCycles * cycle;
			if (run >= r) break;
		}
		else {dyn[q.front()][0] = run; dyn[q.front()][1] = ans;}
		
		int rem = k;
		vector <int> go;
		while (!q.empty())
		{
			if (rem < a[q.front()]) break;
			rem -= a[q.front()]; ans += a[q.front()];
			go.push_back(q.front()); q.pop();
		}
		for (int i = 0; i < (int)go.size(); i++) q.push(go[i]);
		run++;
	}
	fprintf(out, "%s\n", toString(ans).c_str());	
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("ThemePark.in", "rt");
	out = fopen("ThemePark.out", "wt");
	
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
