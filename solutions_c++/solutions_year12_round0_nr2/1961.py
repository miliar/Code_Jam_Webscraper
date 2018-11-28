#include <cstdio>

int main(void)
{
	int T;
	scanf("%d", &T);
	for(int caseN=1;caseN<=T;caseN++)
	{
		int n, s, p;
		int ans=0;
		scanf("%d %d %d", &n, &s, &p);
		for(int i=0;i<n;i++)
		{
			int val;
			scanf("%d", &val);
			if(val/3 + (val%3?1:0) >=p) ans++;
			else
			{
				if(!s) continue;

				if(val%3==0)
				{
					if(val/3 - 1 >=0 && val/3 + 1 <= 10 && val/3 + 1 >= p)
					{
						s--;
						ans++;
					}
				}
				else if (val%3==1) continue;
				else
				{
					if(val/3 + 2 >= p && val/3 + 2 <= 10)
					{
						s--;
						ans++;
					}
				}
			}
		}

		printf("Case #%d: %d\n", caseN, ans);
	}

	return 0;
}
