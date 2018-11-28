#include "stdafx.h"

#include <stdio.h>
#include <stdlib.h>

char buf[1024];

int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		int  N, K;
		scanf("%d", &N);
		scanf("%d", &K);

		//printf("N=%d, K=%d\n", N, K);

		int ans;
		
		if ( N >= 31 )
			ans = 0;
		else 
		{
			int  Chk = K;
			int  sum = 0;
			for (int i=0; i<N; i++)
			{
				sum += Chk & 0x1;
				Chk = Chk >> 1;
			}
			if  ( sum == N )
				ans = 1;
			else
				ans = 0;
		}

		printf("Case #%d:", i);
		
		if ( ans == 1 )
    		printf(" ON");
		else
			printf(" OFF");
    	printf("\n");
	}
  
	return  0;  
}

