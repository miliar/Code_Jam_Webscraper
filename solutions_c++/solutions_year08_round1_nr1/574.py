#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

int main() {
	int T, n;
	ifstream fin("a.in");
	ofstream fout("a.out");
	vector<long long> va, vb;
	long long dot;
	
	fin >> T;
	
	for(int t = 1; t <= T; t++) {
		cout << t << endl;
		fin >> n;
		va.resize(n);
		vb.resize(n);
		
		for(int i = 0; i < n; i++) {
			fin >> va[i];
		}
		sort(va.begin(), va.end(), greater<int>());
		
		for(int i = 0; i < n; i++) {
			fin >> vb[i];
		}
		sort(vb.begin(), vb.end(), less<int>());
		
		dot = 0;
		for(int i = 0; i < n; i++) {
			dot += va[i] * vb[i];
		}
			
		fout << "Case #" << t << ": " << dot << endl;
	}
	
	fin.close();
	fout.close();
	
	return 0;
}