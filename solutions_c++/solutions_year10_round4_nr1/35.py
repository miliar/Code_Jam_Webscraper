#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

int fun(int n, int d)
{
	return sqr(n + d) - sqr(n);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int n;
		scanf("%d", &n);
		char s[120][120];
		memset(s, ' ', sizeof(s));
		gets(s[0]);
		for (int i = 0; i < 2 * n - 1; i++)
		{
			gets(s[i]);
			s[i][strlen(s[i])] = ' ';
			s[i][2 * n - 1] = 0;
		}
		int best = 1000000000;
		for (int i = 0; i < 2 * n - 1; i++)
			for (int j = 0; j < 2 * n - 1; j++)
			{
				int fail = 0;
				for (int ii = 0; ii < 2 * n - 1; ii++)
					for (int jj = 0; jj < 2 * n - 1; jj++) if (s[ii][jj] != ' ')
					{
						int iii = 2 * i - ii;
						int jjj = jj;
						if (iii >= 0 && iii < 2 * n - 1 && jjj >= 0 && jjj < 2 * n - 1 && s[iii][jjj] != ' ' && s[iii][jjj] != s[ii][jj])
							fail = 1;
						iii = ii;
						jjj = 2 * j - jj;
						if (iii >= 0 && iii < 2 * n - 1 && jjj >= 0 && jjj < 2 * n - 1 && s[iii][jjj] != ' ' && s[iii][jjj] != s[ii][jj])
							fail = 1;
					}
				if (!fail)
					best = min(best, fun(n, abs(n - 1 - i) + abs(n - 1 - j)));
			}
		printf("Case #%d: %d\n", testCount + 1, best);
	}
	return 0;
}