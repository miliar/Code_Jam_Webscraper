#include <vector>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

const int MAX = 105;

int main(void) {
	int T; cin >> T;
	for(int t = 0; t < T; ++t) {
		int N; cin >> N;
		vector<string> data;

		double WP[MAX][MAX];
		double OWP[MAX];
		double OOWP[MAX];

		for(int n = 0; n < N; ++n) {
			string s; cin >> s;
			data.push_back(s);
		}
		for(int n = 0; n < N; ++n) {
			string& s = data[n];
			int battle = 0;
			int win = 0;
			for(int i = 0; i < N; ++i) {
				char c = s[i];
				battle += (c != '.');
				win += (c == '1');
			}
			for(int i = 0; i < N; ++i) {
				char c = s[i];
				WP[n][i] = (double)(win - (c=='1')) / (battle - (c!='.'));
			}
		}
		for(int n = 0; n < N; ++n) {
			string& s = data[n];
			int battle = 0;
			double sum_wp = 0.;
			for(int i = 0; i < N; ++i) {
				char c = s[i];
				battle += (c != '.');
				sum_wp += (c != '.')*(WP[i][n]);
			}
			OWP[n] = sum_wp / battle;
		}
		for(int n = 0; n < N; ++n) {
			string& s = data[n];
			int battle = 0;
			double sum_owp = 0.;
			for(int i = 0; i < N; ++i) {
				char c = s[i];
				battle += (c != '.');
				sum_owp += (c != '.')*(OWP[i]);
			}
			OOWP[n] = sum_owp / battle;
		}

		cout << "Case #" << (t+1) << ":" << endl;
		for(int n = 0; n < N; ++n) {
			double RPI = 0.25 * WP[n][n] + 0.50 * OWP[n] + 0.25 * OOWP[n];
			cout << setprecision(12) << RPI << endl;
		}
	}
	return 0;
}
