#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>

#include <algorithm>
#include <memory>
#include <string>
#include <vector>
#include <map>
#include <iostream>

#define TASK "c"
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)

using namespace std;

#define MAXN 1000

int T, n, len;

const int p_len = 19;
const int mod = 10000;
const string pattern = "welcome to code jam";

int f[MAXN][p_len + 100];

int ff(int x, int y)
{
	if (x >= 0 && x <= len && y >= 0 && y <= p_len)
		return f[x][y];
	return 0;
}

void write(int x)
{
	x %= mod;
	if (x < 1000)
		printf("0");
	if (x < 100)
		printf("0");
	if (x < 10)
		printf("0");
	printf("%d", x);
}

int main()
{
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif
	scanf("%d\n", &T);

	for (int t = 1; t <= T; t++)
	{
		memset(f, 0, sizeof(f));
		string str = "";
		char buf;
		while (scanf("%c", &buf) == 1 && buf != '\n')
			str = str + buf;
	    len = str.length();

		memset(f, 0, sizeof(f));	    	
	    f[0][0] = 1;

	    for (int i = 0; i <= len; i++)
	    	for (int j = 0; j <= p_len; j++)
	    	{
	    		f[i + 1][j] = (f[i][j] + f[i + 1][j]) % mod;

	    		if (i < len && j < p_len && pattern[j] == str[i])
	    			f[i + 1][j + 1] = (f[i + 1][j + 1] + f[i][j]) % mod;
//				printf("f[%d][%d] == %d\n", i, j, f[i][j]);
	    	}
		printf("Case #%d: ", t);
		write(f[len][p_len] % mod);
		printf("\n");
	}

	return 0;
}
