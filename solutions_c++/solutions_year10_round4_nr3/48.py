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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int r;
		scanf("%d", &r);
		int f[120][120];
		int f2[120][120];
		memset(f, 0, sizeof(f));
		memset(f2, 0, sizeof(f2));
		for (int k = 0; k < r; k++)
		{
			int x1, y1, x2, y2;
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i = x1; i <= x2; i++)
				for (int j = y1; j <= y2; j++)
					f[i][j] = 1;
		}

		int cnt = 0;
		while (1)
		{
			cnt++;
			int life = 0;
			for (int i = 0; i <= 100; i++)
				for (int j = 0; j <= 100; j++)
				{
					if (f[i][j])
						f2[i][j] = !(!i || !j || !f[i - 1][j] && !f[i][j - 1]);
					else
						f2[i][j] = i && j && f[i - 1][j] && f[i][j - 1];
					life |= f2[i][j];
				}
			if (!life)
				break;
			memcpy(f, f2, sizeof(f));
		}

		printf("Case #%d: %d\n", testCount + 1, cnt);
	}
	return 0;
}