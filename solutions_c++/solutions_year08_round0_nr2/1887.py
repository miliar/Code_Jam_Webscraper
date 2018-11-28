#include<stdio.h>
#include <string.h>
int maxa, maxb, leva[24*60], levb[24*60], reca[24*60], recb[24*60], tr, na, nb;

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.out","w",stdout);
	int n;
	scanf("%d", &n);
	int tt = 0;
	while (n--)
	{
		tt++;
		memset(leva,0,sizeof(leva));
		memset(levb,0,sizeof(levb));
		memset(reca,0,sizeof(reca));
		memset(recb,0,sizeof(recb));
		scanf("%d", &tr);
		scanf("%d%d", &na, &nb);

		int i, m, h;
		char c;
		for(i = 0; i < na; i++)
		{
			scanf("%d%c%d", &h, &c, &m);
			int time = h * 60 + m;
			leva[time]++;
			scanf("%d%c%d", &h, &c, &m);
			time = h * 60 + m + tr;
			recb[time]++;
		}

		for (i = 0; i < nb; i++)
		{
			scanf("%d%c%d", &h, &c, &m);
			int time = h * 60 + m;
			levb[time]++;
			scanf("%d%c%d", &h, &c, &m);
			time = h * 60 + m + tr;
			reca[time]++;
		}

		int nowa, nowb;
		for (nowa = 0,nowb = 0,maxa = 0,maxb = 0,i = 0; i < 1440; i++)
		{
			nowa = leva[i] - reca[i] + nowa;
			maxa = maxa > nowa ? maxa : nowa;

			nowb = levb[i] - recb[i] + nowb;
			maxb = maxb > nowb ? maxb : nowb; 
		}

		printf("Case #%d: %d %d\n",tt,maxa,maxb);
	}

	return 0;
}
