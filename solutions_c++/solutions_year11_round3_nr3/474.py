// Harmony.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

const int MaxN = 10000;

int notes[MaxN];

int _tmain(int argc, _TCHAR* argv[])
{

	int T;

	scanf("%d", &T);

	for (int t = 1; t <= T; t++)
	{
		int N, L, H;
		bool foundMatch = false;

		scanf("%d %d %d", &N, &L, &H);

		for (int n = 0; n < N; n++)
		{
			scanf("%d", &notes[n]);
		}

		int f;
		for (f = L; f <= H; f++)
		{
			foundMatch = false;
			int n;
			for (n = 0; n < N; n++)
			{
			  int f1 = notes[n];

			  if (f1 > f)
			  {
				  if ((f1 % f) != 0)
				  {
					  break;
				  }
			  }
			  else
			  {
				  if ((f % f1) != 0)
				  {
					  break;
				  }
			  }
			}

			if (n == N)
			{
				break;
			}
		}

		if (f <= H)
		{
			printf ("Case #%d: %d\n", t, f);
		}
		else
		{
			printf("Case #%d: NO\n", t);
		}
	}

	return 0;
}

