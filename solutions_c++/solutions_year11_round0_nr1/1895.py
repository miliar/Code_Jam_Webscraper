//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

int cnt_a, cnt_b;
int a[102], b[102];
int order_a[102], order_b[102];

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w",  stdout);
#endif

	int n, pos, i, j;
	int T;
	char o[2];
	int time_a, time_b, ahead_a, ahead_b;

	scanf("%d", &T);
	for (int t = 1; t <= T; ++t)
	{
		cnt_a = cnt_b = 1;
		scanf("%d", &n);
		a[0]=b[0]=1;
		for (i = 0; i < n; ++i)
		{
			scanf("%s %d", o, &pos);
			if (o[0] == 'B')
			{
				order_b[cnt_b] = i;
				b[cnt_b++] = pos;				
			} else
			{
				order_a[cnt_a] = i;
				a[cnt_a++] = pos;
			}
		}
		a[cnt_a] = a[cnt_a-1];
		b[cnt_b] = b[cnt_b-1];
		order_a[cnt_a] = n + 1;
		order_b[cnt_b] = n + 1;

		i = 1; j = 1;
		int total = 0;
		time_a = time_b = 0;
		while (i < cnt_a || j < cnt_b)
		{			
			bool first = true;
			if (order_a[i] < order_b[j])
			{
				time_a = 0;
				while (i < cnt_a && order_a[i] < order_b[j])
				{
					if (first)
					{
						first= false;
						time_a += max(0, abs(a[i] - a[i-1]) - time_b) + 1;
					}
					else
						time_a += abs(a[i] - a[i-1]) + 1;
					++i;
				}
				total += time_a;
			}
			else
			{
				time_b = 0;
				while (j < cnt_b && order_b[j] < order_a[i])
				{
					if (first)
					{
						time_b += max(0, abs(b[j] - b[j-1]) - time_a) + 1;
						first = false;
					} else
					time_b += abs(b[j] - b[j-1]) + 1;
					++j;
				}
				total += time_b;
			}
			
		}
		printf("Case #%d: %d\n", t, total);
	}

	return 0;
}