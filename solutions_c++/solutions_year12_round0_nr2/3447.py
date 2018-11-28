#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    ofstream fout ("QB.out");
    ifstream fin ("QB.in");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int N,S,p;
		fin >> N >> S >> p;
		int answer=0,possible=0;
		for (int i = 0; i < N; i++) {
			int x;
			fin >> x;
			if (x%3 == 0) {
				if (x/3 >= p) answer++;
				else if (x != 0 && x != 30 && x/3 >= p-1) possible++;
			}
			if (x%3 == 1) {
				if (x/3 >= p-1) answer++;
				//else if (x != 1 && x/3 >= p-2) possible++;
			}
			if (x%3 == 2) {
				if (x/3 >= p-1) answer++;
				else if (x/3 >= p-2) possible++;
			}
		}
		answer += min(S,possible);
		fout << "Case #" << t << ": " << answer << endl;
	}
    return 0;
}