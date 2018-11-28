#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

char score[100][100];

int num_win[100];
int num_match[100];

double wp[100];
double owp[100];
double oowp[100];

int main()
{	
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin >> N;
		for (int n = 0; n < N; ++n)
		{
			string buffer;
			cin >> buffer;
			for (int i = 0; i < N; ++i)
				score[n][i] = buffer[i];
		}

		// wp
		for (int n = 0; n < N; ++n)
		{
			num_win[n] = 0;
			num_match[n] = 0;
			for (int i = 0; i < N; ++i)
			{
				switch (score[n][i])
				{
				case '.':
					break;
				case '1':
					++num_win[n];
				case '0':
					++num_match[n];
					break;
				}
			}
			wp[n] = double(num_win[n]) / num_match[n];
		}

		// owp
		for (int n = 0; n < N; ++n)
		{
			owp[n] = 0;
			// for each opp
			for (int i = 0; i < N; ++i)
			{
				switch (score[n][i])
				{
				case '.':
					break;
				case '0':
					owp[n] += double(num_win[i] - 1) / (num_match[i] - 1);
					break;
				case '1':
					owp[n] += double(num_win[i]) / (num_match[i] - 1);
					break;
				}
			}

			owp[n] /= num_match[n];
		}

		// oowp
		for (int n = 0; n < N; ++n)
		{
			oowp[n] = 0;

			for (int i = 0; i < N; ++i)
				if (n != i && score[n][i] != '.')
					oowp[n] += owp[i];

			oowp[n] /= num_match[n];
		}

		cout << "Case #" << t << ":" << endl;
		for (int n = 0; n < N; ++n)
			cout << wp[n]/4 + owp[n]/2 + oowp[n]/4 << endl;
	}

	return 0;
}