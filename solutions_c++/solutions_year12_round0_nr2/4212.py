#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int steps(int[]);

int main() {
	ifstream in("B-large.in");
	ofstream out("output.txt");
	string in_line, out_line;
	int T, N, S, p, t, r;
	int s[3];
	
	in >> T;
	for (int i = 0; i < T; i++) {
		r = 0;
		in >> N;
		in >> S;
		in >> p;
		for (int j = 0; j < N; j++) {
			in >> t;
			s[0] = t/3;
			s[1] = (t-s[0])/2;
			s[2] = t-s[0]-s[1];
			if (s[2] >= p){
				r++;
			} else if (S > 0){
				if (s[2]+steps(s) >= p) {
					S--;
					r++;
				}
			}
		}
		out << "Case #" << (i+1) << ": " << r << endl;; 
	}
	in.close();
	out.close();
}

int steps(int s[3]) {
	if (s[2] == 0) {
		return 0;
	}
	if (s[1] == 0) {
		return 0;
	}
	if (s[1]-s[0] > 0) {
		return 1;
	} else {
		if (s[2]-s[1] > 0) {
			return 0;
		} else {
			return 1;
		}
	}
}
