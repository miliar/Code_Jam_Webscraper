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

#define MAX 32

using namespace std;
FILE *in; FILE *out;


void doWork(int testNum)
{
	char buff[MAX];
	fscanf(in, "%s", buff);
	
	string str = buff;
	if (next_permutation(str.begin(), str.end()))
	{
		fprintf(out, "%s\n", str.c_str());
	}
	else
	{
		sort(str.begin(), str.end());
		int cnt = 0;
		for (int i=0; i<(int)str.size(); i++)
			if (str[i] == '0') cnt++;

		int pos = 0;
		while (str[pos] == '0') pos++;
		string ans;
		ans += str[pos++];
		for (int i=0; i<=cnt; i++) ans += '0';
		while (pos < (int)str.size()) ans += str[pos++];
		fprintf(out, "%s\n", ans.c_str());
	}
	
	return;
}

int main(void)
{
	unsigned sTime = clock();
	in = fopen("TheNextNumber.in", "rt");
	out = fopen("TheNextNumber.out", "wt");
	
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
