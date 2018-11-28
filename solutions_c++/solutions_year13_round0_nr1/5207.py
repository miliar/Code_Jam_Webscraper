#include <cstdio>
using namespace std;

char T[5][5];
bool full;

bool checkRows(char x){
	bool b;
	for (int i=0; i<4; i++){
		b = true;
		for (int j=0; j<4; j++){
			if (T[i][j]!='T' && T[i][j]!=x){
				b = false;
				break;
			}
		}
		if (b) return true;
	}
	return false;
}

bool checkColumns(char x){
	bool b;
	for (int i=0; i<4; i++){
		b = true;
		for (int j=0; j<4; j++){
			if (T[j][i]!='T' && T[j][i]!=x){
				b = false;
				break;
			}
		}
		if (b) return true;
	}
	return false;
}

bool checkDiagonals(char x){
	if ((T[0][0]==x || T[0][0]=='T') && (T[1][1]==x || T[1][1]=='T') && (T[2][2]==x || T[2][2]=='T') && (T[3][3]==x || T[3][3]=='T')) return true;
	if ((T[3][0]==x || T[3][0]=='T') && (T[2][1]==x || T[2][1]=='T') && (T[1][2]==x || T[1][2]=='T') && (T[0][3]==x || T[0][3]=='T')) return true;
	return false;
}

int main(){
	int z;
	scanf("%d", &z);
	for (int j=1; j<=z; j++){printf("Case #%d: ",j);
		full = true;
		for (int i=0; i<4; i++){
			scanf("%s", T[i]);
			for (int j=0; j<4; j++) if (T[i][j]=='.') full = false;
		}
		if (checkRows('O') || checkDiagonals('O') || checkColumns('O')){
			printf("O won\n");
			continue;
		}
		if (checkRows('X') || checkDiagonals('X') || checkColumns('X')){
			printf("X won\n");
			continue;
		}
		if (full) printf("Draw\n");
		else printf("Game has not completed\n");
	}
}

