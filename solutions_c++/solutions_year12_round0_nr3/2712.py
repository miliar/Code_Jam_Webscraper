#include <stdio.h>
#include <string.h>

int main()
{
	int n, d, i, a, b, sum, t, k, len, cnt, tt;
	char na[10], nb[10], nt[20];
	scanf("%d", &n);
	for(d=1; d<=n; d++)
	{
		scanf("%d%d", &a, &b);
		sum = 0;
		for(t=a; t<=b; t++)
		{
			sprintf(nt, "%d", t);
			len = strlen(nt);
			nt[len] = cnt = 0;
			for(i=1; i<len; i++)
			{
				nt[i+len-1] = nt[i-1];
				nt[i+len] = 0;
				sscanf(nt+i, "%d", &tt);
				if(t == tt) break;
				if(tt >= a && tt <= b)	cnt++;
			}
			sum += cnt;//(1+cnt)*cnt/2;
		}
		printf("Case #%d: %d\n", d, sum/2);
	}
	return 0;
}
