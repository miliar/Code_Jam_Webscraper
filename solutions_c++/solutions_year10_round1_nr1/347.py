#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
using namespace std;

bool findLine(vector<string> &board, char ch, int K)
{
	int M = board.size();
	if (M == 0) return false;

	int N = board[0].length();

	//cout << ch << ' ' << K << endl;

	int i, j, k;
	for (i=0; i<M; ++i) for (j=0; j<N; ++j) if (board[i][j] == ch) {
		//right
		for (k=0; k<K; ++k) {
			int i1 = i;
			int j1 = j+k;
			if (j1 >= N) break;
			if (board[i1][j1] != ch) break;
		}
		if (k == K) {
			//cout << i << ' ' << j << ' ' << 1 << endl;
			return true;
		}

		//down
		for (k=0; k<K; ++k) {
			int i1 = i+k;
			int j1 = j;
			if (i1 >= M) break;
			if (board[i1][j1] != ch) break;
		}
		if (k == K) {
			//cout << i << ' ' << j << ' ' << 2 << endl;
			return true;
		}

		//down left
		for (k=0; k<K; ++k) {
			int i1 = i+k;
			int j1 = j-k;
			if (i1 >= M) break;
			if (j1 < 0) break;
			if (board[i1][j1] != ch) break;
		}
		if (k == K) {
			//cout << i << ' ' << j << ' ' << 3 << endl;
			return true;
		}

		//down right
		for (k=0; k<K; ++k) {
			int i1 = i+k;
			int j1 = j+k;
			if (i1 >= M) break;
			if (j1 >= N) break;
			if (board[i1][j1] != ch) break;
		}
		if (k == K) {
			//cout << i << ' ' << j << ' ' << 4 << endl;
			return true;
		}
	}

	return false;
}

string calc()
{
	stringstream S;
	int i, j, k;

	int N, K;
	cin >> N >> K;

	vector<string> ori(N);
	for (i=0; i<N; ++i) {
		cin >> ori[i];
	}

	int M = ori[0].length();

	//cout << "N/M: " << N << ' ' << M << endl;

	//for (i=0; i<M; ++i) cout << ori[i] << endl;
	//cout << endl;

	vector<string> board(M, string(N, 'a'));

	//rotate
	for (i=0; i<N; ++i) for (j=0; j<M; ++j) {
		board[j][M-i-1] = ori[i][j];
	}

	//for (i=0; i<M; ++i) cout << board[i] << endl;
	//cout << endl;

	//gravity
	//board M*N;
	for (i=0; i<N; ++i) {
		j = M-1;
		k = M-1;
		while (k >= 0) {
			if (board[k][i] != '.') {
				board[j][i] = board[k][i];
				j--;
			}

			k--;
		}

		while (j >= 0) {
			board[j][i] = '.';
			j--;
		}
	}

	//for (i=0; i<M; ++i) cout << board[i] << endl;

	bool red = findLine(board, 'R', K);
	bool blue = findLine(board, 'B', K);

	if (red && blue) {
		S << "Both";
	} else if (red) {
		S << "Red";
	} else if (blue) {
		S << "Blue";
	} else {
		S << "Neither";
	}

	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

