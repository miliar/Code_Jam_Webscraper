#include<stdio.h>


int T, N, Tcount;
char map[13][13];
int row[2][5];
int col[2][5];
int diag[2][5];
int flag, gamenot;
FILE *fp, *fout;

void input();
void process();
void output();
void diago(int i, int j, char symbol);

int main(){
	fp = fopen("input.txt","r");
	fout = fopen("output.txt", "w");
	fscanf(fp,"%d", &T);
	for(Tcount = 1; Tcount <= T; Tcount++){
		input();
		process();
		output();
	}
	return 0;
}

void input(){
	int i;
	for(i=1;i<=4;i++){
		fscanf(fp,"%s",&map[i][1]);
		row[0][i] = 0;
		row[1][i] = 0;
		col[0][i] = 0;
		col[1][i] = 0;
		diag[0][i-1] = 0;
		diag[1][i-1] = 0;
	}
}

void diago(int i, int j, char symbol){
	if(i == j){
		if(symbol == 'O' || symbol == 'T')
			diag[0][0]++;
		if(symbol == 'X' || symbol == 'T')
			diag[1][0]++;
	}
	if(i+j == 5){
		if(symbol == 'O' || symbol == 'T')
			diag[0][1]++;
		if(symbol == 'X' || symbol == 'T')
			diag[1][1]++;
	}
}

void process(){
	int i, j;
	flag = 2; gamenot = 0;
	N = 4;
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++){
			
			if(map[i][j] == 'O' || map[i][j] == 'T'){
				row[0][i]++;
				col[0][j]++;
			}
			if(map[i][j] == 'X' || map[i][j] == 'T'){
				row[1][i]++;
				col[1][j]++;
			}
			diago(i,j,map[i][j]);
			if(map[i][j] == '.') gamenot = 1;
		}
	}

	for(i=0;i<=1;i++){
		for(j=1;j<=4;j++){
			if(row[i][j] == 4) flag = i;
			if(col[i][j] == 4) flag = i;
		}
		for(j=0;j<=1;j++){
			if(diag[i][j] == 4) flag = i;
		}
	}
}

void output(){
	fprintf(fout,"Case #%d: ",Tcount);
	if(flag == 0){
		fprintf(fout,"O won\n");
	}
	else if(flag == 1){
		fprintf(fout, "X won\n");
	}
	else if(gamenot == 1){
		fprintf(fout, "Game has not completed\n");
	}
	else fprintf(fout, "Draw\n");
}