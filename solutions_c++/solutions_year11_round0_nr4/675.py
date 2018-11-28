 
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

int T, N, nums [1001], cnt;

int main () {
	
	ifstream fin ("input");
	ofstream fout ("output");
	
	fin >> T;
	for (int t = 1; t <= T; t ++) {
		
		fin >> N;
		cnt = 0;
		for (int i = 1; i <= N; i ++) {
			fin >> nums [i];
			if (nums [i] != i) cnt ++;
		}
		
		cout << "Case #" << t << ": " << cnt << ".000000" << endl;
		fout << "Case #" << t << ": " << cnt << ".000000" << endl;
	}
}