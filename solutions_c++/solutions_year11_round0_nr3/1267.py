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
		int n;
		scanf("%d", &n);
		long long ss = 0, sxor = 0, least = 1000000000;
		for (int i = 0; i < n; i++)
		{
			int p;
			scanf("%d", &p);
			ss += p;
			sxor = (sxor ^ p);
			least = min(least, (long long)p);
		}
		if (sxor)
			printf("Case #%d: NO\n", tc + 1);
		else
			printf("Case #%d: %lld\n", tc + 1, ss - least);
	}
	return 0;
}