// GjamCpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <conio.h>
#include <string>
#include <iostream>

int main()
{
	int i,j,k;
	//printf("Hello world!\n");

	int Number_of_TestCases=0;
	int l=1;
	scanf("%d",&Number_of_TestCases);
	int  L, t, N , C;

	int* Matrix;
	int* Distance;
	int* BoosterLocation;
	int* TimeSaved;
	int* MaxTimeSaved;

	int ttime=0;
	while(l<=Number_of_TestCases)
	{
		scanf("%d %d %d %d", &L, &t, &N, &C);

		Matrix = new int[C+1];
		Distance = new int[N + 1];
		BoosterLocation = new int[N+1];
		TimeSaved = new int[N+1];
		MaxTimeSaved = new int[L+1];

		for(int i=0;i<N;i++)
		{
			BoosterLocation[i] = 0;
			TimeSaved[i]=0;
		}

		for(int j=0;j<C;j++)
			scanf("%d", &Matrix[j]);
		int Maxtime=0;

		for(int i=0;i<N;i++)
		{
			Distance[i] = Matrix[i%C];
			Maxtime += Distance[i] * 2; 
		}

		for(int i=0;i<L;i++)
			MaxTimeSaved[i] = 0;

		int j=0;
		int time = 0;
		int gtime = 0;
		bool flag = false;
		for(int k=0;k<N;k++)
		{
			time += Distance[k] *2;
			
			/*while(j<N)
			{*/
			if(flag == false)
			{
				if(time > t) 
				{
					TimeSaved[k] = (time-t)/2;
					flag = true;

					for(int i=0;i<L;i++)
						if(MaxTimeSaved[i] < TimeSaved[k])
						{

							int least = MaxTimeSaved[j];
							int li = 0;
							for(int j=0;j<L;j++)
								if(MaxTimeSaved[j] < least)
								{li= j; least = MaxTimeSaved[j]; }
							MaxTimeSaved[li] = TimeSaved[k]; break;
						}


				}
			}
			else
			{
				TimeSaved[k] = Distance[k];

					for(int i=0;i<L;i++)
						if(MaxTimeSaved[i] < TimeSaved[k])
						{

							int least = MaxTimeSaved[j];
							int li = 0;
							for(int j=0;j<L;j++)
								if(MaxTimeSaved[j] < least)
								{li= j; least = MaxTimeSaved[j]; }
							MaxTimeSaved[li] = TimeSaved[k]; break;
						}

			}

			/*}*/
		}

		for(int i=0;i<L;i++)
			Maxtime -= MaxTimeSaved[i];

		printf("Case #%d: %d\n",l,Maxtime);
		
		delete Matrix;
		delete Distance;
		delete BoosterLocation;
		delete TimeSaved;
		delete MaxTimeSaved ;
		l++;
	}
	return 0;
}
