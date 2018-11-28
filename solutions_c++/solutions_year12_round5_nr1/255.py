#include <cstdio>
#include <algorithm>
using namespace std;
const int maxn = 1005;
struct node
{
	int x, d;
}	a[maxn];
int test, n, l[maxn], p[maxn];

bool cmp(const node &a, const node &b)
{
	return a.x > b.x || a.x == b.x && a.d < b.d;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &test);
	for (int kase = 1; kase <= test; ++kase)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%d", &l[i]);
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &p[i]);
			a[i].x = p[i];
			a[i].d = i - 1;
		}
		sort(a + 1, a + n + 1, cmp);
		printf("Case #%d:", kase);
		for (int i = 1; i <= n; ++i)
			printf(" %d", a[i].d);
		puts("");
	}
	
	return 0;
}
