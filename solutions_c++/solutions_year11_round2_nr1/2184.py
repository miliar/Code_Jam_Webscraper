#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iomanip>
#include <bitset>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	int T;
	fin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		static const int NMax = 100;

		static double WP[NMax];
		static double OWP[NMax];
		static double OOWP[NMax];
		static bitset<NMax> Opponents[NMax];

		memset(WP, 0, sizeof(WP));
		memset(OWP, 0, sizeof(OWP));
		memset(OOWP, 0, sizeof(OOWP));
		memset(Opponents, 0, sizeof(Opponents));

		int N;
		fin >> N;

		for (int nLine = 0; nLine < N; nLine++)
		{
			string mask;
			fin >> mask;

			int tot = 0, win = 0;
			for (int i = 0; i < N; i++)
			{
				if (mask[i] != '.')
				{
					tot++;
					Opponents[nLine][i] = true;
					if (mask[i] == '1')
						win++;
				}
			}
			WP[nLine] = double(win) / tot;

			for (int i = 0; i < N; i++)
			{
				if (i == nLine)
					continue;

				switch (mask[i])
				{
				case '1':
					OWP[i] += double(win - 1) / (tot - 1);
					break;
				case '0':
					OWP[i] += win / double(tot - 1);
					break;
				default:
					break;
				}
			}
		}

		for (int i = 0; i < N; i++)			
			OWP[i] /= Opponents[i].count();
		
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
				if (Opponents[i][j])
					OOWP[i] += OWP[j];
			OOWP[i] /= Opponents[i].count();
		}

		fout << "Case #" << nTestCase << ':' << endl;
		for (int i = 0; i < N; i++)
			fout << fixed << setprecision(6) << ( 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i] ) << endl;
	}

	return 0;
}
