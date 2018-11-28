#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

string tab[100];
int won[100], played[100];
int wonag[100][100], playedag[100][100];
double wp[100], owp[100];

int main() {
	
	int cases;
	cin >> cases;
	
	for (int c = 1; c <= cases; c++) {
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> tab[i];
			won[i] = played[i] = 0;
			for (int k = 0; k < n; k++)
				wonag[i][k] = playedag[i][k] = 0;
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (tab[i][j] == '.')
					continue;
				if (tab[i][j] == '1') {
					won[i]++;
					wonag[i][j]++;
				}
				played[i]++;
				playedag[i][j]++;
			}
		}
		
		cout << "Case #" << c << ":" << endl;
		
		for (int i = 0; i < n; i++) {
			wp[i] = won[i] / (double) played[i];
			//cout << "wp " << (i+1) << " = " << wp[i] << " " << won[i] << " " << played[i] << endl;
		}
		
		for (int i = 0; i < n; i++) {
			owp[i] = 0;
			int cont = 0;
			for (int k = 0; k < n; k++) {
				if (playedag[k][i]) {
					owp[i] += (won[k] - wonag[k][i]) / ((double) played[k] - playedag[k][i]);
					cont++;
				}
			}
			owp[i] /= cont;
			//cout << "owp " << (i+1) << " = " << owp[i] << " " << cont << endl;
		}
		
		for (int i = 0; i < n; i++) {
			double oowp = 0;
			int cont = 0;
			for (int k = 0; k < n; k++) {
				if (playedag[i][k]) {
					oowp += owp[k];
					cont++;
				}
			}
			oowp /= cont;
			cout << setprecision(12) << 0.25 * (wp[i] + 2 * owp[i] + oowp) << endl;
		}
	}
	
	return 0;
}
