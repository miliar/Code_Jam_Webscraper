#include <iostream>
#include <cstdio>

using namespace std;

#define N 4

int T;
char board[N][N];

bool check(char c) {
	//check rows
	for (int i = 0; i < N; i++) {
		int Ts = 0, cs = 0;
		for (int j = 0; j < N; j++) {
			Ts += (board[i][j]=='T');
			cs += (board[i][j]==c);
		}
		if (cs+Ts == N) return 1;
	}
	//check columns
	for (int i = 0; i < N; i++) {
        int Ts = 0, cs = 0;
        for (int j = 0; j < N; j++) {
            Ts += (board[j][i]=='T');
            cs += (board[j][i]==c);
        }
        if (cs+Ts == N) return 1;
    }
	//check diags
	int Ts = 0, cs = 0, Ts2 = 0, cs2 = 0;
	for (int i = 0; i < N; i++) {
		Ts += (board[i][i]=='T');
		cs += (board[i][i]==c);
		Ts2 += (board[i][N-i-1]=='T');
		cs2 += (board[i][N-i-1]==c);
	}
	if (Ts+cs == N || Ts2+cs2 == N) return 1;
	return 0;
}

int main()
{
	freopen("tictac.out", "w", stdout);
	freopen("tictac.in", "r", stdin);
	
	cin >> T;
	
	for (int i = 0; i < T; i++) {
		for (int j = 0; j < N; j++) 
			for (int k = 0; k < N; k++) 
				cin >> board[j][k];
		printf("Case #%d: ", i+1);
		if (check('X')) printf("X won\n");
		else if (check('O')) printf("O won\n");
		else {
			bool draw = 1;
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < N; k++) {
					if (board[j][k] == '.') {
						draw = 0;
						break;
					}
				}
			}
			if (draw) printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}
}
