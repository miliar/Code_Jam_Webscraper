//============================================================================
// Name        : round1A_1.cpp
// Author      : Toqa Osama
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <list>

using namespace std;

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, N;
	cin >> t;
	for (int test = 1; test <= t; test++) {
		cin >> N;
		vector<string> s(N);
		vector<pair<int, int> > w(N);
		vector<double> RPI(N);
		vector<double> OWP(N);
		vector<double> OOWP(N);
		for (int i = 0; i < N; i++) {
			cin >> s[i];
			int tot = 0;
			int win = 0;
			for (int j = 0; j < N; j++) {
				if (s[i][j] == '1') {
					win++;
					tot++;
				} else if (s[i][j] == '0') {
					tot++;
				}
			}
			w[i] = make_pair(win, tot);
			RPI[i] += 0.25 * ((double) win / (double) tot);
		}
		cout<<"Case #"<<test<<":\n";
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < s[i].size(); j++) {
				if (s[i][j] != '.') {
					if (s[i][j] != '1')
						OWP[i] += ((double) (w[j].first - 1)
								/ (double) (w[j].second - 1));
					else
						OWP[i] += ((double) (w[j].first)
								/ (double) (w[j].second - 1));
				}
			}
			OWP[i] = OWP[i] / (double) w[i].second;
			RPI[i] += 0.50 * OWP[i];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < s[i].size(); j++) {
				if (s[i][j] != '.') {
					OOWP[i] += OWP[j];
				}
			}
			OOWP[i] = OOWP[i] / (double) w[i].second;
			RPI[i] += 0.25 * OOWP[i];
			cout<<RPI[i]<<endl;
		}

	}
	return 0;
}
