#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

#define POSITION 0
#define SEQUENCE 1
#define TIME 2
#define ORNGE 0
#define BL 1

int positiveDifference(int a, int b)
{
	return ((a-b)<0)?(b-a):(a-b);
}

int delay(int a, int b)
{
	int x=0;
	if(b>=a)
		return b-a+1;
	return x;
}

int main() 
{
	int arr_ornge[100][3],arr_bl[100][3];
	int t,ntests,delayBL=0,delayORNGE=0,totalTime=0;
	scanf("%d",&ntests);
	for(t=0;t<ntests;t++)
	{
		delayBL=delayORNGE=totalTime=0;
		char *color;
		int steps,i,temp,currentStepColor,prevStepColor;
		int turnCountBL,turnCountORNGE=turnCountBL=0;
		int currentStepBL=0,currentStepORNGE=0;
		scanf("%d",&steps);
		for(i=0;i<steps;i++)
		{
			scanf("%s %d",color,&temp);
			if(strcmp(color,"O")==0)
			{
				arr_ornge[turnCountORNGE][SEQUENCE]=i;
				arr_ornge[turnCountORNGE][POSITION]=temp;
				if(turnCountORNGE==0)
				{
					arr_ornge[turnCountORNGE][TIME]=arr_ornge[turnCountORNGE][POSITION];
				}
				else
				{
					arr_ornge[turnCountORNGE][TIME]= positiveDifference(arr_ornge[turnCountORNGE-1][POSITION] , arr_ornge[turnCountORNGE][POSITION]) + arr_ornge[turnCountORNGE-1][TIME] + 1;
				}
				turnCountORNGE++;
			}
			else if (strcmp(color,"B")==0)
			{
				arr_bl[turnCountBL][SEQUENCE]=i;
				arr_bl[turnCountBL][POSITION]=temp;
				if(turnCountBL==0)
				{
					arr_bl[turnCountBL][TIME]=arr_bl[turnCountBL][POSITION];
				}
				else
				{
					arr_bl[turnCountBL][TIME]= positiveDifference(arr_bl[turnCountBL-1][POSITION] , arr_bl[turnCountBL][POSITION]) + arr_bl[turnCountBL-1][TIME] + 1;
				}
				turnCountBL++;
			}
		}
		
		for(i=0;i<(turnCountBL+turnCountORNGE);i++)
   		{
			if(arr_ornge[currentStepORNGE][SEQUENCE] < arr_bl[currentStepBL][SEQUENCE] && currentStepORNGE < turnCountORNGE )
			{
				prevStepColor = (i==0)?ORNGE:currentStepColor;
				currentStepColor=ORNGE;
				
				if(currentStepColor==prevStepColor)
					totalTime = arr_ornge[currentStepORNGE][TIME] + delayORNGE;
				else
				{
					delayORNGE = delayORNGE + delay( arr_ornge[currentStepORNGE][TIME] + delayORNGE , totalTime );
					totalTime = arr_ornge[currentStepORNGE][TIME] + delayORNGE;
				}
				currentStepORNGE++;
			}
    		else if ( currentStepBL < turnCountBL )
			{
				prevStepColor = (i==0)?BL:currentStepColor;
				currentStepColor=BL;
				if(currentStepColor==prevStepColor)
					totalTime = arr_bl[currentStepBL][TIME] + delayBL;
				else
				{
					delayBL = delayBL + delay( arr_bl[currentStepBL][TIME] + delayBL , totalTime );
					totalTime = arr_bl[currentStepBL][TIME] + delayBL;
				}
				currentStepBL++;
			}
			else
			{
				prevStepColor = (i==0)?ORNGE:currentStepColor;
				currentStepColor=ORNGE;
				if(currentStepColor==prevStepColor)
					totalTime = arr_ornge[currentStepORNGE][TIME] + delayORNGE;
				else
				{
					delayORNGE = delayORNGE + delay( arr_ornge[currentStepORNGE][TIME] + delayORNGE , totalTime );
					totalTime = arr_ornge[currentStepORNGE][TIME] + delayORNGE;
				}
				currentStepORNGE++;
			}
				
		}
		printf("Case #%d: %d\n",(t+1),totalTime);
			
	}
}
