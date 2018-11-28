#include <cstdio>

const int MAXN = 550;

int s[MAXN], n, sum;

void work()
{
	sum = 0;
	scanf("%d", &n);
	for(int i = 0; i < n; i ++)
	{
		scanf("%d", s + i);
		sum += s[i];
	}
	double ave = (double)(sum * 2) / n;
	int m = n;
	double newave = sum * 2;
	for(int i = 0; i < n; i ++)
		if((double)s[i] >= ave) 
		{
			m --;
			newave -= s[i];
		}
	newave /= m;
	for(int i = 0; i < n; i ++)
	{
		double ans = (newave - s[i]) / sum;
		if(ans < 0) ans = 0;
		printf("%.6lf ", ans * 100);
	}
}

int main() 
{
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i ++)
	{
		printf("Case #%d: ", i);
		work();
		printf("\n");
	}
	return 0;
}
