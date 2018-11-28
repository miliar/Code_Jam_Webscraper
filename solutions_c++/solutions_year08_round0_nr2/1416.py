//http://code.google.com/codejam/contest/dashboard?c=agdjb2RlamFtcg8LEghjb250ZXN0cxjqOQw
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
struct time_table_t
{
	int start_time;
	int arrive_time;
}table_a[100], table_b[100];
bool flag_a[100], flag_b[100];
bool fcmp(const time_table_t &a, const time_table_t &b)
{
	return a.arrive_time < b.arrive_time;
}
int main()
{
	int ncase;
	int pcase;
	int i;
	int T, na, nb;
	int h1, h2, m1, m2;
	int pa, pb;
	int a_count, b_count;
	int t, min;
	scanf("%d\n", &ncase);
	for (pcase = 1; pcase <= ncase; pcase++)
	{
		a_count = 0;
		b_count = 0;
		memset(flag_a, false, sizeof(flag_a));
		memset(flag_b, false, sizeof(flag_b));
		pa = pb = 0;
		scanf("%d", &T);
		scanf("%d %d\n", &na, &nb);
		for (i = 0; i < na; i++)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			table_a[i].start_time = h1 * 60 + m1;
			table_a[i].arrive_time = h2 * 60 + m2;
		}
		sort(table_a, table_a + na, fcmp);
		for (i = 0; i < nb; i++)
		{
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			table_b[i].start_time = h1 * 60 + m1;
			table_b[i].arrive_time = h2 * 60 + m2;
		}
		sort(table_b, table_b + nb, fcmp);
		while (pa < na || pb < nb)
		{
			if (pa < na && pb < nb)
			{
				if (table_a[pa].arrive_time < table_b[pb].arrive_time)
				{
					min = 2000000000;
					t = -1;
					for (i = pb; i < nb; i++)
					{
						if (table_b[i].start_time >= table_a[pa].arrive_time + T && !flag_b[i] && table_b[i].start_time < min)
						{
							min = table_b[i].start_time;
							t = i;
						}
					}
					if (t > -1)
						flag_b[t] = true;
					if (!flag_a[pa]) a_count++;
					pa++;
				}else
				{
					min = 2000000000;
					t = -1;
					for (i = pa; i < na; i++)
					{
						if (table_a[i].start_time >= table_b[pb].arrive_time + T && !flag_a[i] && table_a[i].start_time < min)
						{
							min = table_a[i].start_time;
							t = i;
						}
					}
					if (t > -1)
						flag_a[t] = true;
					if (!flag_b[pb]) b_count++;
					pb++;
				}
			}else
			{
				if (pa < na)
				{
					if (!flag_a[pa]) a_count++;
					pa++;
				}else if (pb < nb)
				{
					if (!flag_b[pb]) b_count++;
					pb++;
				}
			}
		}
		printf("Case #%d: %d %d\n", pcase, a_count, b_count);
	}	
	return 0;
}