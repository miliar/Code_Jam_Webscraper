

#include <iostream>

using namespace std;

double WP  [200];
double OWP [200];
double OOWP[200];
int    Match[200][200];
int    Num [200];


int main () {
	int cases;
	cin >> cases;

	int n = 0;
	while (++n <= cases) {
		int teams;
		cin >> teams;

		for (int i = 0; i < teams; ++i) {
			Num[i] = 0;
			WP[i] = 0;
			for (int j = 0; j < teams; ++j) {
				char c;
				cin >> c;
				if (c == '.')		{Match[i][j] = -1;}
				else if (c == '1')	{Match[i][j] = 1; ++Num[i]; WP[i] += 1;}
				else if (c == '0')	{Match[i][j] = 0; ++Num[i];}
			}
		}

		for (int i = 0; i < teams; ++i) {
			OWP[i] = 0;
			for (int j = 0; j < teams; ++j) {
				if (Match[i][j] == -1) continue;
				OWP[i] += (WP[j] - Match[j][i]) / (Num[j] - 1);
			}
			OWP[i] /= Num[i];
		}

		for (int i = 0; i < teams; ++i) {
			OOWP[i] = 0;
			for (int j = 0; j < teams; ++j) {
				if (Match[i][j] == -1) continue;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= Num[i];
		}

		cout << "Case #" << n << ":" << endl;
		for (int i = 0; i < teams; ++i) {
			double RPI = 0.25 * (WP[i]/Num[i]) + 0.50 * OWP[i] + 0.25 * OOWP[i];
			cout.precision(10);
			cout << RPI << endl;
		}
	}

	return 0;
}