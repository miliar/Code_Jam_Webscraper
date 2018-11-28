#include <algorithm>
#include <iostream>
#include <fstream>
#include <stddef.h>
#include <stdlib.h>
#include <string>

int vinecount;
int vinelengths [10000];
int vinepos [10000];
int minreqlength [10000];
int destpos;

int main ()
{
	std::ifstream in ("a.in");
	std::ofstream out ("a.out");

	unsigned int tests;
	in >> tests;

	for (unsigned int i = 0; i < tests; i++)
	{
		in >> vinecount;
		for (int j = 0; j < vinecount; j++)
		{
			in >> vinepos [j];
			in >> vinelengths [j];
			minreqlength [j] = 0;
		}
		in >> destpos;

		for (int j = vinecount - 1; j >= 0; j--)
		{
			minreqlength [j] = destpos - vinepos [j];
			for (int k = j + 1; k < vinecount; k++)
			{
				int swinglengthreq = vinepos [k] - vinepos [j];
				int nextlengthreq = minreqlength [k];

				// if unreachable, break
				if (swinglengthreq > vinelengths [j]) { break; }
				// current vine cannot produce enough swing length for next vine
				if (swinglengthreq < minreqlength [k]) { continue; }
				// next vine being considered is useless
				if (minreqlength [k] == -1) { continue; }

				if (swinglengthreq > nextlengthreq) { nextlengthreq = swinglengthreq; }
				if (nextlengthreq < minreqlength [j]) { minreqlength [j] = nextlengthreq; }
			}
			if (minreqlength [j] > vinelengths [j]) { minreqlength [j] = -1; }
			// out << minreqlength [j] << std::endl;
		}

		out << "Case #" << (i + 1) << ": ";
		if (minreqlength [0] == -1) { out << "NO"; }
		else if (minreqlength [0] > vinepos [0])
		{
			out << "NO";
		}
		else
		{
			out << "YES";
		}
		out << std::endl;
	}

	return 0;
}