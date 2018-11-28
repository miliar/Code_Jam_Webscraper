#include <iostream>
#include <fstream>
#include <stddef.h>

unsigned int pow10 [] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000 };
unsigned int fac [] = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 };

unsigned int countdigits (unsigned int n)
{
	unsigned int digitcount = 0;
	if (n == 0) { return 1; }
	while (n)
	{
		n /= 10;
		digitcount++;
	}
	return digitcount;
}

unsigned int ror (unsigned int digitcount, unsigned int n)
{
	unsigned int lastdigit = n % 10;
	n /= 10;
	return n + lastdigit * pow10 [digitcount - 1 ];
}

unsigned int choose (unsigned int n, unsigned int r)
{
	if (r > n) { return 0; }
	return fac [n] / fac [r] / fac [n - r];
}

unsigned int *next;

int main ()
{
	std::ifstream in ("c.in");
	std::ofstream out ("c.out");

	unsigned int testcount;
	in >> testcount;

	next = new unsigned int [10000001];

	for (unsigned int i = 0; i < testcount; i++)
	{
		unsigned int a;
		unsigned int b;
		in >> a;
		in >> b;

		for (unsigned int j = 0; j < 10000001; j++) { next [j] = 0; }

		unsigned int digitcount = countdigits (a);
		unsigned int paircount = 0;
		for (unsigned int j = a; j <= b; j++)
		{
			unsigned int num = j;
			if (!next [num])
			{
				unsigned int blobcount = 0;
				unsigned int nextnum;
				while (!next [num])
				{
					nextnum = ror (digitcount, num);
					next [num] = nextnum;
					if (nextnum == num) { break; }
					if (a <= nextnum && nextnum <= b)
					{
						blobcount++;
					}
					// out << num << "->" << nextnum << std::endl;
					num = nextnum;
				}
				paircount += choose (blobcount, 2);
				// out << "blobcount = " << blobcount << std::endl;
				// out << "paircount += " << choose (blobcount, 2) << std::endl;
			}
		}

		out << "Case #" << (i + 1) << ": " << paircount << std::endl;
	}

	delete [] next;
	next = NULL;
	return 0;
}

