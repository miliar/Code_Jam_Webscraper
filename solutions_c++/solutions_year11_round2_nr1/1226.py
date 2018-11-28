// ---------------------------------------------------------------------------

#pragma hdrstop

#include <tchar.h>
// ---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
#include <stdlib>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
	int t;
	ifstream fin("A1.in");
	ofstream fout("A.out");
	fin >> t;

	// p = p;

	for (int l = 0; l < t; l++) {

		int n;
		fin >> n;
		int a[100][100];
		char c;
		double wp[100], k[100], owp[100], oowp[100];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {

				fin >> c;
				if (c == '1')
					a[i][j] = 1;
				else if (c == '0')
					a[i][j] = 0;
				else if (c == '.')
					a[i][j] = -1;
			}
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
			k[i] = 0;
		}

		//vector<double>wp(100, 0);

		for (int i = 0; i < n; i++) {

			for (int j = 0; j < n; j++) {
				if (a[i][j] == 1) {
					wp[i] += a[i][j];
					k[i]++;
				}
				else if (a[i][j] == 0) {
					k[i]++;
				}

			}

		

		}
        wp[0] = wp[0];
		//vector<double>owp(100, 0);
		for (int i = 0; i < n; i++) {

			for (int j = 0; j < n; j++) {
				double temp;
				if (a[i][j] == 1 || a[i][j] == 0) {
					temp = (wp[j] - (1 - a[i][j])) / (double)(k[j] - 1);

					owp[i] += temp;
				}

			}

			if (k[i] != 0)
				owp[i] /= (double)k[i];

		}

		//vector<double>oowp(100, 0);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (a[i][j] == 1 || a[i][j] == 0) {
					oowp[i] += owp[j];
				}

			}

			if (k[i] != 0)
				oowp[i] /= (double)k[i];

		}

		fout << "Case #" << (l + 1) << ":" << endl;
		for (int i = 0; i < n; i++) {
			double temp = 0.25 * (wp[i] / (double) k[i]) + 0.5 * owp[i] + 0.25 * oowp[i];
			fout << fixed << setprecision(8)  << temp << endl;
		}

	}

	fin.close();

	return 0;
}
// ---------------------------------------------------------------------------
