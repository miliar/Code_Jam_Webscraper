#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;

int cmp(char a, char b){
	if(a == '.' || b == '.') return 0;
	if(a == b || a == 'T' || b == 'T') return 1;
	else return 0;
}

void output(int won){
	if(won == 1) puts("X won");
	else if(won == 2) puts("O won");
	else if(won == -1) puts("Draw");
	else puts("Game has not completed");
}

int main(){
	int repeat, won;
	char map[4][10];
	scanf("%d", &repeat);
	getchar();
	for(int re = 1;re <= repeat;re++){
		won = -1;
		for(int i = 0;i < 4;i++){
			scanf("%s", map[i]);
			if(won < 0){
				for(int j = 0;j < 4;j++){
					if(map[i][j] == '.'){
						won = 0;
						break;
					}
				}
			}
		}
		for(int i = 0, j = 0;i < 4 && won <= 0;i++){
			if(cmp(map[i][0], map[i][1]) && cmp(map[i][1], map[i][2]) && cmp(map[i][2], map[i][3])){
				while(map[i][j] == 'T') j++;
				if(map[i][j] == 'X') won = 1;
				else if(map[i][j] == 'O') won = 2;
				break;
			}
		}
		for(int i = 0, j = 0;i < 4 && won <= 0;i++){
			if(cmp(map[0][i], map[1][i]) && cmp(map[1][i], map[2][i]) && cmp(map[2][i], map[3][i])){
				while(map[j][i] == 'T') j++;
				if(map[j][i] == 'X') won = 1;
				else if(map[j][i] == 'O') won = 2;
				break;
			}
		}
		for(int i = 0;won <= 0;){
			if(cmp(map[0][0], map[1][1]) && cmp(map[1][1], map[2][2]) && cmp(map[2][2], map[3][3])){
				while(map[i][i] == 'T') i++;
				if(map[i][i] == 'X') won = 1;
				else if(map[i][i] == 'O') won = 2;
			}
			break;
		}
		for(int i = 0;won <= 0;){
			if(cmp(map[0][3], map[1][2]) && cmp(map[1][2], map[2][1]) && cmp(map[2][1], map[3][0])){
				while(map[i][3 - i] == 'T') i++;
				if(map[i][3 - i] == 'X') won = 1;
				else if(map[i][3 - i] == 'O') won = 2;
			}
			break;
		}
		printf("Case #%d: ", re);
		output(won);
		getchar();
	}
	return 0;
}

