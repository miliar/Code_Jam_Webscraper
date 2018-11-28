#include <stdio.h>
#include <stdlib.h>
#include <fstream>

using namespace std;

int n;
int x[1001];


int solve()
{
	int maxSum = 0;
	int minElm = x[0];

	for (int i = 0; i < n; i++)
	{
		maxSum += x[i];

		if (minElm > x[i])
		{
			minElm = x[i];
		}
	}

	/*
	int maxSum = -1;
	int sum;
	int nStates = 1 << n;

	for (int state = 0; state < nStates; state++)
	{
		sum = 0;
		for (int i = 0; i < n; i++)
		{
			if ( (state & (1 << i)) != 0)
			{
				sum ^= x[i];
			}
		}

		if (sum > maxSum)
		{
			maxSum = sum;
		}
	}
	*/

	return maxSum - minElm;
}


int main()
{
	fstream			f, g;
	int			    tests;

	f.open("in.txt", ios :: in);
	g.open("out.txt", ios :: out);

	f >> tests;

	for (int k = 1; k <= tests; k++)
	{
		f >> n;
		int sum = 0;

		for (int i = 0; i < n; i++)
		{
			f >> x[i];
			sum ^= x[i];
		}

		if (sum != 0)
		{
			g << "Case #" << k << ": NO";
		}
		else
		{
			g << "Case #" << k << ": " << solve();
		}

		if (k < tests)
		{
			g << "\n";
		}
	}

	f.close();
	g.close();
	
}