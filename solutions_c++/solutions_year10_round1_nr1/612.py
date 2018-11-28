/*
 * Google Code Jam 2010. Round 1 - sub-round A
 * (C)Copyright jclin (j i a n c h e n g [at] g_m_a_i_l [dot] c_o_m)
 */
#include <iostream>
#include <cstring>
#include <cstdlib>

using namespace std;

#define FOR(i,N)	for(int i=0;i<N;++i)

struct cell {
	char	c;	// color
	int		col, row, r2l, l2r;
};

static cell board[50][50];

const char * game()
{
	int N,K;
	char line[4096];
	
	int max_b, max_r;
	
	cin >> N >> K;
	
	max_b = max_r = 0;
	
	memset(board,0,sizeof(board));
	FOR(i,N) {
		cin >> line;
		int idx = N-1;
		for(int j=N-1; j>=0; j--) {
			if(line[j] != '.') {
				board[idx][i].c = line[j];
				idx--;
			}
		}
	}
	FOR(i,N) {
		FOR(j,N) {
			if(board[i][j].c != 0) {
				board[i][j].row = 1;
				board[i][j].col = 1;
				board[i][j].l2r = 1;
				board[i][j].r2l = 1;
				if(i>0) {
					if(board[i][j].c == board[i-1][j].c)
						board[i][j].col += board[i-1][j].col;
				}
				if(j>0) {
					if(board[i][j].c == board[i][j-1].c)
						board[i][j].row += board[i][j-1].row;
				}
				if(i>0 && j>0) {
					if(board[i][j].c == board[i-1][j-1].c)
						board[i][j].l2r += board[i-1][j-1].l2r;
				}
				if(board[i][j].c == board[i-1][j+1].c)
					board[i][j].r2l += board[i-1][j+1].r2l;
			}
#if 0
			cout << board[i][j].c << '[' << board[i][j].row << ',' << board[i][j].col
			<< ',' << board[i][j].l2r << ',' << board[i][j].r2l << ']';
#endif		
			int * c_ptr = board[i][j].c == 'R' ? &max_r : &max_b;
			if(board[i][j].row > *c_ptr)
				*c_ptr = board[i][j].row;
			if(board[i][j].col > *c_ptr)
				*c_ptr = board[i][j].col;
			if(board[i][j].l2r > *c_ptr)
				*c_ptr = board[i][j].l2r;
			if(board[i][j].r2l > *c_ptr)
				*c_ptr = board[i][j].r2l;
		}
		//cout << endl;
	}
	
	if(max_r >= K && max_b >= K)
		return "Both";
	else if(max_r >= K)
		return "Red";
	else if(max_b >= K)
		return "Blue";
	return "Neither";
}

int main(int ac, char**av)
{
	int T;

	cin >> T;
	FOR(i,T) {
		cout << "Case #" << i+1 << ": " << game() << endl;
	}
	return 0;
}

