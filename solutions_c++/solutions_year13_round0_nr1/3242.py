#include <cstdio>

char map[4][5];

int main(){
	for(int T, t = (scanf("%d", &T), 1); t <= T; t++){
		bool isCmp = true;
		bool xWin = false;
		bool oWin = false;
		for(int r = 0; r < 4; r++){
			scanf("%s", map[r]);
		}
		for(int r = 0; r < 4 && isCmp; r++){
			for(int c = 0; c < 4 && isCmp; c++){
				if(map[r][c] == '.'){
					isCmp = false;
				}
			}
		}
		for(int r = 0; r < 4; r++){
			bool tmp = true;
			for(int c = 0; c < 4 && tmp; c++){
				if(map[r][c] != 'O' && map[r][c] != 'T'){
					tmp = false;
				}
			}
			if(tmp){
				oWin = true;
			}
			tmp = true;
			for(int c = 0; c < 4 && tmp; c++){
				if(map[r][c] != 'X' && map[r][c] != 'T'){
					tmp = false;
				}
			}
			if(tmp){
				xWin = true;
			}
		}
		for(int c = 0; c < 4; c++){
			bool tmp = true;
			for(int r = 0; r < 4; r++){
				if(map[r][c] != 'O' && map[r][c] != 'T'){
					tmp = false;
				}
			}
			if(tmp){
				oWin = true;
			}
			tmp = true;
			for(int r = 0; r < 4 && tmp; r++){
				if(map[r][c] != 'X' && map[r][c] != 'T'){
					tmp = false;
				}
			}
			if(tmp){
				xWin = true;
			}
		}
		bool tmp = true;
		for(int rc = 0; rc < 4 && tmp; rc++){
			if(map[rc][rc] != 'O' && map[rc][rc] != 'T'){
				tmp = false;
			}
		}
		if(tmp){
			oWin = true;
		}
		tmp = true;
		for(int rc = 0; rc < 4 && tmp; rc++){
			if(map[rc][rc] != 'X' && map[rc][rc] != 'T'){
				tmp = false;
			}
		}
		if(tmp){
			xWin = true;
		}
		tmp = true;
		for(int rc = 0; rc < 4 && tmp; rc++){
			if(map[3 - rc][rc] != 'O' && map[3 - rc][rc] != 'T'){
				tmp = false;
			}
		}
		if(tmp){
			oWin = true;
		}
		tmp = true;
		for(int rc = 0; rc < 4 && tmp; rc++){
			if(map[3 - rc][rc] != 'X' && map[3 - rc][rc] != 'T'){
				tmp = false;
			}
		}
		if(tmp){
			xWin = true;
		}
		printf("Case #%d: ", t);
		if(isCmp){
			if      (xWin && ! oWin){
				printf("X won\n");
			}else if(oWin && !xWin){
				printf("O won\n");
			}else{
				printf("Draw\n");
			}
		}else{
			if      (xWin && ! oWin){
				printf("X won\n");
			}else if(oWin && !xWin){
				printf("O won\n");
			}else{
				printf("Game has not completed\n");
			}
		}
	}
	return 0;
}
