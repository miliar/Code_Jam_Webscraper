// RPI.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <iostream>
#include <string>

using namespace std;


int _tmain(int argc, _TCHAR* argv[]) {
	
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ++ncase) {
		int n;
		cin >> n;
		vector< string > results;
		for (int i = 0; i < n; ++i) {
			string str;
			cin >> str;
			results.push_back(str);
		}
		vector< int > ngames(n, 0);
		vector<int> nwins(n, 0);
		vector<double> wp(n, 0.0);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (results[i][j] != '.')
					++ngames[i];
				if (results[i][j] == '1')
					++nwins[i];
			}
			wp[i] = (double) nwins[i] / ngames[i];
		}
		vector<double> owp(n, 0.0);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (results[i][j] == '.')
					continue;
				if (results[i][j] == '1') 
					owp[i] += (double) nwins[j] / (ngames[j] - 1);
				else 
					owp[i] += ((double) nwins[j] - 1.0) / (ngames[j] - 1); 
			}
			owp[i] /= ngames[i];
		}
		vector<double> oowp(n, 0.0);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (results[i][j] == '.')
					continue;
				oowp[i] += owp[j];
			}
			oowp[i] /= ngames[i];
		}
		cout << "Case #" << ncase << ":\n";
		for (int i = 0; i < n; ++i) {
			cout << 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i] << endl;
		}
	}
	return 0;
}

