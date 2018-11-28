#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int result(int N, int S, int p, int t[]);

void main () {
	int T,N,S,p,t[100];
	ifstream fin;
	fin.open("B-large.in");
	fin >> T;
	fin.get();

	ofstream fout;
	fout.open("Output.txt");

    for (int i = 0; i < T; i++) {
		fin >> N >> S >> p;
		for (int j = 0; j < N; j++) {
			fin >> t[j];
		}
		fout << "Case #" << i+1 << ": " << result(N, S, p, t) << endl;
    }
	fin.close();
	fout.close();
}

int result(int N, int S, int p, int t[]) {
	int y = 0;
	switch (p) {
	case 0:
		y = N;
		break;
	default:
		for (int i = 0; i < N; i++) {
			if ((t[i] >= 3*p-4) && t[i] > 0) {
				if (t[i] >= 3*p-2) {
					y = y + 1;
				}
				else if (S != 0) {
					y = y + 1;
					S = S - 1;
				}
			}
		}
	}
	return y;
}