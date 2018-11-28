#include <iostream>
#include <fstream>
#include <string>

using namespace std;

inline int abs(int x) {
	return x > 0 ? x : -x;
}

int main() {

	fstream fin, fout;
	int t;
	int n;
	int prev_o = 1, time_since_o = 0;
	int prev_b = 1, time_since_b = 0;
	int nr;
	int size;
	int time = 0;
	int dist;
	string type;
	int i, j;
	fin.open("A-large-0.in", fstream::in);
	fout.open("A-large-0.out", fstream::out);
	
	fin >> t;
	
	for (i = 0; i < t; ++i) {
		time = 0;
		prev_o = 1;
		prev_b = 1;
		time_since_o = 0;
		time_since_b = 0;
		fin >> size;
		for (j = 0; j < size; ++j) {
			fin >> type >> nr;
			if (type.c_str()[0] == 'O') {
				dist = abs(prev_o - nr) - time_since_o;
				dist = (dist > 0 ? dist : 0) + 1;
				time += dist;
				if (time_since_o > 0) {
					time_since_b = dist;
				} else {
					time_since_b += dist;
				}
				time_since_o = 0;
				prev_o = nr;
			} else if (type.c_str()[0] == 'B') {
				dist = abs(prev_b - nr) - time_since_b;
				dist = (dist > 0 ? dist : 0) + 1;
				time += dist;
				if (time_since_b > 0) {
					time_since_o = dist;
				} else {
					time_since_o += dist;
				}
				time_since_b = 0;
				prev_b = nr;
			}
		}
		fout << "Case #" << i+1 << ": " << time << "\n";
	}
	fin.close();
	fout.close();
	
	return 0;
}
