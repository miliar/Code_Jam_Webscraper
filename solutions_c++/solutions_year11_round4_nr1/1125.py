#include <iostream>
#include <cstdio>
#include <algorithm>
#define eps 1e-9
using namespace std;
struct data
{
	int len;
	int ws;
	bool friend operator < (struct data a,struct data b)
	{
		if (a.ws<b.ws) return 1;
		else return 0;
	}
}wway[1100];

int main()
{
	int tt;
	scanf("%d",&tt);
	for (int tc=1;tc<=tt;tc++)
	{
		int clen,walks,runs,runtm,n;
		scanf("%d %d %d %d %d",&clen,&walks,&runs,&runtm,&n);
		int sum=0;
		for (int i=0;i<n;i++)
		{
			int b,e,w;
			scanf("%d %d %d",&b,&e,&w);
			wway[i].len=e-b;
			wway[i].ws=w;
			sum+=wway[i].len;
		}
		wway[n].len=clen-sum;
		wway[n].ws=0;
		sort(wway,wway+n+1);
		double tt=0,tl=runtm;
		for (int i=0;i<=n;i++)
		{
			if (tl>wway[i].len/(double)(wway[i].ws+runs))
			{
				tl-=wway[i].len/(double)(wway[i].ws+runs);
				tt+=wway[i].len/(double)(wway[i].ws+runs);
			}
			else if (tl>eps)
			{
				tt+=(wway[i].len-tl*(double)(wway[i].ws+runs))/(double)(wway[i].ws+walks)+tl;
				tl=0;
			}
			else
				tt+=wway[i].len/(double)(wway[i].ws+walks);

		}
		printf("Case #%d: %.7lf\n",tc,tt);


	}
    return 0;
}
