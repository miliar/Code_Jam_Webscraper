#include <cstdio>
#include <string>
#include <vector>

using namespace std;

long long dp[41][210];

long long doit(string s, int beg, int b)
{
	if (beg == s.length()) {
		return ((b % 2 == 0) || (b % 3 == 0) ||
			(b % 5 == 0) || (b % 7 == 0)) ? 1 : 0;
	}

	if (dp[beg][b] >= 0) {
		return dp[beg][b];
	}

	long long num = 0;
	int base = 0;
	for (int i = beg; i < s.length() - 1; i++) {
		base += s[i] - '0';
		base %= 210;
		num += doit(s, i + 1, (base + b) % 210);
		num += doit(s, i + 1, (420 - base - b) % 210);
		base *= 10;
	}
	int i = s.length() - 1;
	base += s[i] - '0';
	base %= 210;
	num += doit(s, i + 1, (base + b) % 210);

	//printf("%d %d %lld\n", beg, b, num);
	return (dp[beg][b] = num);
}

int main()
{
	char inp[999];

	int cases;
	gets(inp); sscanf(inp, "%d", &cases);

	for (int casenum = 1; casenum <= cases; casenum++) {
		string s;
		gets(inp); s = inp;

		memset(&(dp[0][0]), -1, sizeof(dp));
		long long num = doit(s, 0, 0);

		printf("Case #%d: %I64d\n", casenum, num);
	}

	return 0;
}

