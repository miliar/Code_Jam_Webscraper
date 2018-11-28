#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define ABS(a) ((a)<0?(-(a)):(a))
struct people
{
	int t, per, rdc, tg;
}pep[200];
int p;

bool cmp(const people a, const people b)
{
	return (a.per == b.per ? (a.rdc>b.rdc) : (a.per<b.per));
}

bool cmpx(const people a, const people b)
{
	return (a.rdc == b.rdc ? (a.per < b.per) : (a.rdc > b.rdc));
}

int main()
{
	int d, T, n, s, i, sum;
	scanf("%d", &T);
	for(d=1; d<=T; d++)
	{
		scanf("%d%d%d", &n, &s, &p);
		for(i=0; i<n; i++)
		{
			scanf("%d", &pep[i].t);
			pep[i].per = pep[i].t / 3;
			pep[i].rdc = pep[i].t % 3;
			pep[i].tg = 0;
		}
		sort(pep, pep+n, cmpx);
		for(i=0; s && i<n; i++)
		{
			if(pep[i].per - p > -3 && pep[i].per - p < 0)
			{
				switch(pep[i].rdc)
				{
					case 0:
					case 1: if(pep[i].per && p-pep[i].per == 1)
							{
								pep[i].per++;
								pep[i].tg = 1;
								s--;
							}break;
					case 2: if(p-pep[i].per == 2)
							{
								pep[i].per += 2;
								pep[i].tg = 1;
								s--;
							}
				}
			}
		}
	//	sort(pep, pep+n, cmp);
		for(i=0; s--; i++)
		{
		//	printf("---%d %d %d\n",pep[i].t, pep[i].per,pep[i].rdc);
			if(!pep[i].tg)
			switch(pep[i].rdc)
			{
				case 0: 
				case 1: if(pep[i].per) pep[i].per++;
						break;
				case 2: pep[i].per+=2; break;
			}
		//	printf("---%d %d %d\n",pep[i].t, pep[i].per,pep[i].rdc);
		}
	//	printf("==\n");
		for(; i<n ;i++)
		{
			if(!pep[i].tg && pep[i].per && pep[i].rdc)
				pep[i].per++;
	//		printf("---%d %d %d\n",pep[i].t, pep[i].per,pep[i].rdc);
		}
		sum = 0;
		for(i=0; i<n; i++)
			if(pep[i].per >= p) sum++;
		printf("Case #%d: %d\n", d, sum);
	}
	return 0;
}
