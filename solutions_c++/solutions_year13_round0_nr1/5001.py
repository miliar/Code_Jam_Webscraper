#include <iostream>
#include <fstream>

using namespace std;

int T;
char board[4][4];
bool end;
int xt, yt;

bool won(char c) {
     if (xt != -1) board[yt][xt] = c;
     bool k;
     for (int i = 0; i<=3; i++) {
            k = 1;
            for (int j = 0; j<=3; j++) {
                if (board[i][j] != c) {
                   k = 0;
                   break;
                }
            }
            if (k == 1) return 1;
     }
     for (int i = 0; i<=3; i++) {
            k = 1;
            for (int j = 0; j<=3; j++) {
                if (board[j][i] != c) {
                   k = 0;
                   break;
                }
            }
            if (k == 1) return 1;
     }
     k = 1;
     for (int i = 0; i<=3; i++) {
         if ( board[i][i] != c) k = 0;
     }
     if (k) return 1;
     k = 1;
     for (int i = 0; i<=3; i++) {
         if ( board[i][3-i] != c) k = 0;
     }
     if (k) return 1;
     return 0;
}

int main(){
	ifstream in ("A.in");
	ofstream out ("A.out");
	in >> T;
	for (int t = 1; t<=T; t++) {
        xt = -1;
		for (int y = 0; y<=3; y++) {
			in >> board[y];
		}
		end = 1;
		for (int y = 0; y<=3; y++) {
			for (int x = 0; x<=3; x++) {
				if (board[y][x] == '.') {
                     end = 0;
                }
                if (board[y][x] == 'T') {
                     xt = x;
                     yt = y;           
                }
			}
		}
		out << "Case #" << t << ": ";
		if (won('X')) out << "X won\n";
		else if (won('O')) out << "O won\n";
		else if (end) out << "Draw\n";
		else out << "Game has not completed\n";
		
		
		
	}
	return 0;
}
