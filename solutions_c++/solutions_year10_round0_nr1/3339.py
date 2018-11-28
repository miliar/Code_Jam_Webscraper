#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main() {
	ifstream file("input.txt");
	ofstream output("output.txt");
	string line;
	long int T;
	long int N;
	long int K;
	long int want;
	if (file.is_open()) {
		if (output.is_open()) {
			getline(file,line);
			T = strtol(&line[0],NULL,10);
			for (int i = 1; i < T+1; i++) {
				getline(file,line);
				N = strtol(&line[0],NULL,10);
				K = strtol(&line[line.find(" ")],NULL,10);
				want = pow(2,N)-1;
				if ((want&K) == want) {
					output << "Case #" << i << ": ON\n";
				}
				else {
					output << "Case #" << i << ": OFF\n";
				}
			}
		}
	}
	return 1;
}
