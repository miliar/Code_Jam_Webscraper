#include<vector>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	fout << std::setprecision(10);
	unsigned int numberOfCases;
	fin >> numberOfCases;

	int N;

	for (unsigned int zz=1; zz<=numberOfCases; ++zz)
	{
		fin >> N;
		vector<string> res(N);
		vector<int> games(N, 0), wins(N, 0);
		vector<double> wp(N, 0.0), owp(N, 0.0), oowp(N, 0.0), score(N, 0.0);
		for (int i=0; i<N; ++i)
		{
			fin >> res[i];
			for (int j=0; j<N; ++j)
			{
				if (res[i][j] != '.')
				{
					++games[i];
					if (res[i][j] == '1')
						++wins[i];
				}
			}
			wp[i] = double(wins[i])/games[i];
			score[i] += wp[i] * 0.25;
		}

		for (int i=0; i<N; ++i)
		{
			for (int j=0; j<N; ++j)
			{
				double thisOWP = 0.0;
				if (res[i][j] == '1')
				{
					thisOWP = double(wins[j]) / (games[j]-1);
				}
				else if (res[i][j] == '0')
				{
					thisOWP = double(wins[j]-1) / (games[j]-1);
				}
				owp[i] += thisOWP / games[i];
			}
			score[i] += owp[i] * 0.5;
		}

		fout << "Case #" << zz << ": " << endl;
		for (int i=0; i<N; ++i)
		{
			for (int j=0; j<N; ++j)
			{
				if (res[i][j] != '.')
				{
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= games[i];
			score[i] += oowp[i] * 0.25;
			fout << score[i] << endl;
		}
	}

	return 0;
}