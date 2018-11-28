#include <iostream>

using namespace std;

int main() {
	int N;

	cin >> N;

	for (int cs = 1; cs <= N; cs++) {
		int t;

		cin >> t;
		
		int r[200][200], tot[200], win[200];
		double wp[200], owp[200], oowp[200];

		for (int i = 0; i < t; i++) {
			win[i] = tot[i] = 0;
			for (int j = 0; j < t; j++) {
				char c;

				cin >> c;
				
				// r[i][j] = (c=='.')?-1:((c=='0')?:0:1);				

				switch (c) {
					case '.':
						r[i][j] = -1;
						break;
					case '1':
						r[i][j] = 1;
						win[i]++;
						tot[i]++;
						break;
					case '0':
						r[i][j] = 0;
						tot[i]++;
						break;
				}
			}
			wp[i] = (double)win[i]/tot[i];
		}
		
		// wp
		
		for (int i = 0; i < t; i++) {
			owp[i] = 0;
			for (int j = 0; j < t; j++) {
				//cout << "" << r[i][j] << endl;
				if (r[i][j] != -1) {
					if (r[i][j] == 1)
						owp[i] += double(win[j])/(tot[j] - 1);
					else
						owp[i] += double(win[j] - 1)/(tot[j] - 1);
					//cout << "\t" << owp[i] << endl;
				}
			}
			owp[i] /= tot[i];
		}

		for (int i = 0; i < t; i++) {
			oowp[i] = 0;
			for (int j = 0; j < t; j++) {
				if (r[i][j] != -1)
					oowp[i] += owp[j];
			}
			oowp[i] /= tot[i];
		}

		cout << "Case #" << cs << ": " << endl;

		for (int i = 0; i < t; i++) {
			cout << .25 * wp[i] + .5 * owp[i] + .25 * oowp[i] << endl;
			//cout << "wp " << wp[i] << " owp " << owp[i] << " oowp " << oowp[i] << endl;

		}

	}


	return 0;
}