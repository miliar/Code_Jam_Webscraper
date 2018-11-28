#include <cstdio>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

#define For(i, n) for (int i = 0; i < n; i ++)
#define foreach(x, i) for (__typeof(x.begin()) i; i != x.end(); i ++)

using namespace std;

int a[1000];
int n, l, r;
int valid()
{
	for (int i = l; i <= r; i ++)
	{
		bool flag = true;
		for (int j = 0; j < n && flag; j ++)
			if (!(i % a[j] == 0 || a[j] % i == 0))
				flag = false;
		if (flag) return i;
	}
	return false;

}

void solve()
{
	scanf("%d%d%d", &n, &l, &r);
	for (int i = 0; i < n; i ++)
		scanf("%d", &a[i]);
	if (int ans = valid())
		printf("%d\n", ans);
	else puts("NO");
}

int main()
{
	int t; scanf("%d", &t);
	For (i, t) printf("Case #%d: ", i + 1), solve();
	return 0;
}

