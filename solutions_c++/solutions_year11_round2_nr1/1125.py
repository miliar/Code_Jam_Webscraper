#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int t;
	cin >> t;

	char tbl[128][128];
	double wp[128],owp[128],oowp[128];
	for (int i=0;i<t;i++) {
		int n;
		cin >> n;

		for (int j=0;j<n;j++) {
			for (int k=0;k<n;k++) {
				cin >> tbl[j][k];
			}
		}

		// wp
		for (int j=0;j<n;j++) {
			int total = 0, win = 0;
			for (int k=0;k<n;k++) {
				if (tbl[j][k] == '.') continue;
				if (tbl[j][k] == '1') win++;
				total++;
			}
			wp[j] = (double)win/total;
		}

		// owp
		for (int j=0;j<n;j++) {
			owp[j] = 0;
			int nn = 0;
			for (int k=0;k<n;k++) {
				if (tbl[j][k] == '.') continue;
				nn++;
				int total = 0, win = 0;
				for (int l=0;l<n;l++) {
					if (l == j) continue;
					if (tbl[k][l] == '.') continue;
					if (tbl[k][l] == '1') win++;
					total++;
				}
				owp[j] += (double)win/total;
			}
			owp[j] /= nn;
		}
		
		// oowp
		for (int j=0;j<n;j++) {
			oowp[j] = 0;
			int nn = 0;
			for (int k=0;k<n;k++) {
				if (tbl[j][k] == '.') continue;
				nn++;
				oowp[j] += owp[k];
			}
			oowp[j] /= nn;
		}


		cout.precision(10);
		cout << "Case #" << (i+1) << ": " << endl;
		
		for (int j=0;j<n;j++) {
			cout << wp[j]*0.25 + owp[j]*0.5 + oowp[j]*0.25 << endl;
		}

	}

	return 0;
}
