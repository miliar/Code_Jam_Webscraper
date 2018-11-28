#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>

#include <algorithm>
#include <set>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <iostream>

#define TASK "a"
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)

using namespace std;

#define MAXLEN 100

int L, D, N;
vector<string> dic;
set<char> pattern[MAXLEN];

int main()
{
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i++)
	{
		char buf[MAXLEN];
		scanf("%s", buf);
		dic.PB((string) buf);
	}

	for (int t = 1; t <= N; t++)
	{
		scanf("\n");
		for (int i = 0; i < L; i++)
		{
			pattern[i].clear();
			char ch;
			scanf("%c", &ch);
			assert(isalpha(ch) || ch == '(');
			if (isalpha(ch))
			{
				pattern[i].insert(ch);
				continue;
			}
			while (scanf("%c", &ch) == 1 && ch != ')')
			{
				pattern[i].insert(ch);
			}
		}

        int res = 0;
		for (int i = 0; i < D; i++)
		{
			bool ok = true;
			for (int j = 0; j < L; j++)
				if (pattern[j].find(dic[i][j]) == pattern[j].end())
				{
					ok = false;
					break;
				}
			res += ok;
		}

		printf("Case #%d: %d\n", t, res);
	}

	return 0;
}
