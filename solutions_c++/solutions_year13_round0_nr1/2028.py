#include<cstdio>
#include<cstdlib>
bool isWin(char s[4][5], char who){
	bool win;
	for(int i=0;i<4;i++){
		win = true;
		for(int j=0;j<4;j++)
			if(s[i][j] != who && s[i][j] != 'T')
				win = false;
		if(win)
			return true;
	}
	for(int i=0;i<4;i++){
		win = true;
		for(int j=0;j<4;j++)
			if(s[j][i] != who && s[j][i] != 'T')
				win = false;
		if(win)
			return true;
	}
	win = true;
	for(int i=0;i<4;i++)
		if(s[i][i] != who && s[i][i] != 'T')
			win = false;
	if(win)
		return true;
	win = true;
	for(int i=0;i<4;i++)
		if(s[i][3-i] != who && s[i][3-i] != 'T')
			win = false;
	if(win)
		return true;
}
bool isFull(char s[4][5]){
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(s[i][j] == '.')
				return false;
	return true;
}
int main(){
	int C;
	scanf("%d",&C);
	for(int Case=1; Case<=C; Case++){
		char s[4][5];
		for(int i=0; i<4; i++)
			scanf("%s",s[i]);
		printf("Case #%d: ",Case);
		if(isWin(s,'X'))
			puts("X won");
		else if(isWin(s,'O'))
			puts("O won");
		else if(isFull(s))
			puts("Draw");
		else puts("Game has not completed");
	}
}
