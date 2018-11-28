#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

void printBoard(int N, char b[][50]) {
	for (int r=0; r<N; r++) {
		for (int c=0; c<N; c++) {
			//cout << ((b[r][c]!=0) ? b[r][c] : '.');
		}
		//cout << endl;
	}
}

char gV(int r, int c, int N, char b[][50]) {
	if ((r < 0) || (c < 0) || (r >= N) || (c >= N)) {
		return 0;
	}else{
		return b[r][c];
	}
}

bool checkPos(int size, int p, int r, int c, int rd, int cd, int N, char b[][50]) {
	if (size <= 0) return true;
	bool r1 = (gV(r,c,N,b) == p);
	bool r2 = (checkPos(size-1,p,r+rd,c+cd,rd,cd,N,b));
	return (r1 && r2);
}

void searchBoard(int N, int K, int caseN, char b[][50]) {
	cout << "Case #"<<caseN<<": ";

	bool redWin=false, blueWin=false;

	// (rd,cd)
	// down (1,0) right (0,1) down left (1,-1) down right (1,1)

	for (int r=N-1; r>=0 && ((!redWin) || (!blueWin)); r--) {
		for (int c=0; c<N && ((!redWin) || (!blueWin)); c++) {

			//cout << endl << r << '\t' << c << endl;

			char curVal = gV(r,c,N,b);
			if ((curVal != 0) && (curVal != '.')
				&& (
					((curVal == 'R') && (!redWin))
					|| ((curVal == 'B') && (!blueWin))
				) ) {

				bool win = false;
				if (checkPos(K,curVal,r,c,1,0,N,b)) {
					//cout << "D  AT " << r << "\t" << c;
					win = true;
				}else if (checkPos(K,curVal,r,c,0,1,N,b)) {
					//cout << "R  AT " << r << "\t" << c;
					win = true;
				}else if (checkPos(K,curVal,r,c,1,-1,N,b)) {
					//cout << "DL AT " << r << "\t" << c;
					win = true;
				}else if (checkPos(K,curVal,r,c,1,1,N,b)) {
					//cout << "DR AT " << r << "\t" << c;
					win = true;
				}

				if (win) {
					if (curVal == 'R') {
						//cout << "(red)";
						redWin = true;
					}else if (curVal == 'B') {
						//cout << "(blue)";
						blueWin = true;
					}else{
						cerr << "FAILED BAD SQ" << curVal;
					}
					//cout << endl;
				}
			}
		}

	}

	if (redWin && blueWin) {
		cout << "Both";
	}else if (redWin) {
		cout << "Red";
	}else if (blueWin) {
		cout << "Blue";
	}else{
		cout << "Neither";
	}

	cout << endl;
}

int main(int argc, char** argv) {
	int T=0;
	cin >> T;

	for (int caseN=1; caseN<=T; caseN++) {
		int K=0, N=0;
		char board[50][50] = {{0}};
		char boardr[50][50] = {{0}};
		int roffset[50] = {0};

		// read board

		cin >> N >> K;
		//cout << N << K << endl;


		string blah;
		//getline(cin,blah);

		for (int ln=0; ln < N; ln++) {
			//string line;
			//getline(cin,board[ln]);
			cin >> board[ln];
			//cout << board[ln] << endl;
		}

		// rotate + gravity
		for (int row=N-1; row>=0; row--) { // rotated row (i.e. orig col)
			// check each cell if nonblank
			for (int col=0; col<=N; col++) {
				if ((board[col][row] != 0) && (board[col][row] != '.')) {
					// insert into new board
					boardr[N-(1+roffset[col])][N-(1+col)] = board[col][row];
					roffset[col]++;
				}
			}
		}

		//printBoard(N,boardr);
		searchBoard(N, K, caseN, boardr);

	}

	return 0;
}
