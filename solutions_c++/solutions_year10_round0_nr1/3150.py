//============================================================================
// Name        : snapper_chain.cpp
// Author      : shailesh
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

bool get_light_status(int N, int K) {
	int number = K % (int) pow((long double) 2, (long double) N);
	for (int i = 0; i < N; i++) {
		if (((number >> i) & 1) == 0) {
			return false;
		}
	}
	return true;

}

int main() {
	int num_of_tests = 0;
	int N;
	int K;
	string line;
//	ifstream myfile("example.txt");
	ifstream myfile("A-large.in");
	ofstream out_file("A-large.out");
	myfile >> num_of_tests;
	int i = 0;
	while (i < num_of_tests) {
		myfile >> N;
		myfile >> K;
		bool res = get_light_status(N, K);
		if (res == true) {
//			cout << "CASE #" << (i + 1) << ": ON" << endl;
			out_file << "Case #" << (i + 1) << ": ON" << endl;
		} else {
//			cout << "CASE #" << (i + 1) << ": OFF" << endl;
			out_file << "Case #" << (i + 1) << ": OFF" << endl;
		}
		i++;
	}
	return 0;
}
