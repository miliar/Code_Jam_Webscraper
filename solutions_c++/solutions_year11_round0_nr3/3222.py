#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>

using namespace std;

static const int NMax = 15;

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	int T;
	fin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N;
		fin >> N;

		vector<int> candies(N);
		for (int i = 0; i < N; i++)
			fin >> candies[i];

		int best = -1;
		for (int selGen = 1; selGen < (1 << N) - 1; selGen++)
		{
			bitset<NMax> sel(selGen);

			int sCount1, sCount2, pCount1, pCount2;
			sCount1 = sCount2 = pCount1 = pCount2 = 0;

			for (int nCandy = 0; nCandy < N; nCandy++)
				if (sel[nCandy])
				{
					sCount1 += candies[nCandy];
					pCount1 ^= candies[nCandy];
				}
				else
				{
					sCount2 += candies[nCandy];
					pCount2 ^= candies[nCandy];
				}

			if (pCount1 != pCount2)
				continue;

			best = max(best, sCount1);
			best = max(best, sCount2);
		}

		fout << "Case #" << nTestCase << ": ";
		if (best > 0)
			fout << best;
		else
			fout << "NO";
		fout << endl;
	}

	return 0;
}
