//============================================================================
// Name        : codejam2011-A2-a.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

int main() {
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	for (int Ti = 1; Ti <= T; ++Ti) {
		int N;
		cin >> N;
		vector<double> wp(N);
		vector<double> owp(N);
		vector<double> oowp(N);
		vector<vector<char> > m(N);
		for (int i = 0; i < N; ++i) {
			m[i].resize(N);
			for (int j = 0; j < N; ++j) {
				char ch;
				cin >> m[i][j];
			}
		}
		for (int i = 0; i < N; ++i) {
			int sz = 0;
			for (int j = 0; j < N; ++j) {
				if (m[i][j] != '.' && i != j) {
					wp[i] += m[i][j] - '0';
					++sz;
				}
			}
			wp[i] /= sz;
		}
		for (int i = 0; i < N; ++i) {
			int sz = 0;
			for (int j = 0; j < N; ++j) {
				if (m[i][j] != '.' && i != j) {
					double wp = 0.0;
					int wp_sz = 0;
					for (int k = 0; k < N; ++k)
						if (k != i && k != j && m[j][k] != '.') {
							wp += m[j][k] - '0';
							++wp_sz;
						}
					owp[i] += wp / wp_sz;
					++sz;
				}
			}
			owp[i] /= sz;
		}
		for (int i = 0; i < N; ++i) {
			int sz = 0;
			for (int j = 0; j < N; ++j) {
				if (m[i][j] != '.' && i != j) {
					oowp[i] += owp[j];
					++sz;
				}
			}
			oowp[i] /= sz;
		}
		cout << "Case #" << Ti << ":" << endl;
		for (int i = 0; i < N; ++i)
			cout << wp[i] / 4 + owp[i] / 2 + oowp[i] / 4 << endl;
	}
	return 0;
}
