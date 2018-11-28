#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T, Case=1, a[50];
	scanf("%d", &T);
	while(T--)
	{
		int n, i, res=-1, pilea, pileb, suma, sumb, maxn, no, now, j, tmp, bin[20];
		scanf("%d", &n);
		for (i=0; i<n; i++)
		{
			scanf("%d", &a[i]);
		}
		maxn=(int)pow(2.0, n);

		for(i=1; i<maxn; i++)
		{
			no=0;
			now=i;
			pilea=0;
			pileb=0;
			suma=0;
			sumb=0;
			memset(bin, 0, sizeof(bin));
			tmp=0;
			while(now!=0)
			{
				bin[tmp++]=now%2;
				now/=2;
			}
			for(j=0; j<n; j++)
			{
				if(bin[j]==1)
				{
					pilea=pilea^a[j];
					suma+=a[j];
				}
				else
				{
					pileb=pileb^a[j];
					sumb+=a[j];
				}
			}
			if(pilea==pileb && pileb!=0)
			{
				tmp=((suma>sumb)?suma:sumb);
				if(res==-1 || res<tmp) res=tmp;
			}
		}

		printf("Case #%d: ", Case++);
		if (res==-1) printf("NO\n");
		else printf("%d\n", res);
	}
	return 0;
}