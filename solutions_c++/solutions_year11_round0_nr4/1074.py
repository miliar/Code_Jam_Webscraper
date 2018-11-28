#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("D-large.in");
	ofstream fout("D-large.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int N, x;

	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> N;

		int res = 0;
		for (int i=1; i<=N; ++i)
		{
			fin >> x;
			if (x != i)
				++res;
		}

		fout << "Case #" << zz << ": " << double(res) << endl;
	}

	return 0;
}