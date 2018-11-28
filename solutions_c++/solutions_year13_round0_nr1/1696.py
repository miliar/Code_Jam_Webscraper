# include <stdio.h>

char b[10][10];
char t[100];
FILE *fp1, *fp2;

int row_win(int r, char ch)
{
	int i;
	for(i = 0; i < 4; i++){
		if(b[r][i] != ch && b[r][i] != 'T')
			return 0;
	}
	return 1; 
}

int col_win(int c, char ch)
{
	int i;
	for(i = 0; i < 4; i++){
		if(b[i][c] != ch && b[i][c] != 'T')
			return 0;
	}
	return 1; 
}

int dia1_win(char ch)
{
	int i;
	for(i = 0; i < 4; i++){
		if(b[i][i] != ch && b[i][i] != 'T')
			return 0;
	}	
	return 1;
}

int dia2_win(char ch)
{
	int i;
	for(i = 0; i < 4; i++){
		if(b[i][3-i] != ch && b[i][3-i] != 'T')
			return 0;
	}
	return 1;
}

int hasDots()
{
	int i, j;
	for(i = 0; i < 4; i++) {
		for(j = 0; j < 4; j++) {
			if(b[i][j] == '.')
				return 1;
		}
	}
	return 0;
}

int main()
{
	int kase = 1, tests;
	
	freopen("judgelarge.txt", "r", stdin);
	freopen("outjudgelarge.txt", "w", stdout);

	gets(t);
	sscanf(t, "%d", &tests);

	while(tests-->0){
	
		for(int i = 0; i < 4; i++)
			gets(b[i]);
		gets(t);


		printf("Case #%d: ", kase++);

		//X wins cases


		if(row_win(0, 'X') || row_win(1, 'X') || row_win(2, 'X') || row_win(3, 'X') ||
			col_win(0, 'X') || col_win(1, 'X') || col_win(2, 'X') || col_win(3, 'X') || dia1_win('X') || dia2_win('X')){
			printf("X won\n");
		}
		else if(row_win(0, 'O') || row_win(1, 'O') || row_win(2, 'O') || row_win(3, 'O') ||
			col_win(0, 'O') || col_win(1, 'O') || col_win(2, 'O') || col_win(3, 'O') || dia1_win('O') || dia2_win('O')){
			printf("O won\n");
		}
		else if(hasDots()){
			printf("Game has not completed\n");
		}
		else {
			printf("Draw\n");
		}

	}

	return 0;
}