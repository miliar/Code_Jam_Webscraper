#include <stdio.h>
#include <stdlib.h>

class event
{
public:
	int time;
	int enter;
	int mode;
};


event ev[2000];

int cmp(const void *a,const void *b)
{
	if( ((event *)a)->time > ((event *)b)->time )
		return 1;
	else if(((event *)a)->time < ((event *)b)->time )
		return -1;
	if(((event *)a)->enter < ((event *)b)->enter )
		return 1;
	else if(((event *)a)->enter > ((event *)b)->enter )
		return -1;
	return 0;
}

int main()
{
	int turn;
	int cas,asd;
	int i,A,B;
	int x,y;
	int ind;
	int ta,tb;
	int ans_a,ans_b;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		ind=0;
		scanf("%d",&turn);
		scanf("%d %d",&A,&B);
		for(i=0;i<A;i++)
		{
			scanf("%d:%d",&x,&y);
			ev[ind].time = x*60 + y;
			ev[ind].mode = 0;
			ev[ind].enter = 0;
			ind++;
			scanf("%d:%d",&x,&y);
			ev[ind].time = x*60 + y + turn;
			ev[ind].mode = 0;
			ev[ind].enter = 1;
			ind++;
		}
		for(i=0;i<B;i++)
		{
			scanf("%d:%d",&x,&y);
			ev[ind].time = x*60 + y;
			ev[ind].mode = 1;
			ev[ind].enter = 0;
			ind++;
			scanf("%d:%d",&x,&y);
			ev[ind].time = x*60 + y + turn;
			ev[ind].mode = 1;
			ev[ind].enter = 1;
			ind++;
		}
		qsort((void *)ev,ind,sizeof(ev[0]),cmp);
		ans_a=ans_b=ta=tb=0;
		for(i=0;i<ind;i++)
		{
			if(ev[i].enter==0)
			{
				if(ev[i].mode==0)  /* from A to B */
				{
					if(ta==0)
						ans_a++;
					else
						ta--;
				}
				else /* from B to A */
				{
					if(tb==0)
						ans_b++;
					else
						tb--;
				}
			}
			else
			{
				if(ev[i].mode==0) /* from A to B */
					tb++;
				else /* from B to A */
					ta++;
			}
		}
		printf("Case #%d: %d %d\n",asd+1,ans_a,ans_b);
	}
	return 0;
}
