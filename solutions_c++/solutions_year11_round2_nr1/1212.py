#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>

using namespace std;

void calculateWP(const vector<string> & table, vector<double> * wp) {
	for(int i = 0; i < wp->size(); ++i) {
		int wins = 0;
		int loses = 0;
		for (int j = 0; j < table[i].size(); ++j) {
			if (table[i][j] == '1') {
				++wins;
			}
			if (table[i][j] == '0') {
				++loses;
			}
		}
		wp->at(i) = wins * 1.0 / (wins + loses);
	}
}

void calculateOWP(const vector<string> & table, vector<double> * owp) {
	for(int i = 0; i < owp->size(); ++i) {
		double res = 0;
		int count = 0;
		for(int k = 0; k < owp->size(); ++k) {
			if (table[i][k] != '.') {
				int wins = 0;
				int loses = 0;
				for (int j = 0; j < owp->size(); ++j) {
					if (i == j) {
						continue;
					}
					if (table[k][j] == '1') {
						++wins;
					}
					if (table[k][j] == '0') {
						++loses;
					}
				}
				++count;
				res += wins * 1.0 / (wins + loses);
			}
		}
		owp->at(i) = res / count;
	}
}

void calculateOOWP(const vector<string> & table, const vector<double> owp, vector<double> * oowp) {
	for(int i = 0; i < oowp->size(); ++i) {
		double res = 0;
		int count = 0;
		for(int k = 0; k < oowp->size(); ++k) {
			if (table[i][k] != '.') {
				res += owp[k];
				++count;
			}
			oowp->at(i) = res / count;
		}
	}
}


string solveA(ifstream & input) {
	int teamsCount;
	input >> teamsCount;
	vector<string> table(teamsCount);
	for (int i = 0; i < teamsCount; ++i) {
		input >> table[i];
	}
	vector<double> wp(teamsCount);
	vector<double> owp(teamsCount);
	vector<double> oowp(teamsCount);

	calculateWP(table, &wp);
	calculateOWP(table, &owp);
	calculateOOWP(table, owp, &oowp);
	ostringstream res("");
	for(int i = 0; i < teamsCount; ++i) {
		res << '\n';
		//cout << "wp = " << wp[i] << " owp = " << owp[i] << " oowp = " << oowp[i] << endl;
		res << (wp[i] * 0.25 + owp[i] * 0.5 + oowp[i] * 0.25);
	}

	return res.str();
}

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");
	int testCount;
	input >> testCount;
	for (int test = 0; test < testCount; ++test) {
		output << "Case #" << test + 1 << ":" << solveA(input) << endl;
		cout << "Case #" << test + 1 << endl;
	}
	return 0;
}