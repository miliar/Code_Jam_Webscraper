#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream infile ("d:\\temp\\A-large.in");
	//ofstream outfile(argv[2]);

	int T = 0;

	int n = 0;
	int s[200];
	double d[200];

	if (infile.is_open())
	{
		infile >> T;

		for (int t = 1; t < T + 1; t++)
		{
			infile >> n;
			int sum = 0;
			for (int comp = 0; comp < n; comp++)
			{
				int tmp = 0;
				infile >> tmp;
				sum += tmp;
				s[comp] = tmp;
				d[comp] = -1;
			}

			double mean = (double) sum / n;

			int cntNeg = 0;

			int sum1 = 0;
			for (int comp = 0; comp < n; comp++)
			{
				if (2 * mean - s[comp] < 0)
				{
					d[comp] = 0;
					cntNeg++;
					sum1 += s[comp];
				}
			}

			if (cntNeg == 0)
			{
				for (int comp = 0; comp < n; comp++)
				{
					d[comp] = (2 * mean - s[comp]) / sum * 100;
				}
			}
			else
			{
				double mean1 = ((double) (2 * sum - sum1)) / (n - cntNeg);
				for (int comp = 0; comp < n; comp++)
				{
					if (d[comp] != 0)
					{
						d[comp] = (mean1 - s[comp]) / sum * 100;
					}
				}
			}

			printf("Case #%d:", t);

			for (int comp = 0; comp < n; comp++)
			{
				printf(" %.6f", d[comp]);
			}

			printf("\n");
		}
		infile.close();
//		outfile.close();
	}

	return 0;
}