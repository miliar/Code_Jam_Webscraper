// jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "windows.h"
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	unsigned int T;
	cin >> T;
	for ( int i = 0; i < T; ++i) {
		unsigned int R, C;
		cin >> R;
		cin >> C;
		unsigned int mat[50][50];
		for (int j = 0; j < R; j++) {
			for(int k = 0; k < C; ++k) {
				char ch;
				cin >> ch;
				mat[j][k] = (ch == '.')? 0:1;
			}
		}
		bool possible = true;
		for (int j = 0; j < R; ++j) {
			for (int k= 0; k < C; ++k) {
				
				if (mat[j][k] != 1)
					continue;

				if (k == C-1) {
					possible = false;
					break;
				}

				if (j == R-1) {
					possible = false;
					break;
				}
				
				if (mat[j][k+1] != 1) {
					possible = false;
					break;
				}
				
				if (mat[j+1][k] != 1) {
					possible = false;
					break;	
				}

				if (mat[j+1][k+1] != 1) {
					possible = false;
					break;
				}

				mat[j][k] = 10;
				mat[j+1][k+1] = 10;
				mat[j][k+1] = 20;
				mat[j+1][k] = 20;

			}
			if (!possible) break;
		}
			
		cout << "Case #" << i+1 << ":" << endl;
		if (!possible) 
			cout << "Impossible" << endl;
		else {
			for (int j = 0; j < R; ++j) {
				for (int k = 0; k < C; ++k) {
					
					if (mat[j][k] == 0)
						cout << '.';
					else if (mat[j][k] == 10)
						cout << '/';
					else if (mat[j][k] == 20)
						cout << '\\';
					else
						cout << "illegal";

				}
				if (C != 1)
					cout << endl;
			}
			cout << endl;
		}

		}
	
	
	return 0;
}

