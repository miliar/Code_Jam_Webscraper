#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ofstream fout ("3A.out");
    ifstream fin ("3A.in");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		int N,L[1005],P[1005],totalP=0;
		fin >> N;
		for (int i = 0; i < N; i++) fin >> L[i];
		for (int i = 0; i < N; i++) {
			fin >> P[i];
			totalP += P[i];
		}
		bool used[1000];
		memset(used,false,sizeof(used));
		fout << "Case #" << t << ":";
		for (int i = 0; i < N; i++) {
			int ind = -1;
			for (int j = 0; j < N; j++) {
				if (used[j]) continue;
				if (ind == -1 || P[j] > P[ind]) ind = j;
			}
			used[ind] = true;
			fout << " " << ind;
		}
		fout << endl;
	}
    return 0;
}