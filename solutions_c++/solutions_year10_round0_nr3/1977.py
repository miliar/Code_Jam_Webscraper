#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int		ca=1;

int	cas;
long long runs, max_p, n;
long long	p[1010];

long long	e[1010];
long long pos[1010];
long long each[1010];

long long ans;

void run()
{
	ans = 0;

	int i, j, k;
	
	long long step = 0;
	int index = 0;
	long long total = 0;
	long long before_loop = 0;
	int before_loop_runs;

	each[0] = 0;
	do
	{
		if (e[index] != -1)
		{
			before_loop = e[index];
			before_loop_runs = pos[index];
			break;
		}
		e[index] = total;
		pos[index] = step;

		each[step] = total;

		step++;		

		int people = 0;
		for (i=0; i<n; i++)
		{
			if (people + p[index] <= max_p)
			{
				people += p[index];
			}
			else
				break;
			index = (index + 1) % n;
		}
		total += people;				
	} while (true);
	

	runs -= before_loop_runs;
	step -= before_loop_runs;
	long long a = runs / step;
	long long b = runs % step;
		
	ans = a * (total - before_loop) + before_loop;

	// after loop
	for (j=0; j<b; j++)
	{
		int people = 0;
		for (i=0; i<n; i++)
		{
			if (people + p[index] <= max_p)
			{
				people += p[index];
			}
			else
				break;
			index = (index + 1) % n;
		}
		ans += people;	
	}
}

int main() 
{    
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	scanf("%d", &cas);
	for (int i=0; i<cas; i++)
	{
		scanf("%lld %lld %lld", &runs, &max_p, &n);
		for	(int j=0; j<n; j++)
			scanf("%lld", p+j);

		memset(e, 0xff, sizeof(e));
		run();

		printf("Case #%d: %lld\n", ca++, ans);
	}
	return 0;
}