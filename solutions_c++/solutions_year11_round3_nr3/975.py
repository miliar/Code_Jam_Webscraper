// ---------------------------------------------------------------------------

#pragma hdrstop

#include <tchar.h>
// ---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>
#include <stdlib>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
using namespace std;

int main() {
	int t;
	ifstream fin("C-small-attempt0(1).in");
	ofstream fout("C.out");
	fin >> t;

	// p = p;

	for (int p = 0; p < t; p++) {

		int n, l, h;


		fin >> n >> l >> h;
		int a[100];
		for (int i = 0; i< n; i++) {
			fin >> a[i];
		}
		int flag = 1;
		int min = l-1;
		for (int i = l; i<=h; i++) {
			flag = 1;
			for (int j = 0 ;j < n; j++)
				if (a[j] % i != 0 && i % a[j] != 0) {
					flag = 0;

					break;
				}
			if (flag) { min = i;break;}
		}




		fout << "Case #" << (p+ 1) << ": ";
		if (min < l) {
			fout << "NO" << endl;
		} else {

				fout  << min;
				fout << endl;

		}
		

	}

	fin.close();

	return 0;
}
// ---------------------------------------------------------------------------
