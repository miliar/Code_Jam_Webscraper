// Candy.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>



int _tmain(int argc, _TCHAR* argv[])
{

	int T, N;
	int C[1000];

	scanf("%d", &T);



	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);

		scanf("%d", &N);

		for (int n = 0; n < N; n++)
		{
			scanf("%d", &C[n]);
		}

		unsigned int mask = (1 << N);
		
		int x = 1;
		int biggest = -1;

		while (((x+1) & mask) == 0)
		{
		  unsigned int m2 = 1;
		  int falseVal1 = 0, falseVal2 = 0;
		  int trueVal1 = 0, trueVal2 = 0;

		  for (int n = 0; n < N; n++)
		  {
			  if (x & m2)
			  {
				  falseVal1 ^= C[n];
				  trueVal1 += C[n];
			  }
			  else
			  {
				  falseVal2 ^= C[n];
				  trueVal2 += C[n];
			  }

			  m2 <<= 1;
		  }

		  if (falseVal1 == falseVal2)
		  {
			  if (trueVal1 > biggest)
				  biggest = trueVal1;
			  if (trueVal2 > biggest)
				  biggest = trueVal2;
		  }

//		  printf("%4x %d %d %d %d %d\n", x, falseVal1, falseVal2, trueVal1, trueVal2, biggest);

		  x++;
		}

		if (biggest == -1)
			printf ("NO\n");
		else
			printf ("%d\n", biggest);
	}

	return 0;
}

