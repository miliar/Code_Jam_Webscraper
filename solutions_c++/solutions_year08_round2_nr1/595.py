#include<stdio.h>
struct node
{
	__int64 x, y;
}no[100005];
int main()
{
	__int64 N, a, b, c, d, m, n, i, j, k, t, l, number;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%I64d", &N);
	for(i=1; i<=N; i++)
	{
		scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d", &n, &a, &b, &c, &d, &no[0].x, &no[0].y, &m);
		for(j=1; j<n; j++)
		{
			no[j].x = (a * no[j-1].x + b) % m;
			no[j].y = (c * no[j-1].y + d) % m;
		}
		number = 0;
		for(k=0; k<n; k++)
		{
			for(t=(k+1); t<n; t++)
			{
				for(l=(t + 1); l<n; l++)
				{
					/*xx = (no[k].x + no[t].x + no[l].x) * 1.0/ 3;
					yy = (no[k].y + no[t].y + no[l].y) * 1.0/ 3;*/
					if((no[k].x + no[t].x + no[l].x) % 3 == 0 && (no[k].y + no[t].y + no[l].y) % 3 == 0)
					{
						number ++;
					}
					
				}
			}
		}
		printf("Case #%I64d: %I64d\n", i, number);
	}
	return 0;
}