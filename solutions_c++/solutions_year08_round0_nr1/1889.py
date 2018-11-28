#include<stdio.h>
#include <string.h>

char ss[109][100], sq[1009][100], flg[109];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	int n, m = 0 ;
	scanf("%d",&n);
	while (n--)
	{
		m++;
		int s, q, i, j;
		scanf("%d",&s);
		gets(ss[0]);
		for (i = 0; i < s; i++)
		{
			gets(ss[i]);
		}
		scanf("%d",&q);
		gets(sq[0]);

		int count = 0, f = 0;
		memset(flg, 0, sizeof(flg));
		for (i = 0; i < q; i++)
		{
			gets(sq[i]);
			for (j = 0; j <s;j++)
			{
				if(strcmp(ss[j],sq[i]) == 0)
				{
					if (flg[j] ==0)
					{
						flg[j] = 1;
						f++;
					}
					break;
				}
			}
			if (f == s)
			{
				count++;
				f = 1;
				memset(flg, 0 ,sizeof(flg));
				flg[j] = 1;
			}
		}

		printf("Case #%d: %d\n",m,count);
	}
	return 0;
}