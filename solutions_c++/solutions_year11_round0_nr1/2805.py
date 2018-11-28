#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int ElapsedTime(const vector<int>& vecButtons, int index) {
	return abs(vecButtons[index] - vecButtons[index - 1]);
}

int main(int argc, char* argv[]) {
	if (argc != 2) {
		cerr << "wrong number of parameter" << endl;
		return -1;
	}

	ifstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}

	string ln, ln2; 
	inf >> ln; 
	int n = atoi(ln.c_str());
	for (int i=0; i<n; i++) {
		inf >> ln;
		int buttonNum = atoi(ln.c_str());
		vector<int> vecOrgQue, vecBluQue;
		vector<char> vecColSeq;
		vecOrgQue.push_back(1); // start button
		vecBluQue.push_back(1); // start button
		// read input
		for (int j=0; j<buttonNum; j++) {
			inf >> ln >> ln2; 
			if (ln[0] == 'O') {
				vecOrgQue.push_back(atoi(ln2.c_str()));
				vecColSeq.push_back('O');
			}
			else if (ln[0] == 'B') {
				vecBluQue.push_back(atoi(ln2.c_str()));
				vecColSeq.push_back('B');
			}
		}

		// find solution
		int elapsedTime_T = 0, elapsedTime_C = 0; 
		int orgIndex = 1, bluIndex = 1; 
		char curColor = 0; 
		for (int colseq=0; colseq<vecColSeq.size(); colseq++) {
			if (vecColSeq[colseq] == curColor) {
				int et = 0; 
				if (vecColSeq[colseq] == 'O') {
					et = ElapsedTime(vecOrgQue, orgIndex++);
				}
				else {
					et = ElapsedTime (vecBluQue, bluIndex++);
				}
				elapsedTime_T += (et + 1);
				elapsedTime_C += (et + 1); 
			}
			else {
				int et = 0; 
				if (vecColSeq[colseq] == 'O') {
					et = ElapsedTime(vecOrgQue, orgIndex++);
				}
				else {
					et = ElapsedTime (vecBluQue, bluIndex++);
				}
				curColor = vecColSeq[colseq];
				et -= elapsedTime_C; 
				if (et < 0) et = 0; 
				elapsedTime_C = (et + 1);
				elapsedTime_T += (et + 1);
			}
		}
		cout << "Case #" << i+1 << ": " << elapsedTime_T << endl;
	}

	return 0;
}

