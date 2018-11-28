#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

#include <math.h>

using namespace std;

void CalcWP(vector<vector<string>> &s, vector<int> wp, int &N)
{
	for (int j = 0; j < N; j++) {
			int n = 0;						// 誰かと対戦した回数
			for (int k = 0; k < N; k++) {
				if (s[j][k] == "1") {
					wp[j] += 1; 
					n++;
				}
				else if (s[j][k] == "0")
					n++;
			}
			wp[j] /= n;
		}
}

int main(void)
{
	ifstream cin("R1B-A-large.in");//RA-small-attempt2.in");
	ofstream ofs("R1B-A-largeO.txt");
	//ifstream cin("R1test.txt");
	//ofstream ofs("R1testO.txt");
	int T, N;
	vector<long double> RPI;
	vector<vector<string>> s;
	vector<long double> WP;
	vector<long double> OWP;
	vector<long double> OOWP;
	vector<long double> w;//vector<double>

	cin >> T;

	for (int i = 0; i < T; i++) {
		w.clear(); OWP.clear(); OOWP.clear(); WP.clear();
		cin >> N;
		cin.ignore();
		s.resize(N);
		WP.resize(N);
		OWP.resize(N);
		w.resize(N);
		OOWP.resize(N);
		RPI.resize(N);
		for (int j = 0; j <N; j++) {
			s[j].resize(N);
			//w.resize(N);
		}

		// load
		for (int j = 0; j < N; j++) {
			string str;
			getline(cin, str);
			for (int k = 0; k < N; k++)
				s[j][k] = str[k];
		}

		// calc
		// WP
		for (int j = 0; j < N; j++) {
			int n = 0;						// 誰かと対戦した回数
			for (int k = 0; k < N; k++) {
				if (s[j][k] == "1") {
					WP[j] += 1; 
					n++;
				}
				else if (s[j][k] == "0")
					n++;
			}
			WP[j] /= n;
		}

		//OWP
		for (int j = 0; j < N; j++) {
			int n = 0;						// 誰かと対戦した回数
			//int wp = 0;					// OWP用のWP
			for (int k = 0; k < N; k++) {
				w.clear();
				w.resize(N);
				if (s[j][k] == "1" || s[j][k] == "0") {
					// calc wp 4 OWP
					/*for (int l = 0; l < N; l++) {
						int t = 0;
						for (int m = 0; m < N; m++) {
							if (m != j && s[l][m] == "1") {// k
								w[l] += 1;
								t++;
							}
							else if (s[l][m] == "0")
								t++;
						}
						w[l] /= t;
					}*/
					int t = 0;
					// 対戦していたら"そのチームの"WPを計算しに行く
					for (int l = 0; l < N; l++) {
						if (l != j) {
							if (s[k][l] == "1") {
								w[j] += 1;
								t++;
							}
							else if (s[k][l] == "0")
								t++;
						}
					}
					w[j] /= t;//w[j] = w[j] / t;

					OWP[j] += w[j];
					n++;
				}
			}
			OWP[j] /= n;
		}

		// OOWP
		for (int j = 0; j < N; j++) {
			int n = 0;
			for (int k = 0; k < N; k++) {
				if (s[j][k] == "1" || s[j][k] == "0") {
					OOWP[j] += OWP[k];//j
					n++;
				}
			}
			OOWP[j] /= n;
		}

		// RPI
		for (int j = 0; j < N; j++)
			RPI[j] = .25 * WP[j] + .50 * OWP[j] + .25 * OOWP[j];

		/*for (int j = 0; j < N; j++) {
			for (int k = 0; k < N; k++)
				ofs << s[j][k] << flush;
			ofs << endl;
		}
		ofs << endl;*/

		ofs << "Case #" << i + 1 << ":" << endl;
		for (int j = 0; j < N; j++) {
			/*ofs << WP[j] << endl;
			ofs << OWP[j] << endl;
			ofs << OOWP[j] << endl;*/
			ofs << RPI[j] << endl;
			//ofs << endl;
		}
		
	}


	return 0;
}