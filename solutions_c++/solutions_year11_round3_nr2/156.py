#include <stdio.h>
#include <algorithm>
using namespace std;

typedef _int64 LL;

static const int N = 1000010;
static const int MAXC = 1010;

int a[MAXC];
double dis[N];

bool cmp(double x, double y)
{
	return x > y;
}


int main()
{
	int total;
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	scanf("%d", &total);
	for (int test = 1; test <= total; ++test)
	{
		double ans = 0;
		
		LL t;
		int n, m, c;

		scanf("%d%I64d%d%d", &m, &t, &n, &c);
		for (int i = 0; i < c; ++i)
			scanf("%d", &a[i]);


		//在时间t到达前可以走到哪里
		int star = 0;
		double notwalk = 0;

		while (ans < t && star < n)
		{ 
			int next = 2 * a[star % c];
			if (ans + next <= t)
				ans += next;
			else
			{
				notwalk = (ans + next - t) / 2.0;
				ans = t;
				break;
			}

			++star;
		}
		
		int left = 0;
		if (notwalk)
		{
			dis[left++] = notwalk;
			star++;
		}

		for (int i = star; i < n; ++i, ++left)
		{
			dis[left] = a[i % c];
		}
	
		sort(dis, dis + left, cmp);


		//选择L段进行加速
		for (int i = 0; i < left; ++i)
		{
			if (m > 0)
			{
				ans += dis[i];
				--m;
			}
			else ans += 2 * dis[i];
		}

		printf("Case #%d: %I64d\n", test, (LL)ans);
	}
	return 0;
}