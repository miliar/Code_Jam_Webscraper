#include <cstdio>
#include <cstring>

#define MAX(a, b) (((a) > (b)) ? (a) : (b))

char board[4][4];

bool check (int x, int y){
	int s = 0, s1 = 0;
	for (int i = 0; i < 4; i++){
		if (board[x][i] == 'T' || board[x][i] == board[x][y]) s++;
		if (board[i][y] == 'T' || board[i][y] == board[x][y]) s1++;
	}
	if (s == 4 || s1 == 4) return true;
	if (x == y){
		s = 0;
		for (int i = 0; i < 4; i++){
			if (board[i][i] == 'T' || board[i][i] == board[x][y]) s++;
			if (s == 4) return true;
		}
	}
	if (s == 3 - y){
		s = 0;
		for (int i = 0; i < 4; i++){
			if (board[i][3 - i] == 'T' || board[i][3 - i] == board[x][y]) s++;
			if (s == 4) return true;
		}
	}
	return false;
}

int main(){
	int t, h = 0;
	freopen ("A.in", "r", stdin);
	freopen ("A.out", "w", stdout);
	scanf ("%d", &t);
	while (h < t){
		printf ("Case #%d: ", ++h);
		int i, j, dot = 0;
		for (i = 0; i < 4; i++)
			scanf ("%s", board[i]);
		bool key = 0;
		for (i = 0; i < 4; i++){
			if (key == 1) break;
			for (j = 0; j < 4; j++){
				if (board[i][j] == '.') dot++;
				if (board[i][j] == 'X' && check (i, j) == true){
					printf ("X won\n");
					key = 1;
					break;
				}
				if (board[i][j] == 'O' && check (i, j) == true){
					printf ("O won\n");
					key = 1;
					break;
				}
			}
		}
		if (key == 0){
			if (dot > 0) printf ("Game has not completed\n");
			else printf ("Draw\n");
		}
	}
}
