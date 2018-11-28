#include <stdio.h>
#include <math.h>

int prizes[12][1<<12];
int P;
int M[1<<12];
bool there(int k,int i,int j)
{
	int stepsize=(1<<(i+1));
	if(k/stepsize==j)
		return 1;
	return 0;
}

int main()
{
	
	
	
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&P);
		for(int i=0;i<(1<<P);i++)
		{
			scanf("%d",&M[i]);
			M[i]=P-M[i];
		}
		
		
		int answer=0;
		
		for(int i=P-1;i>=0;i--)
		{
			
			
			for(int j=0;j<(1<<(P-1-i));j++)
			{
				int tot=0;
				for(int k=0;k<(1<<P);k++)
				{
					if(there(k,i,j) && M[k]>0)
					{
						tot++;
						M[k]--;
					}
				}
				if(tot>0)
					answer++;
			}
		}
		
		printf("Case #%d: %d\n",t,answer);
		
		//for(int i=0;i<(1<<P);i++)
		//	printf("%d ",M[i]);
		
		for(int i=0;i<P;i++)
		{
			for(int j=0;j<(1<<(P-i-1));j++)
				scanf("%d",&prizes[i][j]);
		}
		
		
	}
}