#include <iostream>
#include <cstdio>


using namespace std;

char tab[100][100];
double tab_wp[100];
double tab_owp[100];
double tab_oowp[100];
int t, n;

double wp(int ktory, int bez = -1) {

	int sum = 0;
	int all = 0;

	for (int i=0; i<n; ++i) {

		if (i == bez) continue;
		if (tab[ktory][i] != '.') ++all;
		if (tab[ktory][i] == '1') ++sum;
	}


	return (double)sum / all;
}

int main(int argc, char ** argv) {

	cin >> t;

	for (int i=0; i<t; ++i) {

		cin >> n;

		for (int j=0; j<n; ++j) {

			for (int k=0; k<n; ++k) {

				cin >> tab[j][k];
			}
		}

		for (int j=0; j<n; ++j) {

			tab_wp[j] = wp(j);
		}

		double owp;
		int all;
		for (int j=0; j<n; ++j) {

			owp = 0.0;
			all = 0;
			for (int k=0; k<n; ++k) {

				if (tab[k][j] == '.') continue;
				owp += wp(k,j);
				++all;
			}

			tab_owp[j] = (double)owp / all;
		}

		double oowp;
		for (int j=0; j<n; ++j) {

			oowp = 0.0;
			all = 0;
			for (int k=0; k<n; ++k) {

				if (tab[k][j] == '.') continue;
				oowp += tab_owp[k];
				++all;
			}

			tab_oowp[j] = (double)oowp / all;
		}

		cout << "Case #" << i+1 << ":" << endl;

		double wyn;

		for (int j=0; j<n; ++j) {

			wyn = 0.25 * tab_wp[j] + 0.5 * tab_owp[j] + 0.25 * tab_oowp[j];

			printf("%.12lf\n", wyn);
		}
	}

	return 0;
}
