#include <math.h>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>

void main()
{
	freopen("C:\\Users\\GAURAV\\Documents\\Code Jam\\Files\\A-large.in", "r", stdin);
	freopen("C:\\Users\\GAURAV\\Documents\\Code Jam\\Files\\A-large.out", "w", stdout);

	int T; // number of Test Cases
	scanf("%d", &T);

	int A[1000], B[1000];

	for (int Case = 1; Case <= T; Case++)
	{
		int N;
		int intersects = 0;

		scanf ("%d", &N);

		for (int i = 0 ; i <N; i++)
		{
			scanf("%d %d", A +i, B+i);
			
			for (int j = 0; j <i; j++)
			{
				if ( (A[j] > A[i] && B[j] < B[i]) || (A[j] < A[i] && B[j] > B[i]) )
					intersects++;
			}
		}



		printf ("Case #%d: %d\n", Case, intersects);


	}
}
