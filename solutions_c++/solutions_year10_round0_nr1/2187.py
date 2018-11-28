/*
 * A.cpp
 *
 *  Created on: May 7, 2010
 *      Author: Ningfeng
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

bool light_on(int N, int K){
	int chain = pow(2.0, N*1.0);
	int r = chain-1;
	if(K%chain == r) return true;
	return false;
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int T, N, K;
	fin >> T;
	for(int i=1; i<=T; i++) {
		fin >> N >> K;
		if(light_on(N, K))
			fout << "Case #" << i << ": ON" << endl;
		else
			fout << "Case #" << i << ": OFF" << endl;

	}
	return 0;
}
