#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;

fstream in, out;

int t, c, d, n;

char combine[26][26];
bool opp[26][26];

int ctoi(char x) {
	return ((int)x - 'A');
}


int main() {
	in.open("probb.in", fstream::in);
	out.open("probb.out", fstream::out);

	in >> t;

    for (int i = 0; i < t; i++) {
		in >> c;
		string triple;
		for (int jj = 0; jj < 26; jj++) {
			for (int kk = 0; kk < 26; kk++) {
				combine[jj][kk] = 'a';
				opp[jj][kk] = false;
			}
		}
		for (int j = 0; j < c; j++) {
			in >> triple;
			combine[ctoi(triple.at(0))][ctoi(triple.at(1))] = triple.at(2);
			combine[ctoi(triple.at(1))][ctoi(triple.at(0))] = triple.at(2);
		}
		in >> d;
		for (int k = 0; k < d; k++) {
			in >> triple;
			opp[ctoi(triple.at(0))][ctoi(triple.at(1))] = true;
			opp[ctoi(triple.at(1))][ctoi(triple.at(0))] = true;
		}
		in >> n;
		string input;
		in >> input;
		char output[100];
		for (int tt = 0; tt < n; tt++) {
			output[tt] = 'a';
		}
		int loc = -1;
		for (int x = 0; x < n; x++) {
			loc++;
			output[loc] = input.at(x);
			if (loc > 0 && combine[ctoi(output[loc])][ctoi(output[loc - 1])] != 'a') {
				output[loc - 1] = combine[ctoi(output[loc])][ctoi(output[loc - 1])];
				loc--;
			} 

			for (int y = 0; y < loc; y++) {
				if (opp[ctoi(output[y])][ctoi(output[loc])]) {
					loc = -1;
				}
			} 
		}
		
		out << "Case #" << i + 1 << ": [";
		for (int z = 0; z < loc + 1; z++) {
			out << output[z];
			if (z < loc ) {
				out << ", ";
			} else {
				out << "]" << endl;
			}
		}
		if (loc == -1) {
			out << "]" << endl;
		}
	}
    
	in.close();
	out.close();

	return 0;
}
