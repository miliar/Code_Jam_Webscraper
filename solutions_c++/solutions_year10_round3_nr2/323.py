#include<iostream>
#include<cstring>
#include<algorithm>
#include<stdlib.h>

using namespace std;

#define MAX 100005
#define lld long long
lld a[MAX];
int main(void)
{
	int cas, goal, s, p, cnt, c, l, r, mid;
	lld tmp;

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	scanf("%d", &cas);

	for (int t = 1; t <= cas; t++)
	{
		scanf("%d%d%d", &s, &p, &c);

		tmp = s;
		cnt = 0;
		a[cnt++] = tmp;
		while (tmp < p)
		{
			tmp *= c;
			a[cnt++] = tmp;
		}

		l = 1, r = cnt;

		goal = 0;
		
		if (l == r)
		{
			printf("Case #%d: %d\n", t, goal);
			continue;
		}

		while (l+1 != r)
		{
			mid = (l+r)/2;
			if (r - mid >= mid-l)
				l = mid;
			else
				r = mid;
			goal++;
		}
		printf("Case #%d: %d\n", t, goal);
	}
}