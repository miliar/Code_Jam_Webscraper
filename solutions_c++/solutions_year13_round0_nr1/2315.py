#include <stdio.h>
#include <string.h>

bool check(char c, int tx, int ty, char board[4][4]) {
	int r1, r2, r3, t1, t2, t3, t4;
	if(tx != -1 && ty != -1) {
		board[tx][ty] = c;
	}
	t3 = t4 = 0;
	for(r1=0; r1<4; r1++) {
		t1 = t2 = 0;
		for(r2=0; r2<4; r2++) {
			if(board[r1][r2] == c) {
				t1++;
			}
			if(board[r2][r1] == c) {
				t2++;
			}
		}
		if(t1 == 4 || t2 == 4) {
			return true;
		} 
		if(board[r1][r1] == c) {
			t3++;
		}
		if(board[r1][3-r1] == c) {
			t4++;
		}
	}
	if(t3 == 4 || t4 == 4) {
		return true;
	} else {
		return false;
	}
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, tx, ty;
	int r1, r2, r3, r4, t1, t2, t3, t4, cs;
	char board[4][4];
	char c;
	bool draw;
	scanf("%d", &t);
	for(int cs=1; cs<=t; cs++) {
		draw = true;
		memset(board, 0, sizeof(board));
		tx = ty = -1;
		for(r1=0; r1<4; r1++) {
			for(r2=0; r2<4; r2++) {
				scanf("%c", &c);
				while((!(c > 'A' && c < 'Z')) && c != '.') {
					scanf("%c", &c);
				}
				if(c == 'X') {
					board[r1][r2] = 'X';
				} else if(c == 'O') {
					board[r1][r2] = 'O';
				} else if(c == '.') {
					draw = false;
				} else {
					tx = r1;
					ty = r2;
				}
//				printf("%c", c);
			}
		}
		if(check('X', tx, ty, board) == true) {
			printf("Case #%d: X won\n", cs);
			continue;
		}
		if(check('O', tx, ty, board) == true) {
			printf("Case #%d: O won\n", cs);
			continue;
		}
		if(draw == true) {
			printf("Case #%d: Draw\n", cs);
			continue;
		}
		printf("Case #%d: Game has not completed\n", cs);
	}
	return 0;
}
