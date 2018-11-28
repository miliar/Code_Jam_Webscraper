#include <iostream>

#include <string>
#include <fstream>

using namespace std;

#define EMPTY 1
#define RED 2
#define BLUE 3

int n, k;

int board[50][50];

void zero() {
	memset(board, 0, sizeof(board));
}

int isWin(int x, int y) {
	int i = 0;
	int player = board[x][y];
	
	if(player == EMPTY) return 0;
	
	int tx = x, ty = y;
	while(tx>0) {
		if(board[tx][y] == player) ++i;
		else break;
		tx--;
	}
	if(i >= k) return player;
	
	tx=x; i = 0;
	while(tx < n) {
		if(board[tx][y] == player) ++i;
		else break;
		tx++;
	}
	if(i>=k) return player;
	
	tx=x; i=0;
	while(ty>0) {
		if(board[x][ty] == player) ++i;
		else break;
		ty--;
	}
	if(i>=k) return player;
	
	ty=y; i=0;
	while(ty<n) {
		if(board[x][ty] == player) ++i;
		else break;
		ty++;
	}
	if(i>=k) return player;
	
	tx=x; ty=y; i=0;
	while(tx>0&&ty>0) {
		if(board[tx][ty] == player) ++i;
		else break;
		
		tx--;
		ty--;
	}
	if(i>=k) return player;
	
	tx=x; ty=y; i=0;
	while(tx<n&&ty<n) {
		if(board[tx][ty] == player) ++i;
		else break;
		
		tx++;
		ty++;
	}
	if(i>=k) return player;
	
	tx=x; ty=y; i=0;
	while(tx>0&&ty<n) {
		if(board[tx][ty] == player) ++i;
		else break;
		
		tx--;
		ty++;
	}
	if(i>=k) return player;
	
	tx=x; ty=y; i=0;
	while(tx<n&&ty>0) {
		if(board[tx][ty] == player) ++i;
		else break;
		
		tx++;
		ty--;
	}
	if(i>=k) return player;
	
	return 0;
}

void rotate() {
	int newboard[50][50];
	
	memset(newboard, 0, sizeof(newboard));
	
	for(int i=0; i<n; ++i) {
		for(int j=0; j<n; ++j) {
			newboard[i][j] = board[n-j-1][i];
		}
	}
	
	memcpy(board, newboard, sizeof(board));
}

void gravity() {
	for(int i=n-1; i>=0; --i) {
		for(int j=0; j<n; ++j) {
			if(board[i][j] != EMPTY) {
				int tmp = i+1;
				while(board[tmp][j] == EMPTY) {
					++tmp;
					if(tmp >= n) break;
				}
				
				if(tmp - 1 != i) {
					board[tmp-1][j] = board[i][j];
					board[i][j] = EMPTY;
				}
			}
		}
	}
}

void printMatrix() {
	for(int i=0; i<n; ++i) {
		for(int j=0; j<n; ++j) {
			if(board[i][j] == EMPTY) cout<<'.';
			if(board[i][j] == RED) cout<<'R';
			if(board[i][j] == BLUE) cout<<'B';
		}
		cout<<endl;
	}
}

int main() {
	int t;
	ifstream in("A-large.in");
	ofstream out1("1.out");
	
	in>>t;
	
	for(int i=0; i<t; ++i) {
		in>>n>>k;

		zero();
		
		for(int j=0; j<n; ++j) {
			for(int k=0; k<n; ++k) {
				char tc;
				
				in>>tc;
				if(tc == '.') board[j][k] = EMPTY;
				else if(tc == 'R') board[j][k] = RED;
				else if(tc == 'B') board[j][k] = BLUE;
			}
		}
		
		rotate();
		gravity();
		
		printMatrix();
				
		int a=0;
		int b=0;
		int c=0;
		for(int j=0; j<n; ++j) {
			for(int k=0; k<n; ++k) {
				if(board[j][k] != EMPTY) {
					if(a != 0 && board[j][k] == a) continue;
					
					a = isWin(j, k);
					if(a == RED) b=1;
					else if(a == BLUE) c=1;
					
					if(b==1 && c==1) break;
				}
			}
			if(b==1 && c==1) break;
		}
		
		string result;
		if(b==0 && c==0) result = "Neither";
		else if(b==1 && c==0) result = "Red";
		else if(b==0 && c==1) result = "Blue";
		else if(b==1 && c==1) result = "Both";
		out1<<"Case #"<<i+1<<": "<<result<<endl;
	}
	in.close();
	out1.close();
}
