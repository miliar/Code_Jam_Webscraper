#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(void) {
	int i, j, nrTest, tTime, fromA, fromB, indIdo, erkIdo;
	string auxSt, ind, erk;
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	vector <int> aStart, aStop, bStart, bStop;
	vector <int> idoA(1500, 0), idoB(1500, 0);
	in >> nrTest;
	
	for (i = 1; i <= nrTest; i++) {
		aStart.clear(); aStop.clear(); bStart.clear(); bStop.clear();
		for (j = 0; j < 24*60; j++) {
			idoA[j] = 0;
			idoB[j] = 0;
		}
		int indexAStart = 0, indexAStop = 0, indexBStart = 0, indexBStop = 0, rezA = 0, rezB = 0;
		in >> tTime;
		in >> fromA >> fromB;
		for (j = 0; j < fromA; j++) {
			in >> ind >> erk;
			indIdo = ((ind[0] - '0') * 10 + ind[1] - '0') * 60 + (ind[3] - '0') * 10 + ind[4] - '0';
			erkIdo = ((erk[0] - '0') * 10 + erk[1] - '0') * 60 + (erk[3] - '0') * 10 + erk[4] - '0' + tTime;
			aStart.push_back(indIdo);
			bStop.push_back(erkIdo);
		}
		for (j = 0; j < fromB; j++) {
			in >> ind >> erk;
			indIdo = ((ind[0] - '0') * 10 + ind[1] - '0') * 60 + (ind[3] - '0') * 10 + ind[4] - '0';
			erkIdo = ((erk[0] - '0') * 10 + erk[1] - '0') * 60 + (erk[3] - '0') * 10 + erk[4] - '0' + tTime;
			bStart.push_back(indIdo);
			aStop.push_back(erkIdo);
		}
		sort(aStart.begin(), aStart.end()); 
		sort(aStop.begin(), aStop.end()); 
		sort(bStart.begin(), bStart.end()); 
		sort(bStop.begin(), bStop.end());
		for (j = 0; j < 24 * 60; j++) {
			if (j == 0) {
				idoA[j] = 0;
				idoB[j] = 0;
			} else {
				idoA[j] = idoA[j-1];
				idoB[j] = idoB[j-1];
			}
			
			bool flag = true;
			while (flag) {
				if (indexAStop < aStop.size()) {
					if (aStop[indexAStop] == j) {
						indexAStop++;
						idoA[j]++;
					} else {
						flag = false;
					}
				} else {
					flag = false;
				}
			}
			flag = true;
			while (flag) {
				if (indexAStart < aStart.size()) {
					if (aStart[indexAStart] == j) {
						indexAStart++;
						idoA[j]--;
					} else {
						flag = false;
					}
				} else {
					flag = false;
				}
			}
			flag = true;
			while (flag) {
				if (indexBStop < bStop.size()) {
					if (bStop[indexBStop] == j) {
						indexBStop++;
						idoB[j]++;
					} else {
						flag = false;
					}
				} else {
					flag = false;
				}
			}
			flag = true;
			while (flag) {
				if (indexBStart < bStart.size()) {
					if (bStart[indexBStart] == j) {
						indexBStart++;
						idoB[j]--;
					} else {
						flag = false;
					}
				} else {
					flag = false;
				}
			}
		}
		for (j = 0; j < 24 * 60; j++) {
			rezA = min(rezA, idoA[j]);
			rezB = min(rezB, idoB[j]);
		}
		rezA *= -1;
		rezB *= -1;
		out << "Case #" << i << ": " << rezA << " " << rezB << endl;
	}
	return 0;
}
