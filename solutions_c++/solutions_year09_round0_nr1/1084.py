#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:65000000")
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <cmath>

using namespace std;
const string FILENAME = "awe";

vector<string> dict;

int main()
{
	freopen((FILENAME + ".in").c_str(), "r", stdin);
	freopen((FILENAME + ".out").c_str(), "w", stdout);

	int L, D, N;
	scanf("%d%d%d\n", &L, &D, &N);
	char buf[5000];
	for (int i = 0; i < D; ++i)
	{
		gets(buf);
		dict.push_back(buf);
	}
	for (int tc = 0; tc < N; ++tc)
	{
		gets(buf);
		
		vector<int> tokens;
		char *c = buf;
		bool br = false;
		int mask = 0;
		while (*c != 0)
		{
			if (!br)
				mask = 0;
			if (*c == '(')
				br = true;
			else if (*c == ')')
			{
				br = false;
				tokens.push_back(mask);
			}
			else 
			{
				mask |= 1 << (*c - 'a');
				if (!br)
					tokens.push_back(mask);
			}
			++c;
		}
		int res = 0;
		for (int i = 0; i < D; ++i)
		{
			bool ok = true;
			for (int j = 0; j < L && ok; ++j)
				ok &= (tokens[j] & (1 << (dict[i][j] - 'a'))) != 0;
			if (ok)
				++res;
		}
		printf("Case #%d: %d\n", tc + 1, res);
	}

	return 0;
}