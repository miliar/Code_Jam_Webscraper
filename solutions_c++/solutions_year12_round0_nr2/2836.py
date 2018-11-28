#include <iostream>
#include <fstream>

using namespace std;

int score[31][2];

void init() {
	for (int i = 0; i <= 30; ++i)
		for (int j = 0; j < 3; ++j)
			score[i][j] = -1;
	for (int i = 0; i <= 10; ++i)
		for (int j = i; j <= i + 2 && j <= 10; ++j)
			for (int k = j; k <= i + 2 && k <= 10; ++k)
				score[i+j+k][(k-i) == 2] = k;
}

void doit() {
	ifstream in = ifstream("test.txt");
	ofstream out = ofstream("answer.txt");
	int T;
	in >> T;
	for (int t = 1; t <= T; ++t) {
		int N, S, P;
		in >> N >> S >> P;
		int total[1000];
		for (int i = 0; i < N; ++i)
			in >> total[i];
		int f[1000] = {0};
		int p[1000] = {0};
		for (int i = 0; i < N; ++i) {
			f[0] = p[0] + (score[total[i]][0] >= P);
			for (int j = 1; j <= S; ++j) 
				f[j] = max(p[j] + (score[total[i]][0] >= P), p[j-1] + (score[total[i]][1] >= P));
			memcpy(p, f, sizeof f);
			memset(f, 0, sizeof f);
		}
		out << "Case #" << t << ": " << p[S] << endl;
	}
	in.close();
	out.close();
}

int main() {
	init();
	doit();
	return 0;
}