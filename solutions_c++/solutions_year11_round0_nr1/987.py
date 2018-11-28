#include<stdio.h>

int main()
{
  int nTests;
  scanf("%d",&nTests);
  for(int i=0;i<nTests;i++)
	{
	  int nSteps;
	  scanf("%d",&nSteps);
	  long long prevOTime = 0;
	  long long prevBTime = 0;
	  long long prevTime = 0;
	  int prevOBut = 1;
	  int prevBBut = 1;
	  for(int j=0;j<nSteps;j++)
		{
		  char curRob[2];int curBut;
		  scanf("%s",curRob);
		  scanf("%d",&curBut);
		  if(curRob[0] == 'O')
			{
			  int diff=0;
			  if(curBut < prevOBut)
				{
				  diff = prevOBut - curBut;
				}
			  else
				{
				  diff = curBut - prevOBut;
				}
			  int TimeChange = diff + 1;
			  long long curOTime = prevOTime + TimeChange;
			  if(curOTime <= prevTime) 
				{
				  curOTime = prevTime+1;
				}
			  prevTime = curOTime;
			  prevOTime = curOTime;
			  prevOBut = curBut;
			}
		  else
			{
			   int diff=0;
			  if(curBut < prevBBut)
				{
				  diff = prevBBut - curBut;
				}
			  else
				{
				  diff = curBut - prevBBut;
				}
			  int TimeChange = diff + 1;
			  long long curBTime = prevBTime + TimeChange;
			  if(curBTime <= prevTime) 
				{
				  curBTime = prevTime+1;
				}
			  prevTime = curBTime;
			  prevBTime = curBTime;
			  prevBBut = curBut;
			}
		}
	  printf("Case #%d: %lld\n",i + 1,prevTime);
	}
}
