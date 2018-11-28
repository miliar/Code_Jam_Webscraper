#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;
const int N = 2000;
bool bb[N][N];
int main()
{
	int test;
	scanf("%d", &test);
	bool b[N];
	int begin[N], end[N], col[N];
	for (int testi = 0; testi < test; ++testi)
	{
		memset(b, 0, sizeof(b));
		memset(bb, 0, sizeof(bb));
		int n, m;
		scanf("%d%d", &n, &m);
		int minn = n;
		for (int i = 0; i < m; ++i)
		{
			scanf("%d", begin + i);
			--begin[i];
		}
		for (int i = 0; i < m; ++i)
		{
			scanf("%d", end + i);
			--end[i];
			b[begin[i]] = 1;
			b[end[i]] = 1;
			bb[begin[i]][end[i]] = 1;
			bb[end[i]][begin[i]] = 1;
			minn = min(minn, 2 + min(abs(end[i] - begin[i] - 1), n - 2 - abs(end[i] - begin[i] - 1)));
		}
		//printf("%d\n", minn);
		for (int i = 0; i < n; ++i)
		{
			if (!b[i])
			{
				continue;
			}
			for (int j = i + 1; !b[j]; ++j)
		}
	}
	return 0;
}