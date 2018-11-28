#include <cstdio>
#include <iostream>
using namespace std;

int T;
char board[10][10];
char tmp[100];
int dx[4] = {+0 , +1 , +1 , +1};
int dy[4] = {+1 , +1 , +0 , -1};
FILE *fin  = fopen("A-small.in" , "r");
FILE *fout = fopen("A-small.out" , "w");

bool check(int i , int j , char v){
	int r , c;
	for(int k = 0 ; k < 4 ; k++){
		 int seen = 0;
		 r = i , c = j;
		 for(int h = 0 ; h < 3 ; h++){
			r += dx[k];
			c += dy[k];
			if(r < 0 || r >= 4 || c < 0 || c >= 4 || ((board[r][c] != v) && (board[r][c] != 'T')))
					break;
			seen++;
		 }
		 if(seen == 3){
				if(v == 'X')
					fprintf(fout , "X won\n");
				else if(v == 'O')
					fprintf(fout , "O won\n");
				return true;
		 }
	}
	return false;
}
void solve(){
	bool complete = true;
	for(int i = 0 ; i < 4 ; i++){
		for(int j = 0 ; j < 4 ; j++){
			int r = i , c = j;
			if(board[i][j] == '.'){
				complete = false;
				continue;
			}
			bool pass;
		    if(board[i][j] == 'X')
				pass = check(i , j , 'X');
			else if(board[i][j] == 'O')
				pass = check(i , j , 'O');
			else if(board[i][j] == 'T')
				pass = check(i , j , 'X') || check(i , j , 'O');
			if(pass)
				return;
		}
	}
	if(complete)
		fprintf(fout , "Draw\n");
	else
		fprintf(fout , "Game has not completed\n");
	return;
}
int main(){
	fscanf(fin , "%d" , &T);
	for(int t = 1 ; t <= T ; t++){
		for(int i = 0 ; i < 4 ; i++)
			fscanf(fin , "%s" , board[i]);
		fprintf(fout , "Case #%d: " , t);
		solve();
	}
	return 0;
}