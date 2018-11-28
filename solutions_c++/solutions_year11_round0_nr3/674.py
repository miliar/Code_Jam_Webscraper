 
#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <vector>
#include <list>
#include <string>

using namespace std;

int T, N;
int m, s;
int c, x;

int main () {
	
	ifstream fin ("input");
	ofstream fout ("output");
	
	fin >> T;
	for (int t = 1; t <= T; t ++) {
		
		m = 0x7FFFFFFF;
		s = 0;
		x = 0;
		
		fin >> N;
		for (int n = 0; n < N; n ++) {
			fin >> c;
			x ^= c;
			s += c;
			m = min (m, c);
		}
		
		cout << "Case #" << t << ": ";
		fout << "Case #" << t << ": ";
		if (x) {
			cout << "NO" << endl;
			fout << "NO" << endl;
		}
		else {
			cout << s - m << endl;
			fout << s - m << endl;
		}
	}
}