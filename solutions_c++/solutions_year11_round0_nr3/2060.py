#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main(){
	int t;
	ifstream fin("C-large.in");
	ofstream fout("c2.out");
	fin >> t;
	for(int i = 0; i < t; i++){
		int n, a, s = 0, xor = 0, m = 1000000;
		fin >> n;
		for(int i = 0; i < n; i++){
			fin >> a;
			s += a;
			m = min(m, a);
			xor ^= a;
		}
		fout << "Case #" << i + 1 << ": ";
		if(xor == 0)
			fout << s - m << endl;
		else
			fout << "NO" << endl;
	}
	return 0;
}