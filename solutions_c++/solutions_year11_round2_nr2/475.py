#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

const int N = 2000000;
typedef long long ll;
ll a[N];
ll b[N];
int cnt = 0;
int D;

bool check(ll time)
{
	memcpy(a, b, cnt * sizeof(ll));
	a[0] -= time;
	a[cnt - 1] += time;
	//printf("test time:%d\n", time);
	for (int l = 1; l < cnt - 1; l++)
	{
		if (a[l-1] + D <= a[l])
		{
			if (a[l-1] + D + time <= a[l])
			{
				a[l] -= time;
			}
			else
			{
				a[l] = a[l-1] + D;
			}
		}
		else
		{
			if (a[l-1] + D >= a[l] + time)
			{
				a[l] += time;
			}
			else
			{
				a[l] = a[l-1] + D;
			}
		}
	}
	for (int l = 1; l < cnt; l++)
	{
		if (a[l - 1] + D <= a[l]);
		else return false;
	}
	return true;
}

int main()
{
	int tc0, tc;
	ll l, r, time;
	scanf("%d", &tc0);
	for (int tc = 1; tc <= tc0; tc++)
	{
		int C;
		cnt  = 0;
		scanf("%d%d", &C, &D);
		D *= 2;
		for (int i = 0; i < C; i++)
		{
			int P, V;
			scanf("%d%d", &P, &V);
			for (int j = 0; j < V; j++)
			{
				b[cnt++] = P * 2;
			}
		}
		//sort (b, b + cnt);
		if (cnt == 1)
		{
			time = 0;
			goto end;
		}
		if (check(0) == true)
		{
			time = 0;
			goto end;
		}

		time = 1;
		while (1)
		{
			if (check(time) == false)
			{
				time *= 2;
			}
			else
			{
				break;
			}
		}
		//printf("--first round end--\n");

		l = time / 2;
		r = time;
		while (l + 1 < r)
		{
			ll m = (l + r) / 2;
			if (check(m) == true)
			{
				r = m;
			}
			else
			{
				l = m;
			}
		}
		//printf("--second round end--\n");
		time = r;
		/*
		for (int i = 0; i < cnt; i++)
		{
			printf("%lf:", a[i] * 0.5);
		}
		printf("\n============\n");
		*/
end:
		printf("Case #%d: %lf\n", tc, time / 2.0);
	}
	return 0;
}
