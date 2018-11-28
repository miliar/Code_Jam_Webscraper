#include <iostream>
#include <fstream>

int main ()
{
	std::ifstream in ("b.in");
	std::ofstream out ("b.out");

	unsigned int testcount;
	in >> testcount;

	for (unsigned int i = 0; i < testcount; i++)
	{
		unsigned int n;
		int s;
		int p;
		in >> n;
		in >> s;
		in >> p;

		int goodcount = 0;
		int possiblescount = 0;
		int goodlbound = p * 3 - 2; // >= goodlbound --> goodcount++
		int pslbound = p * 3 - 4; // >= pslbound --> possiblescount++
		if (pslbound <= 0) { pslbound = 1; }

		for (unsigned int j = 0; j < n; j++)
		{
			int totscore;
			in >> totscore;
			if (totscore >= goodlbound) { goodcount++; }
			else if (totscore >= pslbound) { possiblescount++; }
		}

		if (possiblescount > s) { possiblescount = s; }

		out << "Case #" << (i + 1) << ": " << (possiblescount + goodcount) << std::endl;
	}

	return 0;
}

