#include <iostream>
#include <fstream>
using namespace std;

int main() {
	int T;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	int mm[5000];
	fin >> T;
	for (int i = 1; i <= T; i++) {
		int A;
		int B;
		int num = 0;
		fin >> A;
		fin >> B;
		int n, m;
		int digitsnum = 0;
		int tenfactor = 1;
		int tmp = A;
		while (tmp != 0) {
			tmp = tmp / 10;
			digitsnum++;
		}
		for (int j = 1; j < digitsnum; j++) {
			tenfactor = tenfactor * 10;
		}
		for (n = A; n < B; n++) {
			for (int j = 0; j < 5000; j++) {
				mm[j] = 0;
			}
			tmp = n;
			int tmp2 = tenfactor;
			int factor = 1;
			for (int j = 1; j <= digitsnum ; j++) {
					tmp = tmp / 10;
					factor = factor * 10;
					m = tmp + (n-tmp*factor) * tmp2; 
					tmp2 = tmp2/10;
					if (m > n && m <= B && mm[m]==0) {
						num++;
						mm[m]=1;
					}
			}
		}
		fout << "Case #" << i << ": " << num << endl;
	}
}