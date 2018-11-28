#include <stdio.h>
#include <string>
using namespace std;

#define MOD 10000

string target = "welcome to code jam";

int tc, ntc;
char s[1100];

int dp[600][20];
int len;
int tlen;

int doit(int a, int b)
{
	if (b == tlen) return 1;
	if (a == len) return 0;
	int& res = dp[a][b];
	if (res != -1) return res;

	res = 0;
	res += doit(a+1, b);
	if (s[a] == target[b]) res += doit(a+1, b+1);
	res %= MOD;
	return res;
}

int main()
{
	FILE* fi = fopen("C-large.in", "r");
	FILE* fo = fopen("C-large.out", "w");

	tlen = target.length();

	fscanf(fi, "%d", &ntc);
	fgets(s, 1000, fi);

	int i;
	for (tc=1; tc<=ntc; tc++)
	{
		fgets(s, 1000, fi);
		len = strlen( s );

		memset(dp, -1, sizeof(dp));
		int res = doit(0, 0);
		printf("Case #%d: %.4d\n", tc, res);
		fprintf(fo, "Case #%d: %.4d\n", tc, res);				
	}

	fclose(fi); fclose(fo);
}