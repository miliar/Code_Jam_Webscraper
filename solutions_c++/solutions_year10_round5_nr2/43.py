#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 100;
const int maxx = 100000;

struct node
{
	int c, k;
	bool operator < (node b)
	{
		return c > b.c;
	}
};

int a[maxn];
int b[maxx];
bool c[maxx];
node h[maxx * maxn];
int top;
int n;
long long l;

int gcd(int x, int y)
{
	if (y == 0) return x;
	else return gcd(y, x % y);
}

int main()
{
	int testnumber;
	
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	scanf("%d", &testnumber);
	for (int testcount = 0; testcount < testnumber; testcount++)
	{
		scanf("%lld%d", &l, &n);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		
		int g = a[0];
		for (int i = 1; i < n; i++)
			g = gcd(a[i], g);
		if (l % g != 0)
		{
			printf("Case #%d: IMPOSSIBLE\n", testcount + 1);
		}
		else
		{
			for (int i = 0; i < n; i++)
				a[i] /= g;
			l /= g;
			sort(a, a + n);
			
			memset(b, 0x7f, sizeof b);
			memset(c, 0, sizeof c);
			b[0] = 0;
			top = 1;
			h[0].c = 0;
			h[0].k = 0;
			while (top != 0)
			{
				int now = h[0].k;
				pop_heap(h, h + top);
				top--;
				c[now] = true;
				for (int j = 0; j < n - 1; j++)
				{
					int next = now + a[j];
					int cost = 1;
					if (next >= a[n - 1])
					{
						cost = 0;
						next -= a[n - 1];
					}
					if (b[now] + cost < b[next])
					{
						b[next] = b[now] + cost;
						h[top].c = b[next];
						h[top].k = next;
						top++;
						push_heap(h, h + top);
					}
				}
			}
			printf("Case #%d: %lld\n", testcount + 1, (l / a[n - 1]) + b[l % a[n - 1]]);
		}
	}
	
	return 0;
}
