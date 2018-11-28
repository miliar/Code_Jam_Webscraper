#include <string>
#include <cstring>
#include <iostream>
#include <fstream>

using namespace std;

#define N 4

int tc;
string board[N];

int solve()
{
	int oh[N], ov[N], xh[N], xv[N];
	int d1x = 0, d2x = 0, d1o = 0, d2o = 0;

	memset(oh, 0, sizeof(oh));
	memset(ov, 0, sizeof(ov));
	memset(xh, 0, sizeof(xh));
	memset(xv, 0, sizeof(xv));

	bool empty = false;

	for (int i=0; i<N; i++) {
		for (int j=0; j<N; j++) {
			switch (board[i][j]) {
				case 'O':
					oh[i]++;
					ov[j]++;

					if (i == j) d1o++;
					if (i + j == N-1) d2o++;
					break;

				case 'X':
					xh[i]++;
					xv[j]++;
					if (i == j) d1x++;
					if (i + j == N-1) d2x++;
					break;

				case 'T':
					oh[i]++; ov[j]++;
					xh[i]++; xv[j]++;
					if (i == j) {
						d1o++; d1x++;
					}
					if (i + j == N-1) {
						d2o++; d2x++;
					}
					break;
				case '.':
					empty = true;
					break;
			}
		}
	}

	for (int i=0; i<N; i++) {
		if (xh[i] == N) return 0;
		if (xv[i] == N) return 0;
		if (oh[i] == N) return 1;
		if (ov[i] == N) return 1;
	}
	if (d1x == N || d2x == N) return 0;
	if (d1o == N || d2o == N) return 1;

	return (empty ? 3 : 2);
}

int main()
{
	ifstream fin("tictactoe.txt");
	ofstream fout("tictactoe.out");

	string tmp;
	fin >> tc;

	for (int test=1; test<=tc; test++) {
		// end of the line or empty line
		getline(fin, tmp);

		// reading input matrix
		for (int i=0; i<N; i++)
			getline(fin, board[i]);
		
		int res = solve();
		string result;

		switch (res) {
		case 0:
			result = "X won";
			break;

		case 1:
			result = "O won";
			break;

		case 2:
			result = "Draw";
			break;

		case 3:
			result = "Game has not completed";
			break;
		}

		// output
		fout << "Case #" << test << ": " << result << endl;
	}

	return 0;
}