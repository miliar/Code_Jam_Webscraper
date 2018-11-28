#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int t, test, na, nb, pa[128], pb[128], sa[128], sb[128], recul, sola, solb, i, j, first;
	char line[32];
	
	scanf("%d", &t);

	for(test = 1; test <= t; ++test)
	{
		scanf("%d ", &recul);
		scanf("%d %d ", &na, &nb);
		for(i = 1; i <= na; ++i)
		{
			fgets(line, 32, stdin);
			for(j = 0; j < 32; ++j)
			{
				line[j] -= '0';
			}
			pa[i] = (line[0] * 10 + line[1]) * 60 + line[3] * 10 + line[4];
			sa[i] = (line[6] * 10 + line[7]) * 60 + line[9] * 10 + line[10] + recul;
		}
		for(i = 1; i <= nb; ++i)
		{
			fgets(line, 32, stdin);
			for(j = 0; j < 32; ++j)
			{
				line[j] -= '0';
			}
			pb[i] = (line[0] * 10 + line[1]) * 60 + line[3] * 10 + line[4];
			sb[i] = (line[6] * 10 + line[7]) * 60 + line[9] * 10 + line[10] + recul;
		}
		sort(pa + 1, pa + na + 1);
		sort(sa + 1, sa + na + 1);
		sort(pb + 1, pb + nb + 1);
		sort(sb + 1, sb + nb + 1);
		first = 1;
		sola = solb = 0;
		sb[nb + 1] = sa[na + 1] = 100000;
		for(i = 1; i <= na; ++i)
		{
			if(pa[i] < sb[first])
			{
				++sola;
			}
			else
			{
				++first;
			}
		}
		first = 1;
		for(i = 1; i <= nb; ++i)
		{
			if(pb[i] < sa[first])
			{
				++solb;
			}
			else
			{
				++first;
			}
		}
		printf("Case #%d: %d %d\n", test, sola, solb);
	}

	return 0;
}
