#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int MAXN = 10;

int get(){
    char c = getchar();
    while(c != '.' && c != 'T' && c != 'X' && c != 'O')
	c = getchar();
    return c;
}

int n = 4;
int mat[MAXN][MAXN];

bool checkRaw(int who, int j){
    int num = 0, t = 0;
    for(int i = 0; i < n; i++)
	if(mat[j][i] == who) 
	    num++;
	else if(mat[j][i] == 'T')
	    t++;
    if(num == 4 || num == 3 && t == 1)
	return true;
    else
	return false;
}

bool checkCol(int who, int j){
    int num = 0, t = 0;
    for(int i = 0; i < n; i++)
	if(mat[i][j] == who) 
	    num++;
	else if(mat[j][i] == 'T')
	    t++;
    if(num == 4 || num == 3 && t == 1)
	return true;
    else
	return false;
}

bool checkDiagonal(int who, int inc){
    int x, y, dx, dy;
    if(inc == 1){
	x = 0, y = 0;
	dx = dy = 1;
    }else{
	x = 0, y = 3;
	dx = 1, dy = -1;
    }

    int num = 0, t = 0;
    for(int i = 0; i < n; i++){ 
	if(mat[x][y] == who) 
	    num++;
	else if(mat[x][y] == 'T')
	    t++;
	x += dx, y += dy;
    }

    if(num == 4 || num == 3 && t == 1)
	return true;
    else
	return false;
}

bool win(int who){
    for(int i = 0; i < n; i++)
	if(checkRaw(who, i) || checkCol(who, i))
	    return true;
    if(checkDiagonal(who, 1) || checkDiagonal(who, -1))
	return true;
    return false;
}

int main(){
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
	printf("Case #%d: ", cas);
	for(int i = 0; i < n; i++)
	    for(int j = 0; j < n; j++)
		mat[i][j] = get();
	bool xCanWin = win('X');
	bool oCanWin = win('O');
	if(xCanWin || oCanWin){
	    if(xCanWin) printf("X won\n");
	    else printf("O won\n");
	}else{
	    bool draw = true;
	    for(int i = 0; i < n && draw; i++)
		for(int j = 0; j < n && draw; j++)
		    if(mat[i][j] == '.')
			draw = false;
	    if(draw) printf("Draw\n");
	    else printf("Game has not completed\n");
	}
    }
    return 0;
}
