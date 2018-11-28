#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <fstream>
#include <math.h>
#include <algorithm> 
#include <vector>
#include <string> 

using namespace std;

long m, n; 

void setB(int** board, char c, int i, int j) {
	switch(c) {
		case '0': board[i][j*4] = 0; board[i][j*4+1] = 0; board[i][j*4+2] = 0; board[i][j*4+3] = 0; break;
		case '1': board[i][j*4] = 0; board[i][j*4+1] = 0; board[i][j*4+2] = 0; board[i][j*4+3] = 1; break;
		case '2': board[i][j*4] = 0; board[i][j*4+1] = 0; board[i][j*4+2] = 1; board[i][j*4+3] = 0; break;
		case '3': board[i][j*4] = 0; board[i][j*4+1] = 0; board[i][j*4+2] = 1; board[i][j*4+3] = 1; break;
		case '4': board[i][j*4] = 0; board[i][j*4+1] = 1; board[i][j*4+2] = 0; board[i][j*4+3] = 0; break;
		case '5': board[i][j*4] = 0; board[i][j*4+1] = 1; board[i][j*4+2] = 0; board[i][j*4+3] = 1; break;
		case '6': board[i][j*4] = 0; board[i][j*4+1] = 1; board[i][j*4+2] = 1; board[i][j*4+3] = 0; break;
		case '7': board[i][j*4] = 0; board[i][j*4+1] = 1; board[i][j*4+2] = 1; board[i][j*4+3] = 1; break;
		case '8': board[i][j*4] = 1; board[i][j*4+1] = 0; board[i][j*4+2] = 0; board[i][j*4+3] = 0; break;
		case '9': board[i][j*4] = 1; board[i][j*4+1] = 0; board[i][j*4+2] = 0; board[i][j*4+3] = 1; break;
		case 'A': board[i][j*4] = 1; board[i][j*4+1] = 0; board[i][j*4+2] = 1; board[i][j*4+3] = 0; break;
		case 'B': board[i][j*4] = 1; board[i][j*4+1] = 0; board[i][j*4+2] = 1; board[i][j*4+3] = 1; break;
		case 'C': board[i][j*4] = 1; board[i][j*4+1] = 1; board[i][j*4+2] = 0; board[i][j*4+3] = 0; break;
		case 'D': board[i][j*4] = 1; board[i][j*4+1] = 1; board[i][j*4+2] = 0; board[i][j*4+3] = 1; break;
		case 'E': board[i][j*4] = 1; board[i][j*4+1] = 1; board[i][j*4+2] = 1; board[i][j*4+3] = 0; break;
		case 'F': board[i][j*4] = 1; board[i][j*4+1] = 1; board[i][j*4+2] = 1; board[i][j*4+3] = 1; break;
	}
}

bool check(int** board, int s, int i, int j) {
	for (int p=i; p<i+s; p++) {
		for (int q=j; q<j+s; q++) {
			if (board[p][q] == -1)
				return false;
		}
	}
	for (int p=i; p<i+s-1; p++) {
		if (board[p][j] == board[p+1][j])
			return false;
	}
	for (int p=i; p<i+s; p++) {
		for (int q=j; q<j+s-1; q++) {
			if (board[p][q] == board[p][q+1])
				return false;
		}
	}

	for (int p=i; p<i+s; p++) {
		for (int q=j; q<j+s; q++) {
			board[p][q] = -1;
		}
	}
	return true;
}

int searchB(int** board, int s) {
	int res = 0;
	for (int i=0; i<m-s+1; i++) {
		for (int j=0; j<n-s+1; j++) {
			if (board[i][j] != -1 && check(board, s, i, j))
				res++;
		}
	}
	return res;
}

void main() {
	ifstream fin("C.in");
	ofstream fout("C.out");

	long T; fin >> T;
	for (long l=0; l<T; l++) {
		fin >> m >> n; fin.ignore();
		int** board = new int*[m];
		for (int i=0; i<m; i++) {
			board[i] = new int[n];
		}

		char c[130];
		for (int i=0; i<m; i++) {
			fin.getline(c, 150);
			for (int j=0; j<n/4; j++) {
				setB(board, c[j], i, j);
			}
		}

		long ans = 0;
		long res[513] = {0}; 

		for (int i=min(m, n); i>0; i--) {
			res[i] = searchB(board, i);
			if (res[i] != 0) {
				ans++;
			}
		}

		fout << "Case #" << (l+1) << ": ";
		fout << ans << endl;
		for (int i=min(m, n); i>0; i--) {
			if (res[i] != 0)
				fout << i << ' ' << res[i] << endl;
		}
	}

	fin.close(); fout.close();
}