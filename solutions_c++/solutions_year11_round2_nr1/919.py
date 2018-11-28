#include <iostream>
#include <vector>
#include <map>
#include <vector>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <set>

using namespace std;

int T, N;
string maps[128];
double wp[128], owp[128], oowp[128];

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		cin >> N;
		for (int i = 0; i < N; ++i)
			cin >> maps[i];

		cout << "Case #" << t <<":\n";

		for (int i = 0; i < N; ++i)
		{
			int win = 0, tot = 0;
			wp[i] = owp[i] = oowp[i] = 0;

			for (int j = 0; j < N; ++j)
			{
				if (maps[i][j] == '0')
					++tot;
				if (maps[i][j] == '1')
					++win, ++tot;
			}

			wp[i] = win * 1.0 / tot;
			
			int cnt = 0;
			for (int j = 0; j < N; ++j)
				if (j != i && maps[i][j] != '.')
				{
					++cnt;
					win = tot = 0;
					for (int k = 0; k < N; ++k)
						if (k != i)
							if (maps[j][k] == '1')
								++win, ++tot;
							else
								if (maps[j][k] == '0')
									++tot;
					owp[i] += win * 1.0 / tot; 
				}

				if (cnt != 0)
					owp[i] /= cnt;
				else
					owp[i] = 0;
		}

		for (int i = 0; i < N; ++i)
		{
			int cnt = 0;
			for (int j = 0; j < N; ++j)
				if (i != j && maps[i][j] != '.')
					oowp[i] += owp[j], ++cnt;

			oowp[i] /= cnt;

			double rpi = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			cout << rpi << "\n";
		}
	}

	return 0;
}