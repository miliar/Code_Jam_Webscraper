#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");

	unsigned int numberOfCases;
	fin >> numberOfCases;

	int C, D, N;
	string s;

	bool opp[256][256];
	char com[256][256];

	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		string res;
		memset(opp, 0, sizeof(opp));
		memset(com, 0, sizeof(com));

		fin >> C;
		for (int i=0; i<C; ++i)
		{
			fin >> s;
			com[s[0]][s[1]] = com[s[1]][s[0]] = s[2];
		}

		fin >> D;
		for (int i=0; i<D; ++i)
		{
			fin >> s;
			opp[s[0]][s[1]] = opp[s[1]][s[0]] = true;
		}

		fin >> N;
		fin >> s;
		for (int i=0; i<N; ++i)
		{
			res += s[i];
			int a = res.size();
			if (a > 1)
			{
				char alt = com[res[a-1]][res[a-2]];
				if (alt != 0)
				{
					res.pop_back(); res.pop_back();
					res += alt;
				}
			}

			for (int j=0; j+1 < res.size(); ++j)
				if (opp[res[j]][res.back()])
					res.clear();
		}

		string res2 = "[";
		for (int i=0; i<res.size(); ++i)
		{
			if (i>0) res2 += ", ";
			res2 += res[i];
		}
		res2 += "]";

		fout << "Case #" << zz << ": " << res2 << endl;
	}

	return 0;
}