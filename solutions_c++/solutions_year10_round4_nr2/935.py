#include <stdio.h>

const int PMAX = 10;

int m[1100], p, ans;

void process()
{
	int i, j, k, step;

	ans = 0;
	for(i = p; i > 0; i--)
	{
		step = (1<<i);
		for(j = 0; j < (1<<p)/step; j++)
		{
			for(k = j*step; k < (j+1)*step; k++)
				if(m[k] > 0) break;
			if(k < (j+1)*step)
			{
				ans++;
				for(k = j*step; k < (j+1)*step; k++)
					m[k]--;
			}
		}
	}
}

int main()
{
	int t, i, j, temp, z = 1;
	
	scanf("%d", &t);
	while(t > 0)
	{
		scanf("%d", &p);
		for(i = 0; i < (1<<p); i++)
		{
			scanf("%d", &m[i]);
			m[i] = p - m[i];
		}
		for(i = 0; i < p; i++)
			for(j = 0; j < (1<<i); j++)
				scanf("%d", &temp);
		process();
		printf("Case #%d: %d\n", z++, ans);
		t--;
	}
	return 0;
}