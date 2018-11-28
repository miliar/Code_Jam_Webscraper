#include <stdio.h>
#include <stdlib.h>

class interval
{
public:
	int length;
	int speed;
};

int cmp(const void *a, const void *b)
{
	interval *c = (interval *)a;
	interval *d = (interval *)b;
	if(c->speed > d->speed)
		return 1;
	return -1;
}


int main()
{
	double ans,t;
	interval ttt[1002];
	int x,s,r,n,i;
	int start,end,w;
	int cas,asd;
	int total;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		scanf("%d %d %d %lf %d",&x,&s,&r,&t,&n);
		total = 0;
		for(i=0;i<n;i++)
		{
			scanf("%d %d %d",&start,&end,&w);
			ttt[i].length = end - start;
			total += ttt[i].length;
			ttt[i].speed = w;

		}
		ttt[n].length = x - total;
		ttt[i].speed = 0;
		n++;

/*		ans = 0;
		for(i=0;i<n;i++)
		{
			ans += (double) (ttt[i].length / (ttt[i].speed + s));
		}
		if(ans < t)
		{
			ans = (double)x / ((double)( x / ans ) + r - s);
		}
		else
		{
			ans = (double) (x - (r-s)*t) /  (double)( x / ans );
		}*/

		
		printf("Case #%d: ",asd+1);

		

		qsort((void *)ttt,n,sizeof(ttt[i]),cmp);

		
		
		ans = 0;
		for(i=0;i<n;i++)
		{
			double tmp = (double)(ttt[i].length / (double)(ttt[i].speed + r));
			if(tmp < t)
			{
				ans += tmp;
				t -= tmp;
			}
			else
			{
				ans += t;
				ans += (double)(ttt[i].length - (t * (ttt[i].speed + r))) / (double)(ttt[i].speed + s);
				t = 0;
			}
		}
	
		printf("%.6lf\n",ans);

	}
	return 0;
}
