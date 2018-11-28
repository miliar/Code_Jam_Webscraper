#include <stdio.h>
#include <string.h>

int x[200];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T, Case=1;
	scanf("%d", &T);
	while(T--)
	{
		int n, l, h, i, j, ok, found=0;
		scanf("%d%d%d", &n, &l, &h);
		for (i=0;i<n;i++)
		{
			scanf("%d", &x[i]);
		}
		for (i=l; i<=h; i++)
		{
			ok=1;
			for (j=0;j<n;j++)
			{
				if( (x[j]<i && i%x[j]==0) || (x[j]>=i && x[j]%i==0) ) continue;
				else { ok=0; break; }
			}
			if(ok==1) { found=1; break; }
		}
		printf("Case #%d: ", Case++);
		if(found==1) printf("%d\n", i);
		else printf("NO\n");
	}
	return 0;
}