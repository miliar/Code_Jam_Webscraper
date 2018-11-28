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
		int r, n;
		long long k;
		scanf("%d%lld%d", &r, &k, &n);
		vector<int> g(n), next(n);
		vector<long long> l(n);
		long long s = 0;
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &g[i]);
			s += g[i];
		}
		for (int i = 0; i < n; i++)
		{
			long long left = k;
			l[i] = 0;
			int cur = i;
			while (left >= g[cur] && l[i] < s)
			{
				l[i] += g[cur];
				left -= g[cur];
				cur = (cur + 1) % n;
			}
			next[i] = cur;
		}
		long long res = 0;
		int cur = 0;
		for (int i = 0; i < r; i++)
		{
			res += l[cur];
			cur = next[cur];
		}
		printf("Case #%d: %lld\n", testCount + 1, res);
	}
	return 0;
}