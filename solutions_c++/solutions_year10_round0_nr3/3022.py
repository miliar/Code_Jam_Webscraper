#include <iostream>
#include <fstream>
//#include <string>
//#include <vector>

using namespace std;

int T, R, k, N;
int group[1000];
int cache[1000];
int cash_cache[1000];

int main() {
//	char bah;

	ifstream fin ("X:\\Dev\\CodeJam\\2010\\Data\\C-small-attempt1.in");
	ofstream fout ("X:\\Dev\\CodeJam\\2010\\Data\\C-small-attempt1.out");
	//ifstream fin ("X:\\Dev\\CodeJam\\2010\\Data\\C-sample.in");
	//ofstream fout ("X:\\Dev\\CodeJam\\2010\\Data\\C-sample.out");

	fin >> T;


	for (int casenum = 1; casenum <= T; casenum++) {		


		fin >> R; //times run
		fin >> k; //k people at a time
		fin >> N; //groups of people

		for(int i = 0; i < N; i++) {
			fin >> group[i];
			cache[i] = -1;
			cash_cache[i] = 0;
		}


		int curG = 0;
		int curSum = 0;
		int startG = 0;
		int cash = 0;
		for(int ride = 0; ride < R; ride++) {
			curSum = 0;
			if (cache[curG] != -1) {				
				cash += cash_cache[curG];
				curG = cache[curG];
			} else {
				startG = curG;
				while(true) {
					if ((curSum + group[curG]) <= k) {
						curSum += group[curG];
						curG++;
						if (curG == N) { curG = 0; }
						if (curG == startG) { break; }
					} else {
						break;
					}
				}
				cache[startG] = curG;
				cash_cache[startG] = curSum;
				cash += curSum;
			}			
		}

		fout << "Case #" << casenum << ": " << cash << endl;
	}

//cout << "WHAT" << endl; cin >> bah;
}