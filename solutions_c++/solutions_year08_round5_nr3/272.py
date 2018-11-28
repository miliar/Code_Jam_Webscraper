#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int M, N, best;
char board[90][90];

void count(int i, int j, int current) {
	int predict = (N-j + 1) / 2 * M;
	if((N-j)%2==1) predict -= i;
	if(current + predict <= best)
		return;
	if(j >= N) {
		if(current > best)
			best = current;
		return;
	}
	int i1 = i+1, j1 = j;
	if(i1 >= M) {
		i1 = 0;
		j1 = j+1;
	}

	if(board[i][j] == 'x') {
		count(i1, j1, current);
		return;
	}

	if(j==0 || board[i][j-1] != 'O' && (i==M-1 || board[i+1][j-1] != 'O') && (i==0 || board[i-1][j-1] != 'O')) {
		board[i][j] = 'O';
		count(i1, j1, current + 1);
		board[i][j] = '.';

		count(i1, j1, current);
	}
	else {
		count(i1, j1, current);
	}
}

int main(int argc, char* argv[]) {
	int n;
	cin >>n;
	for(int i=0; i<n; i++) {
		cin >>M >>N;
		for(int j=0; j<M; j++)
			cin >>board[j];
		best = 0;
		count(0, 0, 0);
		cout <<"Case #" <<i+1 <<": " <<best <<endl;
		cerr <<i+1 <<endl;
	}
}

/*
d:\Documents\Visual Studio 2008\Projects\GoogleCodeJam\Debug\
*/