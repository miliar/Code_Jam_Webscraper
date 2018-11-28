#include<stdio.h>

char map[4][5];

#define OKAY(a, b) (a == 'T' || a == b)
bool equals_hor(int colidx, char c){
	return OKAY(map[0][colidx], c) && OKAY(map[1][colidx], c) && OKAY(map[2][colidx], c) && OKAY(map[3][colidx], c);
}
bool equals_ver(int rowidx, char c){
	return OKAY(map[rowidx][0], c) && OKAY(map[rowidx][1], c) && OKAY(map[rowidx][2], c) && OKAY(map[rowidx][3], c);
}
bool equals_cross(char c){
	return (OKAY(map[0][0], c) && OKAY(map[1][1], c) && OKAY(map[2][2], c) && OKAY(map[3][3], c))
		|| (OKAY(map[3][0], c) && OKAY(map[2][1], c) && OKAY(map[1][2], c) && OKAY(map[0][3], c));
}

int main(){
	int tcnt;
	scanf("%d", &tcnt);
	int tcnti;
	for(tcnti = 0; tcnti < tcnt; tcnti++){
		scanf("%s %s %s %s", map[0], map[1], map[2], map[3]);
		
		bool isallfilled = true;
		int i, j;
		for(i = 0; i < 4; i++)
			for(j = 0; j < 4; j++)
				if(map[i][j] == '.'){
					isallfilled = false;
					break;
				}
		bool Owin = equals_ver(0, 'O') || equals_ver(1, 'O') || equals_ver(2, 'O') || equals_ver(3, 'O')
			|| equals_hor(0, 'O') || equals_hor(1, 'O') || equals_hor(2, 'O') || equals_hor(3, 'O')
			|| equals_cross('O');
		bool Xwin = equals_hor(0, 'X') || equals_hor(1, 'X') || equals_hor(2, 'X') || equals_hor(3, 'X')
			|| equals_ver(0, 'X') || equals_ver(1, 'X') || equals_ver(2, 'X') || equals_ver(3, 'X')
			|| equals_cross('X');

		if((Owin && Xwin) || (!Owin && !Xwin && isallfilled))
			printf("Case #%d: Draw\n", tcnti + 1);
		else if(Owin)
			printf("Case #%d: O won\n", tcnti + 1);
		else if(Xwin)
			printf("Case #%d: X won\n", tcnti + 1);
		else
			printf("Case #%d: Game has not completed\n", tcnti + 1);
	}
	return 0;
}