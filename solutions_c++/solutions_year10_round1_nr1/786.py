#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <fstream>
#include <math.h>
#include <algorithm> 
#include <vector>
#include <string>

using namespace std;

bool check1(int rotate[][50], int k, int color, int x, int y) {
	for (int i=0; i<k; i++)
		if (rotate[x][y+i] != color)
			return false;
	return true;
}

bool check2(int rotate[][50], int k, int color, int x, int y) {
	for (int i=0; i<k; i++)
		if (rotate[x+i][y] != color)
			return false;
	return true;
}

bool check3(int rotate[][50], int k, int color, int x, int y) {
	for (int i=0; i<k; i++)
		if (rotate[x+i][y-i] != color)
			return false;
	return true;
}

bool check4(int rotate[][50], int k, int color, int x, int y) {
	for (int i=0; i<k; i++)
		if (rotate[x+i][y+i] != color)
			return false;
	return true;
}

bool check(int rotate[][50], int n, int k, int color) {
	for (int i=0; i<n; i++) {
		for (int j=0; j<n; j++) {
			if (i<n-k+1) {
				if (check2(rotate, k, color, i, j))
					return true;
				if (j>k-2 &&
					check3(rotate, k, color, i, j) )
					return true;
				if (j<n-k+1 &&
					check4(rotate, k, color, i, j) )
					return true;
			}
			if (j<n-k+1 &&
				check1(rotate, k, color, i, j) ) {
					return true;
			}
		}
	}
	return false;
}

void main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");

	long T; fin >> T;
	for (long l=0; l<T; l++) {
		int n, k;
		fin >> n >> k;
		int board[50][50];
		char ch;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				fin >> ch;
				if (ch == '.')
					board[i][j] = 0;
				else if (ch == 'R')
					board[i][j] = 1;
				else if (ch == 'B')
					board[i][j] = 2;
			}
		}

		int rotate[50][50];
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				rotate[i][j] = 0;

		for (int i=n-1; i>=0; i--) {
			int k = n-1;
			for (int j=n-1; j>=0; j--) {
				if (board[i][j] != 0) {
					rotate[k][n-1-i] = board[i][j];
					k--;
				}
			}
		}

		bool res1 = check(rotate, n, k, 1);
		bool res2 = check(rotate, n, k, 2);

		fout << "Case #" << (l+1) << ": ";
		if (res1 && res2) 
			fout << "Both\n";
		else if (res1)
			fout << "Red\n";
		else if (res2)
			fout << "Blue\n";
		else
			fout << "Neither\n";
		fout << endl;
	}

	fin.close(); fout.close();
}