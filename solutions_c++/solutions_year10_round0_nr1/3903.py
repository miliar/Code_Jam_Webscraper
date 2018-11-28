#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector <bool> tobase2(unsigned long long in){
	vector <bool> out;
	while (in != 0) {
		out.push_back( (in % 2)? true : false);
		in >>= 1;
	}
	return out;
}


int main (int argc, char * const argv[]) {
	ifstream fin(argv[1]);
	unsigned long long T;
	fin >> T;
	
	for(unsigned long long i = 0; i != T; ++i) {
		unsigned long long N,K;
		fin >> N >> K;
		vector <bool> binary = tobase2(K);
		if (N > binary.size()) {
			cout <<"Case #" << i+1 << ": OFF" << endl;
		} else {
			bool lighton = true;
			for (unsigned long long j = 0; j != N; j++) {
				if (binary[j] == false){
					lighton = false;
					break;
				}
			}
			if (lighton == true){
				cout <<"Case #" << i+1 << ": ON" << endl;
			} else {
				cout <<"Case #" << i+1 << ": OFF" << endl;
			}
		}
	}
    return 0;
}
