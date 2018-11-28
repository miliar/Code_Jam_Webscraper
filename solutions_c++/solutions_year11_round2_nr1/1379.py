// 1B_task1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
    fstream f_in("in2.in", ios::in);
    fstream f_out("out2.txt", ios::out);
	int T;
	f_in >> T;
	for (int i = 0; i < T; ++i) {
		int N;
		f_in >> N;
		int **arr = new int*[N];
		for (int j = 0; j < N; ++j) {
			arr[j] = new int[N];
		}
		for (int j1 = 0; j1 < N; ++j1) {
			for (int j2 = 0; j2 < N; ++j2) {
				char symb;
				f_in >> symb;
				if (symb == '.') {
					arr[j1][j2] = -1;
				} else if (symb == '1') {
					arr[j1][j2] = 1;
				} else if (symb == '0') {
					arr[j1][j2] = 0;
				}
				//cout << arr[j1][j2] << " ";
			}
		}
		f_out << "Case #" << i + 1 << ":" << endl;
		double WP2 = 0, OWP2 = 0, OOWP2 = 0;
		double *WP = new double[N];
		double *OWP = new double[N];
		double *OOWP = new double[N];
		memset(OOWP, 0, sizeof(double) * N);
		for (int j = 0; j < N; ++j) {
			OOWP[j] = 0;
		}
		memset(WP, 0, sizeof(double) * N);
		memset(OWP, 0, sizeof(double) * N);
		double games = 0;
		for (int j = 0; j < N; ++j) {
			games = 0;
			for (int j1 = 0; j1 < N; ++j1) {
				if (arr[j][j1] != -1) {
					++games;
					WP[j] += arr[j][j1];
				}
			}
			WP[j] /= games;
		}
		for (int j = 0; j < N; ++j) {
			games = 0;double cur_sum = 0;
			for (int j1 = 0; j1 < N; ++j1) {
				if (j1 == j) {
					continue;
				}
				int sum = 0;
				if (arr[j][j1] != -1) {
					for (int y = 0; y < N; ++y) {
						if (arr[j1][y] != -1) {
							++sum;
						}
					} 		
					OWP[j] += (WP[j1] * sum - arr[j1][j]) / (sum - 1);
					++games;
				}

				/*if (arr[j][j1] == 0) {
					OWP -= arr[j][j1] / sum;
				}*/
			}
			OWP[j] /= games;
		}
		for (int j = 0; j < N; ++j) {
			games = 0;
			for (int j1 = 0; j1 < N; ++j1) {
				if (j1 == j) {
					continue;
				}
				if (arr[j][j1] != -1) {
					OOWP[j] += OWP[j1];
					++games;
				}
				
			}
			OOWP[j] /= games;
		}
		for (int j = 0; j < N; ++j) {
			f_out << 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j] << endl;
		}
				
	}
    return 0;
}


