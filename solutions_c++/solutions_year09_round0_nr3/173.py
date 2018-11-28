#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define INF           0x7f7f7f7f
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

/* @date    03.09.2009
 * @idea    1) Find all possible positions for each symbol of wel[] in s[].
 *          2) Calculate DP:
 *                dp[i][j] - number of ways to match prefix wel[0..i-1] by
 *                           characters from s[0..j-1], iff s[j] = wel[i]
 */

const char wel[] = "welcome to code jam";

int N;
char s[501];
int dp[19][500];
VI pos[19];

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt+", stdout);

	scanf ("%d\n", &N);
	for (int tc = 0; tc < N; tc++)
	{
		memset (dp, 0, sizeof (dp));
		gets (s);
		int len = strlen (s);

		for (int i = 0; i < 19; i++) pos[i].clear();
		for (int i = 0; i < len; i++)
			for (int j = 0; j < 19; j++)
				if (s[i] == wel[j]) pos[j].push_back(i);
		
		for (int i = 0; i < 19-1; i++)
			for (int j = 0; j < SZ(pos[i]); j++) {
				if (i == 0) dp[0][pos[i][j]] = 1;
				for (int k = 0; k < SZ(pos[i+1]); k++) {
					if (pos[i+1][k] <= pos[i][j]) continue;
					dp[i+1][pos[i+1][k]] += dp[i][pos[i][j]];
					dp[i+1][pos[i+1][k]] %= 10000;
				}
			}

		int res = 0;
		for (int i = 0; i < SZ(pos[18]); i++)
			res = (res + dp[18][pos[18][i]]) % 10000;
		printf ("Case #%d: %.04d\n", tc+1, res);
	}

	return 0;
}