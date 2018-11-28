/*
 * 2---Dancing With the Googlers_small_large.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: fjywade
 */


#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("/home/fjywade/Desktop/B-large.in");
	ofstream fout("/home/fjywade/Desktop/B-large.out", ios::app);
	int T, N, S, p, count = 1, result;
	fin >>T;
	int* max_n = new int[N];
	int* max_s = new int[N];
	while(!fin.eof()) {
		fin >>N >>S >>p;
		int* t = new int[N];
		result = 0;
		for(int i = 0; i < N; i++) {
			fin >>t[i];
			max_n[i] = t[i]/3 +(t[i]%3>0?1:0);	//such beautiful code!

			if(t[i] < 2 || t[i] > 28) max_s[i] = -1;
			else max_s[i] = t[i]/3 +1 +t[i]%3/2;

			if(S > 0 && max_n[i] < p && max_s[i] >= p) {
				S--; result++; max_s[i] = -2;
			}
		}
		for(int i = 0; i < N; i++) {
			if(max_s[i] >= -1 && max_n[i] >= p) result++;
		}
		if(count <= T)
			fout <<"Case #" <<count++ <<": " <<result <<endl;

		delete t;
	}
	delete max_s;
	delete max_n;
	fout.close();
	fin.close();

	return 0;
}

