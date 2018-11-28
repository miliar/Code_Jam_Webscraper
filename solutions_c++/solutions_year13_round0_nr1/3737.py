#include <cstdio>

int cc;

char map[4][4];
bool dotCheck;

void input(){
	dotCheck = false;

	int i, j;
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			char t[2];
			scanf("%1s", t);
			map[i][j] = t[0];
			if(map[i][j] == '.') dotCheck = true;
		}
	}
}

void oWin(){puts("O won");}
void xWin(){puts("X won");}

void check(){
	int i, j;
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(map[i][j] != 'O' && map[i][j] != 'T')
				break;
		}

		if(j == 4){
			oWin();
			return;
		}
		
		for(j=0; j<4; j++){
			if(map[i][j] != 'X' && map[i][j] != 'T')
				break;
		}

		if(j == 4){
			xWin();
			return;
		}
	}
	
	for(i=0; i<4; i++){
		for(j=0; j<4; j++){
			if(map[j][i] != 'O' && map[j][i] != 'T')
				break;
		}

		if(j == 4){
			oWin();
			return;
		}
		
		for(j=0; j<4; j++){
			if(map[j][i] != 'X' && map[j][i] != 'T')
				break;
		}

		if(j == 4){
			xWin();
			return;
		}
	}

	for(j=0; j<4; j++){
		if(map[j][3-j] != 'O' && map[j][3-j] != 'T')
			break;
	}

	if(j == 4){
		oWin();
		return;
	}

	for(j=0; j<4; j++){
		if(map[j][3-j] != 'X' && map[j][3-j] != 'T')
			break;
	}

	if(j == 4){
		xWin();
		return;
	}


	for(j=0; j<4; j++){
		if(map[j][j] != 'O' && map[j][j] != 'T')
			break;
	}

	if(j == 4){
		oWin();
		return;
	}

	for(j=0; j<4; j++){
		if(map[j][j] != 'X' && map[j][j] != 'T')
			break;
	}

	if(j == 4){
		xWin();
		return;
	}

	if(dotCheck)
		puts("Game has not completed");
	else
		puts("Draw");
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	
	for(cc=1; cc<=t; cc++){
		printf("Case #%d: ", cc);

		input();
		check();
	}

	return 0;
}