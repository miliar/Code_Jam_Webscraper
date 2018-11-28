#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
using namespace std;

int n;
long long s[10005], d[10005], l[10005], dd;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("ans.out", "w", stdout);

	int tt;
	scanf("%d", &tt);
	for(int t = 1; t <= tt; ++t)
	{
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
		{
			scanf("%lld%lld", &d[i], &l[i]);
			s[i] = -1;
		}
		scanf("%lld", &d[n]);
		long long sm, tmp;
		s[0] = d[0];
		s[n] = -1;
		l[n] = 0;
		for(int i = 1; i <= n; ++i)
		{
			sm = -1;
			for(int j = 0; j < i; ++j)
			{
				if(s[j] < d[i] - d[j])
					tmp = -1;
				else
					tmp = min(d[i]-d[j], l[i]);
				sm = max(sm, tmp);
			}
			s[i] = min(sm, l[i]);
		}
		printf("Case #%d: %s\n", t, (s[n] >= 0) ? "YES" : "NO");
	}
	return 0;
}

/*

int main()
{
	freopen("", "r", stdin);
	freopen("ans.out", "w", stdout);

	int tt;
	scanf("%d", &tt);
	for(int t = 1; t <= tt; ++t)
	{


		printf("Case #%d: ", t);
	}
	return 0;
}

*/