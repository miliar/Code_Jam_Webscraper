#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
using namespace std;

ifstream lettura ("input.txt");
ofstream scrittura ("output.txt");

int main ()
{
	int t;

	lettura >> t;

	for (int i = 1; i <= t; i += 1)
	{
		int n;

		int seq[15];

		lettura >> n;

		for (int j = 0; j < n; j += 1)
		{
			lettura >> seq[j];
		}

		int result = -1;

		for (int j = 1; j < ((1 << n) - 1); j += 1)
		{
			int xor_a = 0;
			int sum_a = 0;
			int xor_b = 0;
			int sum_b = 0;

			for (int k = 0; k < n; k += 1)
			{
				if (((1 << k) & j) != 0)
				{
					xor_a ^= seq[k];
					sum_a += seq[k];
				}
				else
				{
					xor_b ^= seq[k];
					sum_b += seq[k];
				}
			}

			if (xor_a == xor_b)
			{
				result = max (result, max (sum_a, sum_b));
			}
		}

		scrittura << "Case #" << i << ": ";
		if (result == -1)
		{
			scrittura << "NO";
		}
		else
		{
			scrittura << result;
		}
		scrittura << endl;
	}
}
