/*
 *  File: Program1.cpp
 *  ------------------
 *
 *  Created by Elina Robeva on 5/7/10.
 *
 */

#include <iostream>
#include <fstream>


using namespace std;

int T;


int power(int n) {
	if(n == 1) return 2;
	int a = 1;
	if(n % 2 == 1) a = 2;
	else a = 1;
	int b = power(n/2); 
	return a * b * b; 
}

int main() {
	ifstream in("/Users/erobeva/Downloads/A-large.in");
	ofstream out("/Users/erobeva/Downloads/AAAout.txt");


		
		
	in >> T; 
	
	for(int i = 0; i < T; ++i) {
		
		int K, N;
		in >> N;
		in >> K;
		
		int p = power(N);
		if((K+1) % p == 0) {
			out << "Case #" << i + 1 << ": ON" << endl;
		} else {
			out << "Case #" << i + 1 << ": OFF" << endl;
		}
	}	

	
	return 0;
	
}

