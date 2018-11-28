#include <stdio.h>

const int T = 50;
const int P = 10;

main()
{
	int t;
	int p;
	int m[1<<P];
	int ans, need;
	scanf("%d", &t);
	for (int i=1;i<=t;i++)
	{
		ans=0;
		
		scanf("%d", &p);
		for (int j=0;j<(1<<p);j++)
		{
			scanf("%d", &m[j]);
			m[j]=p-m[j];
		}
		for (int j=p-1;j>=0;j--)
			for (int k=0;k<(1<<j);k++)
				scanf("%*d");
		
		for (int j=0;j<p;j++)
		{
			for (int k=0;k<(1<<j);k++)
			{
				need=0;
				for (int l=(1<<(p-j))*k;l<(1<<(p-j))*(k+1);l++)
					if (m[l]>0)
						need=1;
				if (need)
				{
					for (int l=(1<<(p-j))*k;l<(1<<(p-j))*(k+1);l++)
						m[l]--;
					ans++;
				}
			}
		}
		
		printf("Case #%d: %d\n", i, ans);
	}
}
