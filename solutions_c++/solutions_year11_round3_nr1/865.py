#include <stdio.h>
#include <iostream>
#include <fstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <cmath>
#include <climits>

using namespace std;

int main(int argc, char* argv[]) {
	fstream inf(argv[1]);
	if (!inf) {
		cerr << "cannot open file " << argv[1] << endl;
		return -1;
	}
	string ln; 
	inf >> ln;
	int caseNum = atoi(ln.c_str());
	for (int cn = 0; cn<caseNum; cn++) {
		// read data
		inf >> ln;
		int row = atoi(ln.c_str());
		inf >> ln;
		int col = atoi(ln.c_str());
		vector<string> data; 
		for (int i=0; i<row; i++) {
			inf >> ln;
			data.push_back(ln);
		}

		// find solution
		bool possible = true;
		for (int i=0; i<row; i++) {
			if (i==0) {
				// first line
				int j=0; 
				while (j<col) {
					if (data[i][j] == '#') {
						if ( (j<col-1) && (data[i][j+1] == '#')){
							data[i][j] = '/';
							data[i][j+1] = '\\';
							j += 2;
						}
						else {
							possible = false;
							break;
						}
					}
					else {
						j++;
					}
				}
				if (!possible) break;
			}
			else {
				int j=0; 
				while (j<col) {
					if (data[i][j] == '#') {
						if ((j<col-1) && (data[i][j+1] == '#')){
							int temp = 0; 
							if (data[i-1][j] == '/') {
								for (int k=0; k<=j; k++) {
									if (data[i-1][k] == '/') temp++;
									if (data[i-1][k] == '\\') temp--;
								}
							}
							if ((data[i-1][j] == '/') && (data[i-1][j+1] == '\\') && (temp == 1)){
								data[i][j] = '\\';
								data[i][j+1] = '/';
								j += 2;
							}
							else {
								data[i][j] = '/';
								data[i][j+1] = '\\';
								j += 2;
								if (i==(row-1)){
									possible = false;
									break;
								}
							}
						}
						else {
							possible = false;
							break;
						}
					}
					else {
						int temp = 0; 
						if (data[i-1][j] == '/') {
							for (int k=0; k<=j; k++) {
								if (data[i-1][k] == '/') temp++;
								if (data[i-1][k] == '\\') temp--;
							}
						}
						if ((data[i-1][j] == '/') && 
							(data[i-1][j+1] == '\\') && (temp == 1)){
							possible = false;
							break;
						}
						j++;
					}
				}
			}
		}

		// output
		cout << "Case #" << cn+1 << ":" << endl;
		if (possible) {
			for (int i=0; i<row;i++) {
				cout << data[i] << endl;
			}
		}
		else {
			cout << "Impossible" << endl;
		}
	}
	return 0; 
}