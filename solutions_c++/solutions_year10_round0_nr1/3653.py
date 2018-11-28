#include <iostream>
#include <fstream>

using namespace std;

int main() {
	int n , k, pow, m;
	ifstream fin("A-large.in");
	ofstream fout("A-small.out");
	fin >> m;
	for (int i = 1;i <= m;i++) {
		fin >> n >> k;
		pow = 1;
		for (int j = 0;j < n;j++)
			pow *= 2;
		if ((k % pow) == (pow - 1))
			fout << "Case #" << i << ": ON\n";
		else
			fout << "Case #" << i << ": OFF\n";

	}
	
}
