#include <cstdio>
#include <cmath>

using namespace std;



int main()
{//	freopen("al.in","r",stdin);/
//	freopen("al.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int n;
		
		char lastboot='N';
		int ct=0;
		int ocp=1;     //o当前位置 
		int bcp=1;     //B当前位置 
		int time=0;
		
		scanf("%d",&n);
		for(int j=0;j<n;j++)
		{
			char r ;int p;
			getchar();
			scanf("%c%d",&r,&p);
			if(r=='O')
			{
				int move=abs((double)p-ocp);
				ocp=p;
				if(lastboot=='O')
				{
					ct += move+1;
					time += move+1;
				}	
				else
				{
					if(move>time)
					{	
						int tem=move-ct+1;
						time += tem;	
						ct =tem;
					}
					else
					{
					
						if(ct>move)
						{
							time++;
							ct=1;
						}
						else
						{	
							time += (move-ct)+1;
							ct=(move-ct)+1;
						}
					}
				}
//				printf("1XX  %d  %d  %d \n",time,ct,move);
				lastboot='O';
			}
			else
			{
				int move=abs((double)p-bcp);
				bcp=p;
				if(lastboot=='B')
				{
					ct += move+1;
					time += move+1;
				}	
				else
				{
					if(move>time)
					{	
						int tem=move-ct+1;
						time += tem;	
						ct =tem;
					}
					else
					{
					
						if(ct>move)
						{
							time++;
							ct=1;
						}
						else
						{
							
							time += (move-ct)+1;
							ct=(move-ct)+1;
						}
					}
				}
//				printf("2XX  %d  %d  %d \n",time,ct,move);
				lastboot='B';
			}
		
		}	
		printf("Case #%d: %d\n",i+1,time);
	}
	return 0;
}
