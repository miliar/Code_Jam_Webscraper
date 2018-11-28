#include <cmath>
#include <string>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
using namespace std;

int N;
int K;
string S;
int perm[5];

int size(string x) {
	int len = x.length();
	int ret = 0;
	ret ++;
	for (int i = 0; i < len - 1; i++) {
		if (x.at(i) != x.at(i + 1)) {
			ret ++;
		}
	}
	return ret;
}

int findVal(string x) {
	int len = x.length();
	int numTimes = len/K;
	string newString = "";
	for (int i = 0; i < numTimes; i++) {
		for (int j = 0; j < K; j++) {
			newString += x.at(K * i + perm[j] - 1);
		}
	}
	return size(newString);
}

int main() {
	fstream in;
	fstream out;
	in.open("prob4.in", fstream::in);
	out.open("prob4.out",fstream::out);

	in >> N;

	for (int a = 0; a < N; a++) {
		in >> K;
		in >> S;
		for (int b = 0; b < K; b++) {
			perm[b] = b + 1;
		}
		int min = S.length();
		do {
			string test = S;
			int thisVal = findVal(test);
			if (thisVal < min) {
				min = thisVal;
			}
		} while (next_permutation (perm,perm+K));

		out << "Case #" << a + 1 << ": " << min << endl;
	}
	
	in.close();
	out.close();
	return 0;
}