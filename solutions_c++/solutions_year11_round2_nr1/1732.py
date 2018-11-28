#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
#define DEBUG 0

double RPI (double per, double perOpp, double perOppOpp) {
	return (per * 0.25 + perOpp * 0.5 + perOppOpp * 0.25);
}

int main () {
	int nCases, iCase = 0;

	cin >> nCases;
	while (iCase < nCases) {
		int nT;
		cin >> nT;
		int w[nT]; // num wins
		int l[nT]; // num losses
		double per[nT];
		double perOpp[nT];
		double perOppOpp[nT];

		int opp[nT][nT];
		int oppW[nT][nT];
		int nOpp[nT];
		for (int i = 0; i < nT; i++) {
			w[i] = 0;
			l[i] = 0;
			nOpp[i] = 0;
		}

		char c;
		for (int i = 0; i < nT; i++) {
			for (int j = 0; j <= i; j++) {
				cin >> c;
			}
			for (int j = i+1; j < nT; j++) {
				cin >> c;
				switch (c) {
				case '.':
					break;
				case '1':
					w[i]++;
					l[j]++; 

					opp[i][nOpp[i]] = j;
					oppW[i][nOpp[i]] = 1;
					(nOpp[i])++;

					opp[j][nOpp[j]] = i;
					oppW[j][nOpp[j]] = 0;
					(nOpp[j])++;
					break;
				case '0':
					w[j]++;
					l[i]++;

					opp[i][nOpp[i]] = j;
					oppW[i][nOpp[i]] = 0;
					(nOpp[i])++;

					opp[j][nOpp[j]] = i;
					oppW[j][nOpp[j]] = 1;
					(nOpp[j])++;
					break;
				default:
					printf ("should not get here...!\n");
					return -1;
				}
			}
		}
		
		for (int i = 0; i < nT; i++) {
			per[i] = double (w[i]) / (w[i] + l[i]);
			if (DEBUG) printf ("W %d L %d Per %f\n", w[i], l[i], per[i]);
		}
		for (int i = 0; i < nT; i++) {
			double perSum = 0.0;
			for (int j = 0; j < nOpp[i]; j++) {
				int x = opp[i][j];
				int y = oppW[i][j];
				double perTemp = double (w[x] - !y) / (w[x] + l[x] - 1);
				perSum += perTemp;
			}
			perOpp[i] = perSum / nOpp[i];
			if (DEBUG) printf ("PerOpp %f\n", perOpp[i]);
		}
		for (int i = 0; i < nT; i++) {
			double perSum = 0.0;
			for (int j = 0; j < nOpp[i]; j++) {
				int x = opp[i][j];
				perSum += perOpp[x];
			}
			perOppOpp[i] = perSum / nOpp[i];
			if (DEBUG) printf ("PerOppOpp %f\n", perOppOpp[i]);
		}

		printf ("Case #%d:\n", ++iCase);
		for (int i = 0; i < nT; i++) {
			printf ("%f\n", RPI (per[i], perOpp[i], perOppOpp[i]));
		}
	}
}
