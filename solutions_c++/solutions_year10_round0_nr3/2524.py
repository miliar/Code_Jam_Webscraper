#include<stdio.h>

int groupsize[1000];
int firstplace[1000];

int main()
{
	int i,j,sum,start,people,r,n,k,ncase,t,startpos;
	int roundstart,roundend,round;
	scanf("%d",&ncase);
	for(i=1;i<=ncase;i++)
	{
		printf("Case #%d: ",i);
		sum=0;
		scanf("%d%d%d",&r,&k,&n);
		for(j=0;j<n;j++)
		{
			scanf("%d",&groupsize[j]);
			sum+=groupsize[j];
			firstplace[j]=-1;
		}
		if(sum<=k)
		{
			printf("%d\n",sum*r);
			continue;
		}
		sum=0;
		firstplace[0]=0;
		start=0;
		round=0;
		while(1)
		{
			people=0;
			while(people<=k)
			{
				people+=groupsize[start];
				start=(start+1)%n;
			}
			start=(start+n-1)%n;
			people-=groupsize[start];
			round++;
			if(firstplace[start]>=0)
			{
				roundstart=firstplace[start];
				roundend=round;
				round=roundend-roundstart;
				startpos=start;
				break;
			}
			else
			{
				sum+=people;
				firstplace[start]=round;
			}
		}

		sum=0;
		start=0;
		for(j=0;j<roundstart;j++)
		{
			people=0;
			while(people<=k)
			{
				people+=groupsize[start];
				start=(start+1)%n;
			}
			start=(start+n-1)%n;
			people-=groupsize[start];
			sum+=people;
			r--;
		}

		t=0;	
		//r-=roundstart;
		start=startpos;
		for(j=0;j<round;j++)
		{
			people=0;
			while(people<=k)
			{
				people+=groupsize[start];
				start=(start+1)%n;
			}
			start=(start+n-1)%n;
			people-=groupsize[start];
			t+=people;
		}
		if(r%round==0)
		{
			printf("%d\n",r/round*t+sum);
			continue;
		}
		sum=r/round*t+sum;
		start=startpos;
		round=r%round;
		while(round-->0)
		{
			people=0;
			while(people<=k)
			{
				people+=groupsize[start];
				start=(start+1)%n;
			}
			start=(start+n-1)%n;
			people-=groupsize[start];
			sum+=people;
		}
		printf("%d\n",sum);
	}
	return 0;
}