#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
//#include <vector>

using namespace std;

int T, C, D, N;
bool oppose[9][9];
char combine[9][9];
bool buffer[9];
char X,Y,Z;
char curEle, lastChar;

int ele (char c) {
	switch (c) {
	case 'Q':
		return 1;
	case 'W':
		return 2;
	case 'E':
		return 3;
	case 'R':
		return 4;
	case 'A':
		return 5;
	case 'S':
		return 6;
	case 'D':
		return 7;
	case 'F':
		return 8;
	default:
		return 0;
	}
}

int main() {
//	char bah;

	//ifstream fin ("X:\\Dev\\CodeJam\\2011\\Data\\B-small-attempt1.in");
	//ofstream fout ("X:\\Dev\\CodeJam\\2011\\Data\\B-small-attempt1.out");
	//ifstream fin ("X:\\Dev\\CodeJam\\2011\\Data\\B-sample.in");
	//ofstream fout ("X:\\Dev\\CodeJam\\2011\\Data\\B-sample.out");
	ifstream fin ("X:\\Dev\\CodeJam\\2011\\Data\\B-large.in");
	ofstream fout ("X:\\Dev\\CodeJam\\2011\\Data\\B-large.out");

	fin >> T;


	for (int casenum = 1; casenum <= T; casenum++) {		
		for (int i = 0; i < 9; i++) {
			buffer[i] = false;
			for (int j = 0; j < 9; j++) {
				oppose[i][j] = false;
				combine[i][j] = NULL;
			}
		}

		fin >> C; //combines
		

		for(int i = 0; i < C; i++) {
			fin >> X;
			fin >> Y;
			fin >> Z;
			combine[ele(X)][ele(Y)] = Z;
			combine[ele(Y)][ele(X)] = Z;
		}

		fin >> D; //opposes

		for(int i = 0; i < D; i++) {
			fin >> X;
			fin >> Y;
			oppose[ele(X)][ele(Y)] = true;
			oppose[ele(Y)][ele(X)] = true;
		}

		fin >> N; //ele-list

		lastChar = NULL;
		string output = "";
		
		for(int i = 0; i < N; i++) {
			fin >> curEle;

			//check combine
			if (combine[ele(curEle)][ele(lastChar)] != NULL) {
				output.erase(output.length()-1, 1);
				if (output.find_first_of(lastChar) == output.npos) {
					buffer[ele(lastChar)] = false;
				}
				curEle = combine[ele(curEle)][ele(lastChar)];
			} else {
				bool breaknow = false;
				//check clashes
				for(int j = 1; j <= 8; j++) {
					if (buffer[j] == true && oppose[j][ele(curEle)] == true) {
						//clear and reset
						output.clear();
						lastChar = NULL;
						for (int k = 1; k <= 8; k++) {
							buffer[k] = false;
						}
						breaknow = true;
						continue;
					}
				}
				if (breaknow == true)
					continue;
			}

			buffer[ele(curEle)] = true;
			output.push_back(curEle);
			lastChar = curEle;
		}
						
		fout << "Case #" << casenum << ": ";
		fout << "[";
		if (!output.empty()) {
			fout << output[0];
			for (int i = 1; i < output.length(); i++) {
				fout << ", " << output[i];
			}
		}
		fout << "]" << endl;
	}

//cout << "WHAT" << endl; cin >> bah;
}