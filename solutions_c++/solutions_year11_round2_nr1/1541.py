#include <stdio.h>
#include <iostream>
#include <fstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>
#include <climits>

using namespace std;

int main(int argc, char* argv[]) {
	fstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}
	string ln; 
	inf >> ln;
	int caseNum = atoi(ln.c_str());
	for (int cn = 0; cn<caseNum; cn++) {
		// read team records
		inf >> ln;
		int teamNum = atoi(ln.c_str());
		vector< vector<int> > teamRecs;
		for (int tn = 0; tn<teamNum; tn++) {
			vector<int> teamRec;
			inf >> ln;
			for (int i=0; i<teamNum; i++) {
				if (ln[i] == '.') {
					teamRec.push_back(-1);
				}
				else if (ln[i] == '1') {
					teamRec.push_back(1);
				}
				else {
					teamRec.push_back(0);
				}
			}
			teamRecs.push_back(teamRec);
		}

		// find solution
		
		// WP
		vector<double> WPS;
		

		for (int i=0; i<teamNum; i++) {
			vector<int> vec = teamRecs[i];
			int wins = 0;
			int plays = 0;
			for (int j=0; j<teamNum; j++) {
				if (vec[j] == 1){
					wins++;
				}
				if (vec[j] != -1) {
					plays++;
				}
			}
			WPS.push_back((double)wins / plays);
		}

		vector< vector<double> > partWPS;
		for (int i=0; i<teamNum; i++) {
			// calculate i's part WPS
			vector<int> vec = teamRecs[i];
			vector<double> part;

			for (int j=0; j<teamNum; j++) {
				// calculate WPS without j
				if (i == j) {
					part.push_back(0);
				}
				else {
					int plays = 0;
					double total = 0; 
					for (int k=0; k<teamNum; k++) {
						if (k==j) continue;
						if (vec[k] != -1) {
							plays++;
						}
						if (vec[k] == 1) {
							total += 1;
						}
					}
					part.push_back(total / plays);
				}
			}
			partWPS.push_back(part);
		}

		// OWP
		vector<double> OWPS;
		for (int i=0; i<teamNum; i++) {
			vector<int> vec = teamRecs[i];
			int plays = 0; 
			double total = 0; 
			for (int j=0; j<teamNum; j++) {
				if (vec[j] != -1) {
					plays++;
					// special WPS
					//total += WPS[j];
					total += partWPS[j][i];
				}
			}
			OWPS.push_back(total / plays);
		}

		// OOWP
		vector<double> OOWPS;
		for(int i=0; i<teamNum; i++) {
			vector<int> vec = teamRecs[i];
			int plays = 0; 
			double total = 0; 
			for (int j=0; j<teamNum; j++) {
				if (vec[j] != -1) {
					plays++;
					total += OWPS[j];
				}
			}
			OOWPS.push_back(total / plays);
		}


		// output result
		cout << "Case #" << cn+1 << ": " << endl;
		for (int i=0; i<teamNum; i++) {
			printf("%.12f\n", 0.25*WPS[i] + 0.5 * OWPS[i] + 0.25 * OOWPS[i]);
		}
	}
	return 0; 
}