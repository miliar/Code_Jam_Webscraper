#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d",&t);
	for (int i = 0; i < t; ++i)
	{
		int n,s,p, a_c=0,tmp;
		int count = 0;
		scanf("%d%d%d", &n, &s, &p);
		for (int j = 0; j < n; ++j)
		{
			scanf("%d",&tmp);
			if (!p){++count; continue;}
			if (!tmp)
			{
				if (!p) ++count;
				continue;
			}
			double q = tmp/3.0;
			int f_q = floor(q);
			if (fabs(f_q - q) < .00000001)
			{
				if (q >= p)
					++count;
				else if (s && q+1 >= p)
					--s, ++count;
			}
			else
			{
				if (f_q + 1 >= p)
					++count;
				else if (s && f_q+2 >= p && f_q != floor(q+.5))
					--s, ++count;
			}
		}
		printf("Case #%d: %d\n", i+1, count);
	}
	return 0;
}