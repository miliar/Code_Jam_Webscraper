#include <stdio.h>
#include <vector>

#define DEBUG 0

using namespace std;

long main()
{
	vector<long> group(1100);

	long T; // test cases
	scanf("%d\n", &T);

	for (int t = 0; t < T; t++) // for each test case
	{

		long R; // rides per day
		long K; // max # of riders
		long N; // group count

		// get info
		scanf("%d %d %d\n", &R, &K, &N);

		// get groups
		for (int n = 0; n < N; n++)
		{
			long number;
			scanf("%d", &number);
			group[n] = number;
		}

		long profit = 0;
		long mark = 0;

		// sim rollercoaster
		for (long r = 0; r < R; r++) // for each ride per day
		{
			long start = mark;
			long k = 0;

			while (k < K) // pick groups for the ride
			{
				if (k + group[mark] > K) break;
				else k += group[mark];
				if (DEBUG) printf("boarding group[%d] of size %d\n", mark, group[mark]);

				profit += group[mark];

				mark++;
				if (mark >= N) mark = 0;
				if (mark == start) break; // everyone is on board!!!!
			}
			if (DEBUG) printf("DEPARTING RIDE # %d with %d riders\n", r + 1, k);
		}

		printf("Case #%d: %d\n", t + 1, profit);
	}


	if (DEBUG)
	{
		printf("--DONE--");
		char str[100];
		scanf("%s", str);
	}

	return 0;
}