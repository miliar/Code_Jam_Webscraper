#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

void main () {
	ifstream f ("input.txt");
	FILE * of;
	of = fopen("output.txt", "w+");
	int T = 0;
	f >> T;
	for (int tc = 0; tc < T; ++tc) {
		int N = 0;
		f >> N;

		vector<string> games (N);
		for (int i = 0; i < N; ++i) {
			f >> games[i];
		}

		vector<double> wp (N, 0);
		for (int i = 0; i < N; ++i) {
			int wins = 0, loses = 0;
			for (int j = 0; j < N; ++j) {
				if (games[i][j] == '1') wins++;
				if (games[i][j] == '0') loses++;
			}
			wp[i] = (double)wins / (double)(wins + loses);
		}

		vector<double> owp (N, 0);
		for (int k = 0; k < N; ++k) {
			vector<double> nwp (N, 0);
			for (int i = 0; i < N; ++i) {				
				int wins = 0, loses = 0;
				if (i == k) continue;
				for (int j = 0; j < N; ++j) {
					if (j == k) continue;
					if (games[i][j] == '1') wins++;
					if (games[i][j] == '0') loses++;
				}			
				nwp[i] = (double)wins / (double)(wins + loses);
			}

			double nnwp = 0;
			int cnt = 0;
			for (int i = 0; i < N; ++i)
				if (games[k][i] != '.') {
					nnwp += nwp[i];
					cnt++;
				}
			owp[k] = nnwp / (double)(cnt);
		}

		vector<double> oowp (N, 0);
		for (int i = 0; i < N; ++i) {
			double nowp = 0;
			int cnt = 0;
			for (int j = 0; j < N; ++j) {
				if (j == i || games[i][j] == '.') continue;
				nowp += owp[j];
				cnt++;
			}
			oowp[i] = nowp / (double)(cnt);
		}

		vector<double> res (N, 0);
		for (int i = 0; i < N; ++i) {
			res[i] = (0.25*wp[i])  + (0.5*owp[i]) + (0.25*oowp[i]);
		}
	
		cout << "Case #" << tc+1 << ":" << endl;
		fprintf (of, "Case #%u:\n", tc+1);
		for (int i = 0; i < N; ++i) {
			printf ("%20.15f\n", res[i]);
			fprintf (of, "%20.15f\n", res[i]);			
		}
		
		//of << "Case #" << tc+1 << ": " << res << endl;
	}
	f.close();
	fclose(of);
	cin.get();
}