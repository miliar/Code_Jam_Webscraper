#include <fstream>
using namespace std;

int main()
{
	bool on;
	int nCases, n, k, index;

	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	fin >> nCases;

	for (int currentCase = 1; currentCase <= nCases; currentCase++)
	{
		fin >> n >> k;

		on = true;

		for (index = 0; index < n; index++)
		{
			if ((k & 1) == false)
			{
				on = false;
				break;
			}

			k >>= 1;
		}

		if (on)
			fout << "Case #" << currentCase << ": ON" << endl;
		else
			fout << "Case #" << currentCase << ": OFF" << endl;
	}

	return 0;
}