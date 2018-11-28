#include <stdio.h>

int main(void){
	int T, i, j, k;
	char map[4][5];
	int x, o, t;
	int ans; // 0 : not completed, 1 : X win, 2 : O win, 3 : Draw
	
	scanf("%d", &T);
	for (k=1; k<=T; k++){
		for (i=0; i<4; i++) scanf("%s", map[i]);

		ans = 0;

		for (i=0; i<4; i++){
			x = o = t = 0;
			for (j=0; j<4; j++){
				if (map[i][j]=='X') x++;
				if (map[i][j]=='O') o++;
				if (map[i][j]=='T') t++;
			}
			if (x+t==4) ans = 1;
			if (o+t==4) ans = 2;

			x = o = t = 0;
			for (j=0; j<4; j++){
				if (map[j][i]=='X') x++;
				if (map[j][i]=='O') o++;
				if (map[j][i]=='T') t++;
			}
			if (x+t==4) ans = 1;
			if (o+t==4) ans = 2;
		}

		x = o = t = 0;
		for (i=0; i<4; i++){
			if (map[i][i]=='X') x++;
			if (map[i][i]=='O') o++;
			if (map[i][i]=='T') t++;
		}
		if (x+t==4) ans = 1;
		if (o+t==4) ans = 2;

		x = o = t = 0;
		for (i=0; i<4; i++){
			if (map[i][3-i]=='X') x++;
			if (map[i][3-i]=='O') o++;
			if (map[i][3-i]=='T') t++;
		}
		if (x+t==4) ans = 1;
		if (o+t==4) ans = 2;

		printf("Case #%d: ", k);
		if (ans==1) printf("X won\n");
		else if (ans==2) printf("O won\n");
		else {
			for (i=0; i<4; i++){
				for (j=0; j<4; j++) if (map[i][j]=='.') break;
				if (j<4) break;
			}
			if (i<4) printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
	return 0;
}

