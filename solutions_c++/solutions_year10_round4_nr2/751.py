#include <fstream>
#include <string>
using namespace std;

int M[1024];
int C[10][1024];
unsigned int T, P;

bool check(int loc, int n)
{
	bool ok = true;
	for (int i=loc; i<loc+n; ++i)
		ok &= (M[i] > 0);

	if (!ok) return false;
	for (int i=loc; i<loc+n; ++i)
		--M[i];

	return true;
}

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");


	fin >> T;
	for (unsigned int z=1; z<=T; ++z)
	{
		fin >> P;
		int totalTeams = 1<<P;
		for (int i=0; i < totalTeams; ++i)
			fin >> M[i];
		for (int i=1; i<=P; ++i)
		{
			int nMatches = totalTeams / (1<<i);
			for (int j=0; j<nMatches; ++j)
				fin >> C[i-1][j];
		}


		int cost = 0;
		for (int i=1; i<=P; ++i)
		{
			int nTeams = 1 << i;
			for (int j=0; j<totalTeams; j+=nTeams)
			if (!check(j, nTeams))
				++cost;
		}

		fout << "Case #" << z << ": " << cost << endl;
	}

	return 0;
}