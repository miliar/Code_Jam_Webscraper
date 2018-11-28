#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
typedef long long int ll;

int main() {
	int T;
	fin >> T;
	for(int i=0; i < T; i++) {
		int a, b;
		fin >> a >> b;
		ll k = (1 << a);
		if(b % k == (k-1))
			fout << "Case #" << (i+1) << ": ON\n";
		else
			fout << "Case #" << (i+1) << ": OFF\n";
	}
	return 0;
}
