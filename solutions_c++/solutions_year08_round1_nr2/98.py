#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <set>
using namespace std;

int C;
int N;
int M;

int malted[2000];
int num[2000];

int state[2001];
bool okay;
bool possible;

int compare(const void *a, const void *b) {
	return (*((int*)a)) - (*((int*)b));
}

int main() {
	fstream in;
	fstream out;
	in.open("prob2.in", fstream::in);
	out.open("prob2.out",fstream::out);

	in >> C;
	int t1,t2;

	for (int a = 0; a < C; a++) {
		in >> N;
		in >> M;
		set<int> regular[2000];
		for (int b = 0; b < M; b++) {	
			malted[b] = -1;
			in >> num[b];
			for (int c = 0; c < num[b]; c++) {
				in >> t1 >> t2;
				if (t2 == 1) {
					malted[b] = t1;
				} else {
					regular[b].insert(t1);
				}
			}
		}

		for (int aa = 1; aa <= N; aa++) {
			state[aa] = 0;
		}
		okay = false;
		possible = true;
		
		while (!okay) {
			okay = true;
			for (int d = 0; d < M; d++) {
				if (regular[d].empty()) {
					if (malted[d] == -1) {
						possible = false;
						okay = true;
						break;
					} else if (malted[d] != -2) {
						state[malted[d]] = 1;
						for (int e = 0; e < M; e++) {
							regular[e].erase(malted[d]);
						}
						malted[d] = -2;
						okay = false;
						break;
					}
				}
			}
		}
		if (!possible) {
			out << "Case #" << a + 1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			out << "Case #" << a + 1 << ": ";
			for (int i = 0; i < N; i++) {
				out << state[i+1] << " ";
			}
			out << endl;
		}
	}
	
	in.close();
	out.close();
	return 0;
}