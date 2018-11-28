#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cctype>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

int a[120];
int n, l, h;

int main()
{
#ifdef impetus
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int testnum;
	scanf("%d", &testnum);
	for (int tc = 0; tc < testnum; tc++)
	{
		scanf("%d%d%d", &n, &l, &h);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		int res = -1;
		for (int i = l; i <= h; i++)
		{
			int ok = 1;
			for (int j = 0; j < n; j++)
				if (i % a[j] && a[j] % i)
					ok = 0;
			if (ok)
			{
				res = i;
				break;
			}
		}
		if (res == -1)
			printf("Case #%d: NO\n", tc + 1);
		else
			printf("Case #%d: %d\n", tc + 1, res);
	}
	return 0;
}