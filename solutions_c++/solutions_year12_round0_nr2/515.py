#include <iostream>
#include <fstream>

using namespace std;
ofstream fout ("output.out");
ifstream fin ("input.in");

#define MAX_N	100

int T, cases;
int N, S, p;
int score[MAX_N];

void work() {
	int result = 0;
	int i;
	for (i=0; i<N; i++) {
		if (p >= 2) {
			if (score[i] >= 3*p-2) {
				result ++;
			}
			else if (S > 0 && score[i] >= 3*p-4) {
				result ++;
				S --;
			}
		}
		else {
			if (score[i] >= 3*p-2) {
				result ++;
			}
		}
	}
	fout << "Case #" << cases << ": " << result << endl;
}

int main() {
	fin >> T;
	for (cases=1; cases<=T; cases++) {
		fin >> N >> S >> p;
		for (int i=0; i<N; i++) {
			fin >> score[i];
		}
		work();
	}
	return 0;
}
