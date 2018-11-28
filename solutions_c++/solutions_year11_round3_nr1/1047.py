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
	ifstream fin("A-large(1).in");
	ofstream fout("A.out");
	fin >> t;

	// p = p;

	for (int l = 0; l < t; l++) {

		int n, m;
		char a[50][50];

		fin >> n >> m;
		int k = 0;
		for (int i = 0; i< n; i++) {
			for (int j = 0 ;j < m; j++) {
				fin >> a[i][j];
				if  (a[i][j] == '#') k++;
			}
		}
		int flag = 1;
		for (int i = 0; i< n-1; i++) {
			for (int j = 0 ;j < m-1; j++)
				if (a[i][j] == '#') {
					if (a[i+1][j] == '#' && a[i][j+1] == '#' && a[i+1][j+1] == '#') {
						a[i][j] = '/';
						a[i+1][j] = '\\';
						a[i][j+1] = '\\';
						a[i+1][j+1] = '/';
						k-=4;
					} else {
						flag = 0;break;
                    }
				}
			if (!flag) break;
		}


        if (k!=0) flag = 0;

	    fout << "Case #" << (l + 1) << ": " << endl;
		if (!flag) {
			fout << "Impossible" << endl;
		} else {
			for (int i = 0; i< n; i++) {
				fout << a[i][0];
				for (int j = 1 ;j < m; j++)
					fout  << a[i][j];
				fout << endl;
			}
		}
		

	}

	fin.close();

	return 0;
}
// ---------------------------------------------------------------------------
