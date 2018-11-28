#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int N, C;
	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> N;

		int sum = 0, mask = 0, small = 1000001;
		for (int i=0; i<N; ++i)
		{
			fin >> C;
			sum += C;
			mask ^= C;
			small = min(small, C);
		}

		if (mask != 0)
		{
			fout << "Case #" << zz << ": NO" << endl;
		}
		else
		{
			fout << "Case #" << zz << ": " << (sum - small) << endl;
		}
	}

	return 0;
}