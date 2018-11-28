#include <stdio.h>
#include <math.h>

#define N 200

int i, j, n, d, sum, pos[N], cnt[N];

int check(double offset)
{
	int i, j, k;
	double start = pos[0] - offset - d;
	for (i = 0; i < n; ++i)
		for (j = 0; j < cnt[i]; ++j)
		{
			if (fabs(start+d - pos[i]) <= offset+1e-6)
			{
				start += d;
				continue;
			}
			double tmp = start;
			if (start+1e-6 <= pos[i]-offset) tmp = pos[i] - offset;
			else if (start >= pos[i]+offset) tmp = pos[i] + offset;
			if (fabs(tmp-start) < d) return 0;
			start = tmp;
		}
	return 1;
}

int main()
{
	int T, TT;
	scanf("%d", &TT);
	for (T = 1; T <= TT; ++T)
	{
		scanf("%d%d", &n, &d);
		sum = 0;
		for (i = 0; i < n; ++i)
		{
			scanf("%d%d", &pos[i], &cnt[i]);
			sum += cnt[i];
		}
		double left = 0, right = 1.*(sum-1)*d;
		while (fabs(left-right) > 1e-8)
		{
			double mid = (left+right)/2;
			if (check(mid)) right = mid; else left = mid;
		}
		printf("Case #%d: %.8lf\n", T, (left+right)/2);
	}
	return 0;
}
