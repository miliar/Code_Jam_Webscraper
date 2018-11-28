#include <stdio.h>
#include <math.h>

int t, n;
int p[3][3];

double dis(int i, int j)
{
	return (sqrt((p[i][0] - p[j][0]) * (p[i][0] - p[j][0]) + (p[i][1] - p[j][1]) * (p[i][1] - p[j][1])) + p[i][2] + p[j][2]) / 2;
}

double work()
{
	if (n == 1)
	{
		return p[0][2];
	}
	if (n == 2)
	{
		return p[0][2] > p[1][2] ? p[0][2] : p[1][2];
	}
	else if (n == 3)
	{
		double min = 2<<28;
		int r;
		for (int i = 0; i < 2; i++)
		{
			for (int j = i+1; j < 3; j++)
			{
				if (dis(i, j) < min)
				{
					min = dis(i, j);
					r = p[3-i-j][2];
				}

			}
		}
		return min > r ? min : r;
	}
}

int main()
{
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &n);
		for (int j = 0; j < n; j++)
		{
			scanf("%d %d %d", &p[j][0], &p[j][1], &p[j][2]);
		}
		printf("Case #%d: %6lf\n", i+1, work());
	}
}
