/*
 * 3---Recycled Numbers_small.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: fjywade
 */


#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string& operator++(string& s, int)
{
	bool flag = false;
	if(s[s.size()-1] != '9') {
		s[s.size()-1] += 1;
	} else {
		for(int i = s.size()-1; i > 0; i--) {
			if(s[i] == '9') {
				flag = true;
				s[i] = '0';
			} else {
				s[i] += 1;
				flag = false;
				break;
			}
		}
		if(flag == true) {
			if(s[0] == '9') {
				s[0] = '0';
				s = "1" +s;
			} else {
				s[0] += 1;
			}
		}
	}
	return s;
}

long make(string A, string B)
{
	long result = 0;
	int size = B.size();
	string current = A;

	if(B.size() < 2) return result;
	while(current < B) {
		string tmp = current;
		for(int i = 0; i < size-1; i++) {
			string tmp1 = tmp;
			char c = tmp[size-1];
			for(int j = size-2; j >= 0; j--) tmp[j+1] = tmp[j];
			tmp[0] = c;
			if(tmp > current && tmp <= B) result++;
		}
		current++;
	}

	return result;
}

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out", ios::app);
	int T, count = 1;
	fin >>T;
	while(!fin.eof()) {
		string A, B;
		fin >>A >>B;
		if(count <= T)
			fout <<"Case #" <<count++ <<": " <<make(A, B) <<endl;
	}
	fout.close();
	fin.close();

	return 0;
}

