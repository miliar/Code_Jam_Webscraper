#include <stdio.h>
#include <string.h>

int g[1000];
long long m[1000];
int c[1000];

int n,k,r;

main()
{


	
	int t;
	scanf("%d\n", &t);
	for (int time = 0; time < t; ++time)
	{
		memset(m, 0xff, sizeof(m));
		scanf("%d %d %d\n", &r, &k, &n);
		long long sum = 0;
		long long res = 0;
		for (int i = 0; i < n; ++i)
		{
			scanf("%d", &g[i]);
			sum += g[i];
		}
		if (sum <= k) 
		{
			res = sum;
			res *= r;
			printf("Case #%d: %lld\n", time+1, res);
			continue;
		}
		//continue;
		c[0] = 0;	
		m[0] = 0;
		int round = 0;
		int st = 0;
		long long money = 0;
		bool jmp = true;
		while (round < r)
		{
			int en = st; 
			sum = 0; 
			while ( (sum + g[en])<= k)
			{
				sum += g[en];
				en++;
				if (en == n) en = 0;
			}
			//printf("round: %d st: %d\n", round, st);
			if (!jmp)
			{
				money += sum;
				st = en;
				round++;
				continue;
			}
			
			if (m[en] == -1)
			{
				money += sum;
				m[en] = money;
				c[en] = c[st] + 1;
				st = en;
				round++;
			}
			else 
			{
				//printf("%d %d\n",round ,en);
				int length = c[st] - c[en] + 1;
				long long cm = m[st] - m[en] + sum;
				int rep = (r - c[en]) / length;
				money = cm;
				money *= rep;
				money += m[en];
				int rem = r - c[en] - length * rep;
				
				round = 0;
				r = rem;
				jmp = false;
				st = en;				
			
			} 
		}
		printf("Case #%d: %lld\n", time+1, money);
	}
	
	return 0;
}
