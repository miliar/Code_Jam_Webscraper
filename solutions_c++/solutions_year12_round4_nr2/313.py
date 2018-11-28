#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int maxn = 1005;

struct node
{
	int r, d, x, y;
};

node a[maxn];
int n, w, l, ax[maxn], ay[maxn], d[maxn], test;

bool cmp(const node &a, const node &b)
{
	return a.r > b.r;
}

int main()
{ 
    freopen("B.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    scanf("%d", &test);
    for (int kase = 1; kase <= test; ++kase)
    {
		scanf("%d %d %d", &n, &w, &l);
		bool change = 0;
		if (w < l)
		{
			change = 1;
			swap(w, l);
		}
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d", &a[i].r);
			a[i].d = i;
			d[i] = a[i].r;
		}
		sort(a + 1, a + n + 1, cmp);
		int next = 0, cnt = 0, now = 0;
		a[n + 1].r = 0;
		for (int i = 1; i <= n; ++i)
		{
			if (cnt > w)
				puts("no science!");
			if (!now)
				next += a[i].r;
			a[i].x = cnt;
			a[i].y = now;
			now += a[i].r;
			now += a[i + 1].r;
			if (now > l)
			{
				now = 0;
				next += a[i + 1].r;
				cnt = next;
			}
		}
		for (int i = 1; i <= n; ++i)
			if (change != 1)
				ax[a[i].d] = a[i].x, ay[a[i].d] = a[i].y;
			else
				ay[a[i].d] = a[i].x, ax[a[i].d] = a[i].y;
		printf("Case #%d: ", kase);
		for (int i = 1; i <= n; ++i)
			printf("%d.0 %d.0%c", ax[i], ay[i], i == n ? '\n' : ' ');
	}
	
	return 0;
}
