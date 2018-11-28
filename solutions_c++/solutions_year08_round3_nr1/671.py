//============================================================================
// Name        : CGJ200801.cpp
// Author      : liudapeng
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int N, P, K, L;
int p[1024];

int main() {
	
	ifstream in("F:\\in");
	ofstream out("F:\\out");

	in >> N;
//	cout << N << endl;
	for (int t = 1; t <= N; ++t) {
		
		in >> P >> K >> L;
		for (int i = 0; i < L; ++i) {
			in >> p[i];
		}
		std::sort(&p[0], &p[L]);
		int i = L - 1;
		int sum = 0;
		int rate = 1;
		while(i >= 0) {
			for (int j = 0; j < K && i >= 0; ++j) {
				sum += (p[i--] * rate);
			}
			rate++;
		}
		cout << "Case #" << t << ": " << sum << endl;
		out << "Case #" << t << ": " << sum << endl;
	}
	
	return 0;
}
