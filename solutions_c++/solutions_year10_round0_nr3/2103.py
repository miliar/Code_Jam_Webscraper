/*
 * C.cpp
 *
 *  Created on: May 7, 2010
 *      Author: Ningfeng
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	int T, R, k, N;
	int group[10];
	ifstream fin("C-small.in");
	ofstream fout("C-small.out");
	fin >> T;
	for(int i=1; i<=T; i++) {
		int total = 0;
		fin >> R >> k >> N;
		//cout << "Case #" << i << endl;
		//cout << "k is: " << k << endl;
		for(int j=0; j<N; j++) {
			int num;
			fin >> num;
			group[j]= num;
			//cout << group[j] << endl;
		}
		int p = 0; //current group
		for(int s=0; s<R; s++ ) {
			int rideSum = 0;
			int aboarded = 0;
			while((rideSum + group[p]) <= k && aboarded < N) {
				rideSum += group[p];
				aboarded++;
				p = (p+1)%N;
			}
			//cout << "rideSum is: " << rideSum << endl;
			total += rideSum;
			//cout << "total is: " << total << endl;
		}
		fout << "Case #" << i << ": " << total << endl;

	}
	return 0;
}
