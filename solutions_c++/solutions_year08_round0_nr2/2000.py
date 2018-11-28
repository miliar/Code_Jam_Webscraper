#include <stdio.h>
#include <string.h>
#include <algorithm>
#define MAXN 105
using namespace std;

struct hour
{
	int h, m;
};
hour hadep[MAXN], haarr[MAXN], hbdep[MAXN], hbarr[MAXN];

int ncases, na, nb, t, mina, minb;

bool compare(hour a, hour b)
{
	return (a.h<b.h || (a.h==b.h && a.m<=b.m));
}

hour sumtime(hour a, int mins)
{
	a.m+=mins;
	a.h+=a.m/60;
	a.m%=60;
	return a;
}

void go()
{
	int i, j=0;
	mina=0; minb=0;
	
	for(i=0; i<na; i++)
	{
		if(j>=nb)
			mina++;
		
		if(compare(sumtime(hbarr[j], t), hadep[i]))
			j++;
		else
			mina++;
	}
	
	j=0;
	for(i=0; i<nb; i++)
	{
		if(j>=na)
			minb++;
			
		if(compare(sumtime(haarr[j], t), hbdep[i]))
			j++;
		else
			minb++;
	}
}

int main()
{
	int i, j;
	scanf("%d", &ncases);
	for(i=0; i<ncases; i++)
	{
		memset(hadep, 0, MAXN), memset(haarr, 0, MAXN), memset(hbdep, 0, MAXN), memset(hbarr, 0, MAXN);
		scanf(" %d %d %d", &t, &na, &nb);
		for(j=0; j<na; j++)
			scanf(" %d:%d %d:%d", &hadep[j].h, &hadep[j].m, &haarr[j].h, &haarr[j].m);
		for(j=0; j<nb; j++)
			scanf(" %d:%d %d:%d", &hbdep[j].h, &hbdep[j].m, &hbarr[j].h, &hbarr[j].m);
		sort(hadep, hadep+na, compare);
		sort(haarr, haarr+na, compare);
		sort(hbdep, hbdep+nb, compare);
		sort(hbarr, hbarr+nb, compare);
		go();
		printf("Case #%d: %d %d\n", i+1, mina, minb);
	}
	return 0;
}
