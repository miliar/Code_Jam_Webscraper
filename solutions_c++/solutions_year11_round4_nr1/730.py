#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>

using namespace std;

const int MAX = 1023;
const double eps = 1e-12;

int begin[MAX], end[MAX], vel[MAX], lenght[MAX];

void swap(int i)
{
	int t;
	t = lenght[i];
	lenght[i] = lenght[i + 1];
	lenght[i + 1] = t;
	t = vel[i];
	vel[i] = vel[i + 1];
	vel[i + 1] = t;
	return;
}

void sortt(int n)
{
	int i, j;
	for(i = 1; i < n; i++)
		for(j = 0; j < n - 1; j++)
			if(vel[j] > vel[j + 1])
				swap(j);
	return;
}

int main()
{
	int i, t, n, j, l, s, r, x, k;
	double ans, time, ti;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &k);
	for(i = 1; i <= k; i++)
	{
		scanf("%d", &x);
		scanf("%d %d %d %d", &s, &r, &t, &n);
		for(j = 0; j < n; j++)
			scanf("%d %d %d", begin + j, end + j, vel + j);
		l = 0;
		for(j = 0; j < n; j++)
		{
			lenght[j] = end[j] - begin[j];
			l += lenght[j];
		}
		time = t;
		lenght[n] = x - l;
		vel[n] = 0;
		n++;
		sortt(n);
		j = 0;
		ans = 0;
		while( (time > eps) && (j < n) )
		{
			ti = (lenght[j] * 1.0) / (r + vel[j]);
			if(ti < time)
			{
				time -= ti;
				ans += ti;
				j++;
			}
			else
			{
				ans += time + (lenght[j] - ((r + vel[j]) * time) * 1.0) / (s + vel[j]);
				time = 0;
				j++;
			}
		}
		while(j < n)
		{
			ans += (1.0 * lenght[j]) / (s + vel[j]);
			j++;
		}
		printf("Case #%d: %.7lf\n", i, ans);
	}
    return 0;
}
