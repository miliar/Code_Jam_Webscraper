// 1C_task1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;
int _tmain(int argc, _TCHAR* argv[])
{
    fstream f_in("in2.in", ios::in);
    fstream f_out("out2.txt", ios::out);
	int T;
	f_in >> T;
	for (int i = 0; i < T; ++i) {
		f_out << "Case #" << i + 1 << ": " << endl;
		int R, C;
		f_in >> R >> C;
		int **arr = new int*[R];
		for (int j = 0; j < R; ++j) {
			arr[j] = new int [C];
			memset(arr[j], 0, sizeof(int) * C);
		}
		bool has_blue = false;
		for (int j = 0; j < R; ++j) {
			for (int k = 0; k < C; ++k) { 
				char symb;
				f_in >> symb;
				if (symb == '.') {
					arr[j][k] = 0;
				} else if (symb == '#') {
					arr[j][k] = 1;
					has_blue = true;
				}
			}
		}

		bool impossible = false;
		for (int j1 = 0; j1 < R; ++ j1) {
			for (int j2 = 0; j2 < C; ++j2) {
				if (arr[j1][j2] == 1) {
					if (j1 == R-1 || j2 == C-1) {
						impossible = true;
					} else if (arr[j1+1][j2] == 1 && arr[j1][j2+1] == 1 && arr[j1+1][j2+1] == 1) {
						arr[j1][j2] = arr[j1][j2+1] = 2;
						arr[j1+1][j2] = arr[j1+1][j2+1] = 3;
					} else {
						impossible = true;
					}
				}
			}
			if (impossible) {
				break;
			}
		}
		if (impossible) {
			f_out << "Impossible" << endl;
		} else {
			for (int j1 = 0; j1 < R; ++j1) {
				for (int j2 = 0; j2 < C; ++j2) {
					if (arr[j1][j2] == 0) {
						f_out << ".";
					} else if (arr[j1][j2] == 2) {
						f_out << '/' << "\\";
						++j2;
					} else if (arr[j1][j2] == 3) {
						f_out << "\\/";
						++j2;
					}
				}
				f_out << endl;
			}
		}
	}
	return 0;
}

