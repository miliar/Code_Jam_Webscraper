#include <iostream>
#include <string>

using namespace std;

int main() {
	int cases,n;
	cin >> cases;
	string line;
	string x[100];
	double p[100];
	double w[100];
	double wp[100];
	double owp[100];
	double oowp[100];
	double ans[100];
	for (int caseno = 1; caseno <= cases; caseno++) {
		cout << "Case #" << caseno << ":" << endl;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> line;
			x[i] = line;
			p[i] = 0;
			w[i] = 0;
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
			ans[i] = 0;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j<n; j++) {
				if (x[i][j] == '1') {
					p[i] += 1;
					w[i] += 1;
				} else if (x[i][j] == '0') {
					p[i] += 1;
				}
			}
		}
		for (int i = 0; i < n; i++) {
			wp[i] = w[i]/p[i];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (x[i][j] == '1') {
					owp[i] += w[j]/(p[j]-1.0);
				} else if (x[i][j] == '0') {
					owp[i] += (w[j]-1.0)/(p[j]-1.0);
				}
			}
			owp[i]/=p[i];
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (x[i][j] != '.') {
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= p[i];
		}
		for (int i = 0; i < n; i++) {
// 			cout << w[i] << ' ' << p[i] << ' ' << wp[i] << ' ' << owp[i] << ' ' << oowp[i] << ' ';
			cout << 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i] << endl;
		}
			
	}
}