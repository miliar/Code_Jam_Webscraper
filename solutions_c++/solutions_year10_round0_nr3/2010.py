#include <cstdio>
#include <cstring>
#define MAXN 1010

long long int t, maxpeople, runs, ngroups, ridenum[MAXN], earned[MAXN], groups[MAXN], cyclenum, cyclemoney, totalmoney, curpos;

int main()
{
	scanf("%lld", &t);
	for(int i=0; i<t; i++)
	{
		totalmoney=0;
		memset(groups, 0, sizeof(groups));
		memset(ridenum, -1, sizeof(ridenum));
		memset(earned, -1, sizeof(earned));
		cyclenum=cyclemoney=-1;
		scanf("%lld %lld %lld", &runs, &maxpeople, &ngroups);
		for(int j=0; j<ngroups; j++)
			scanf("%lld", &groups[j]);
	
		ridenum[0]=0;
		earned[0]=0;
		curpos=0;
		
		while(runs>0)
		{
			long long int peoplein=0, j=curpos;
			while(true)
			{
				if(peoplein>0 && j==curpos)
					break;
				if(peoplein+groups[j]>maxpeople)
					break;
				
				peoplein+=groups[j];
				j=(j+1)%ngroups;
			}
			runs--;
			totalmoney+=peoplein;
			
			if(earned[j]!=-1) //cycle found
			{
				cyclenum=ridenum[curpos]+1-ridenum[j];
				cyclemoney=earned[curpos]+peoplein-earned[j];
				totalmoney+=(cyclemoney*(runs/cyclenum));
				runs%=cyclenum;
				curpos=j;
				break;
			}
			else
			{
				earned[j]=earned[curpos]+peoplein;
				ridenum[j]=ridenum[curpos]+1;
			}
			curpos=j;
		}
		while(runs>0)
		{
			long long int peoplein=0, j=curpos;
			while(true)
			{
				if(peoplein>0 && j==curpos)
					break;
				if(peoplein+groups[j]>maxpeople)
					break;
				
				peoplein+=groups[j];
				j=(j+1)%ngroups;
			}
			curpos=j;
			runs--;
			totalmoney+=peoplein;
		}
		printf("Case #%d: %lld\n", i+1, totalmoney);
	}
	return 0;
}
