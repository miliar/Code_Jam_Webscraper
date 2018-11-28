#include<stdio.h>

int main()
{
	freopen("A.in","rt",stdin);
	freopen("A.out","wt",stdout);
	int cases,kase;
	scanf("%d", &cases);
	for(kase=1; kase<=cases; kase++)
	{
		int N;
		char cur_bot[3]="A";
		int B_loc=1, O_loc=1;
		long total_time=0;
		long B_tstate=0, O_tstate=0;
		scanf("%d",&N);
		for(int i=0; i<N; i++)
		{
			char bot[3];
			int loc;
			scanf("%s %d",bot,&loc);
			if(cur_bot[0]==bot[0])
			{
				if(bot[0]=='B')
				{
					long LOC = loc-B_loc;
					B_tstate+=(LOC>=0)?(1+LOC):(1-LOC);
					total_time= B_tstate;
					B_loc=loc;
				}
				else
				{
					long LOC = loc-O_loc;
					O_tstate+=(LOC>=0)?(1+LOC):(1-LOC);
					total_time= O_tstate;
					O_loc=loc;
				}				
			}
			else
			{
				cur_bot[0]=bot[0];
				if(cur_bot[0]=='B')
				{
					long LOC = loc-B_loc;
					B_tstate+=(LOC>=0)?(1+LOC):(1-LOC);
					if(B_tstate<=O_tstate)
					{					
						B_tstate=O_tstate+1;						
					}
					total_time= B_tstate;
					B_loc=loc;
				}
				else
				{
					long LOC = loc-O_loc;
					O_tstate+=(LOC>=0)?(1+LOC):(1-LOC);
					if(O_tstate<=B_tstate)
					{					
						O_tstate=B_tstate+1;						
					}
					total_time= O_tstate;
					O_loc=loc;
				}
			}
		}
		printf("Case #%d: %ld\n",kase, total_time);
	}
	return 0;
}