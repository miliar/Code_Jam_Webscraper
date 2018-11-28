#include <stdio.h>
#include <string.h>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <bitset>
#include <iostream>
#include <queue>
#define FOR(i,n) for(int i = 0; i < (int) (n); i++)
using namespace std;

const char pattern[] = "welcome to code jam";

int dp[512][24];
char line[512];
int l, pl;

int f(int i, int j)
{
	if (j >= pl) return 1;
	int &d = dp[i][j];
	if (d != -1) return d;
	d = 0;
	for (int k = i; k < l; k++) if (line[k] == pattern[j]) {
		d = (d + f(k + 1, j + 1)) % 10000;
	}
	return d;
}

int main(void)
{
	int T;
	fgets(line, sizeof(line), stdin);
	sscanf(line, "%d", &T);
	pl = (int) strlen(pattern);
	FOR(tc, T) {
		printf("Case #%d: ", tc + 1);
		fgets(line, sizeof(line), stdin);
		memset(dp, 0xff, sizeof(dp));
		l = (int) strlen(line);
		if (l && line[l-1] == '\n') line[--l] = 0;
		int ans = f(0, 0);
		printf("%04d\n", ans);
		//xans = 0;
		//bt(0, 0);
		//if (ans != xans) printf("Different, should be %d, but calculated as %d\n", xans, ans);
	}
	
	return 0;
}
