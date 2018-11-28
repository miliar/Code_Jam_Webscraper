//#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int T, N, K;
bool on[30];
bool powered[30];

int main() {
	ifstream fin ("X:\\Dev\\CodeJam\\2010\\Data\\A-large.in");
	ofstream fout ("X:\\Dev\\CodeJam\\2010\\Data\\A-large.out");

	fin >> T;

	for (int casenum = 1; casenum <= T; casenum++) {		
		
		fin >> N;
		fin >> K;

		fout << "Case #" << casenum << ": ";
		/*for (int snapper = 0; snapper < N; snapper++) {
			on[snapper] = false;
			powered[snapper] = false;
		}
		powered[0] = true;
		for (int finger = 0; finger < K; finger++) {
			for (int snapper = 0; snapper < N; snapper++) {
				if (powered[snapper]) {
					on[snapper] = !on[snapper];
				}
			}
			for (int snapper = 1; snapper < N; snapper++) {
				if (on[snapper-1] && powered[snapper-1]) {
					powered[snapper] = true;
				} else {
					powered[snapper] = false;
				}
			}
		}
		if (powered[N-1] && on[N-1]) {
			fout << "ON" << endl;
		} else {
			fout << "OFF" << endl;
		}*/
		//Hehe, easier formula by math. but i'll use it only if large is too big to solve.. aaand it was.
		if (((K+1) % (int)(pow((double)2,N)))==0) {
			fout << "ON" << endl;
		} else {
			fout << "OFF" << endl;
		}
	}
	//char bah;
	//cin >> bah;
}