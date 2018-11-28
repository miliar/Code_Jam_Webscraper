#include<stdio.h>
#define MAX_N 1005

int n, k, r, g [MAX_N], t, jump [MAX_N], score [MAX_N];
long long sol;
bool mark [MAX_N];

	void solve()
	{
		for (int i = 0; i < n; i++)
		{
			mark [i] = false;
			jump [i] = -1;
			score [i] = 0;
		}


		int index = 0;
		while (! mark [index])
		{
			mark [index] = true;
			int tmpSum = 0, startIndex = index;
			while ((tmpSum + g [index] <= k) && ((tmpSum == 0) || (index != startIndex)))
			{
				tmpSum += g [index];
				index = (index + 1) % n;
			}
			jump [startIndex] = index;
			score [startIndex] = tmpSum;
		}

		sol = 0;
		index = 0;
		for (int i = 0; i < r; i++)
		{
			sol += score [index];
			index = jump [index];
		}
	}

	int main()
	{
		FILE *in = fopen("input.in", "r");
		fscanf(in, "%d", &t);
		for (int numTest = 1; numTest <= t; numTest++)
		{
			fscanf(in, "%d %d %d", &r, &k, &n);
			for (int i = 0; i < n; i++)
				fscanf (in, "%d", &g [i]);
			solve();
			printf ("Case #%d: %lld\n", numTest, sol);			
		}

		fclose(in);

		return 0;
	}