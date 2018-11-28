#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	unsigned int c, r, k, n;
	fin >> c;
	for (int cn=0; cn<c; cn++) {
		//	Get Input
		fin >> r >> k >> n;
		unsigned int* g = new unsigned int[n];
		for (int i=0; i<n; i++)
			fin >> g[i];
		
		unsigned long int money = 0;
		unsigned int ptr = 0;
		for (int i=0; i<r; i++) {
			unsigned int num = k;
			unsigned int p = ptr;
			while (g[p] <= num) {
				money += g[p];
				num-=g[p];
				p++;
				if (p == n)
					p = 0;
				if (p == ptr)
					break;
			}
			ptr = p;
		}

		fout << "Case #" << (cn+1) << ": "<< money << endl;
	}

	fin.close();
	fout.close();
	return 0;
}