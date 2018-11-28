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
#define MOD 10000

using namespace std;
FILE *in; FILE *out;

int n, m;
char line[MAX], word[MAX] = "welcome to code jam";
int dyn[MAX][MAX];

int recurse(int cur, int pos)
{
	if (pos >= m) return 1;
	if (cur >= n) return 0;
	if (dyn[cur][pos] != -1) return dyn[cur][pos];
	
	int ans = recurse(cur + 1, pos);
	if (line[cur] == word[pos]) ans += recurse(cur + 1, pos + 1);
	
	return dyn[cur][pos] = ans % MOD;
}

void doWork(int testNum)
{
	fgets(line, MAX, in);
	n = (int)strlen(line);
	m = (int)strlen(word);
	
	memset(dyn, -1, sizeof(dyn));
	fprintf(out, "%04d\n", recurse(0, 0));
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("WelcomeToCodeJam.in", "rt");
	out = fopen("WelcomeToCodeJam.out", "wt");
	
	int numTests;
	fscanf(in, "%d", &numTests);
	fgets(line, MAX, in);
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
