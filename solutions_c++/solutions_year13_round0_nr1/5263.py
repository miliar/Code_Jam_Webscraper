#include <cstdio>

int z;
char t[5][5];
int whoWon;
bool dot;

int main() {
	scanf("%d", &z);
	for(int casen = 1; casen <= z; casen ++) {
		whoWon = 0;
		dot = false;
		for(int row = 0; row < 4; row++)
			scanf("%s", t[row]);
		for(int i = 0; i < 4 && (whoWon == 0); i++) {
			bool x = true, o = true;
			for(int j = 0; j < 4; j++) {
				if(t[i][j] == '.') { dot = true; x = o = false; }
				if(t[i][j] == 'O') x = false;
				if(t[i][j] == 'X') o = false;
			}
			if(x) whoWon = 1;
			if(o) whoWon = 2;
		}
		for(int i = 0; i < 4 && (whoWon == 0); i++) {
			bool x = true, o = true;
			for(int j = 0; j < 4; j++) {
				if(t[j][i] == '.') { dot = true; x = o = false; }
				if(t[j][i] == 'O') x = false;
				if(t[j][i] == 'X') o = false;
			}
			if(x) whoWon = 1;
			if(o) whoWon = 2;
		}
		if((t[0][0] == 'O' || t[0][0] == 'T') && (t[1][1] == 'O' || t[1][1] == 'T') && (t[2][2] == 'O' || t[2][2] == 'T') && (t[3][3] == 'O' || t[3][3] == 'T') ) whoWon = 2;
		if((t[0][0] == 'X' || t[0][0] == 'T') && (t[1][1] == 'X' || t[1][1] == 'T') && (t[2][2] == 'X' || t[2][2] == 'T') && (t[3][3] == 'X' || t[3][3] == 'T') ) whoWon = 1;
		if((t[3][0] == 'O' || t[3][0] == 'T') && (t[2][1] == 'O' || t[2][1] == 'T') && (t[1][2] == 'O' || t[1][2] == 'T') && (t[0][3] == 'O' || t[0][3] == 'T') ) whoWon = 2;
		if((t[3][0] == 'X' || t[3][0] == 'T') && (t[2][1] == 'X' || t[2][1] == 'T') && (t[1][2] == 'X' || t[1][2] == 'T') && (t[0][3] == 'X' || t[0][3] == 'T') ) whoWon = 1;
		printf("Case #%d: ", casen);
		if(whoWon == 1) printf("X won\n");
		if(whoWon == 2) printf("O won\n");
		if(whoWon == 0) {
			if(!dot) printf("Draw\n");
			else printf("Game has not completed\n");
		}
	}
}
