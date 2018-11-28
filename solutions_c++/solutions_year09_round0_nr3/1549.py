#include <stdio.h>
#include <vector>
#include <map>
#include <string>

using namespace std;

typedef long long lld;

string str;
string match;

map<pair<int,int>, lld> dp;

lld calc(int stri, int matchi)
{
	if (!dp.count(make_pair(stri,matchi)))
	{
		lld res = 0;

		if (matchi == match.size())
			res = 1;
		else if (stri == str.size())
			res = 0;
		else
		{
			res += calc(stri+1, matchi);
			if (str[stri] == match[matchi])
				res += calc(stri+1,matchi+1);
		}

		res %= 10000;

		dp[make_pair(stri,matchi)] = res;
	}
	return dp[make_pair(stri,matchi)];
}

int main()
{
	FILE *in = fopen("C-large.in", "r");
	FILE *out = fopen("C.out", "w");

	match = "welcome to code jam";

	char buf[100000];
	fgets(buf, 100000, in);

	int ncases;
	sscanf(buf, "%d", &ncases);

	for(int casenum = 1; casenum <= ncases; casenum++)
	{
		fgets(buf, 100000, in);
		str = buf;

		dp.clear();

		fprintf(out, "Case #%d: %.4d\n", casenum, calc(0, 0));
	}
}
