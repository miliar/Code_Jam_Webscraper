// vector.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>


int _tmain(int argc, _TCHAR* argv[])
{
	int MaxLettersInAButton,MaxKeys,NoOflettersInSentence,arr[10000],temp,sum;
	int N,i,j ;
	scanf("%d",&N);
	for(int k=1;k<=N;k++)
	{
		sum=0;
		scanf("%d %d %d",&MaxLettersInAButton,&MaxKeys,&NoOflettersInSentence);

		for(j=0;j<NoOflettersInSentence;j++)
			scanf("%d",&arr[j]);

		/*sort the array */

		for(i=0;i<NoOflettersInSentence-1;i++)
		{
			for(j=0;j<NoOflettersInSentence-1-i;j++)
			{
				if(arr[j+1] > arr[j] )
				{
					temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
				}
			}
		}

		int counter = 1;
		for(i=0;i<NoOflettersInSentence;i++)
		{
			sum=sum+counter*arr[i];
			if((i+1) % MaxKeys == 0)
				counter++;
		}	
		printf("Case #%d: %d\n",k,sum);

	}		
}

