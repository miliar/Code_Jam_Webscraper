#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <fstream>

using namespace std;

void fill(int* row, string s) {
	for (unsigned int i = 0; i < s.length(); i++) {
		unsigned char c = s.at(i);
		if (c >= 'A') c -= 55;
		else c -= 48;
		unsigned int mask = 1;
		for (int j = 0; j < 4; j++) {
			row[i*4 + 3 - j] = mask & c;
			c = c >> 1;			
		}
	}
}

unsigned int calc(int** b, int N, int M, int search, int* bSol, int** fb) {
	bool stop = false;
	if (search == 0) return 0;
	int found = 0;
	for (int i = 0; i + search <= M; i++) {
		for (int j = 0; j + search <= N; j++) {
			for (int ii = 0; ii < search - 1 && stop == false; ii++) {
				for (int jj = 0; jj < search - 1; jj++) {
					if (b[i + ii][j + jj] == 0) { stop = true; break; }
				}
			}

			if (stop == false) {
				for (int ii = 0; ii < search; ii++) {
					for (int jj = 0; jj < search; jj++) {
						b[i + ii][j + jj] = 0;
						fb[i + ii][j + jj] = -1;
					}
				}
			
				if (i != 0 || j != 0)
				for (int ii = 1; ii < search + 1; ii++) {
					if (j != 0)
						b[i-1 + ii][j - 1] = 0;
					if (i != 0)
						b[i-1][j - 1 + ii] = 0;
					if (i != 0 && j != 0) b[i-1][j-1] = 0;
				}

				found++;
				bSol[search]++;

			}
			stop = false;
		}		
	}
	if (found != 0) return 1 + calc(b, N, M, search - 1, bSol, fb);
	else return calc(b, N, M, search - 1, bSol, fb);
}

void printMatrix(int** m, int M, int N) {
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++)
			cout << m[i][j];
		cout << endl;
	}
}

int main()
{
	ofstream myFile;
	myFile.open ("out.out");
	ifstream input("C-large.in");

	int turns;
	input >> turns;

	for (int t = 1; t <= turns; t++) {
	int M, N;
	input >> M >> N;

	int** board;
	board = new int*[M];
	for (int i = 0; i < M; i++) board[i] = new int[N];

	string s;
	for (int i = 0; i < M; i++) {
		input >> s;
		while (s.length() < N/4) s = "0" + s;
		fill(board[i], s);
	}

	//

	// test matrix
	int** fBoard;
	fBoard = new int*[M];
	for (int i = 0; i < M; i++) fBoard[i] = new int[N];

	for (int i = 0; i < M - 1; i++) {
		for (int j = 0; j < N - 1; j++) {
			if (board[i+1][j] != board[i][j] && board[i][j+1] != board[i][j] && board[i][j] == board[i+1][j+1]) fBoard[i][j] = 1;
			else fBoard[i][j] = 0;
		}
	}

	//

	int sol;

	int* bSol = new int [513];
	int* tSol = new int [513];

	for (int i = 0; i < 513; i++) bSol[i] = tSol[i] = 0;

	if (N < M)
		sol = calc(fBoard, N, M, N, bSol, board);
	else 
		sol = calc(fBoard, N, M, M, bSol, board);

	
	int total = 0;
	cout << sol << endl;
	
	for (int i = 512; i > 1; i--) {
		if (bSol[i] != 0)  {
			
			//myFile << i << ' ' << bSol[i] << endl;
			total += i * i * bSol[i];
		}
	}

	if (M * N - total == 0 && bSol[1] != 0) sol--;

	myFile << "Case #" << t << ": " << sol << endl;

	for (int i = 512; i > 1; i--) {
		if (bSol[i] != 0)  {
			
			myFile << i << ' ' << bSol[i] << endl;
		}
	}

	if (M * N - total != 0)
		myFile << 1 << ' ' << M * N - total << endl;
	}
}