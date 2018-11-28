#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <limits>
using namespace std;


char map[4][4];
int status;
int i, j;

void row(){
	for(i = 0; i < 4; ++i){
		for(j = 0; j < 4; ++j)
			if(map[i][j] != 'X' && map[i][j] != 'T')
				break;
		if(j == 4){
			status = 0;
			return;
		}

		for(j = 0; j < 4; ++j)
			if(map[i][j] != 'O' && map[i][j] != 'T')
				break;
		if(j == 4){
			status = 1;
			return;
		}
	}
}

void col(){
	for(i = 0; i < 4; ++i){
		bool xWin = true, oWin = true;
		for(j = 0; j < 4; ++j)
			if(map[j][i] != 'X' && map[j][i] != 'T')
				break;
		if(j == 4){
			status = 0;
			return;
		}

		for(j = 0; j < 4; ++j)
			if(map[j][i] != 'O' && map[j][i] != 'T')
				break;
		if(j == 4){
			status = 1;
			return;
		}
	}
}

void diag(){
	bool xWin = true, oWin = true;
	for(i = 0; i < 4; ++i)
		if(map[i][i] != 'X' && map[i][i] != 'T')
			break;
	if(i == 4){
		status = 0;
		return;
	}

	for(i = 0; i < 4; ++i)
		if(map[i][i] != 'O' && map[i][i] != 'T')
			break;
	if(i == 4){
		status = 1;
		return;
	}

	for(i = 0; i < 4; ++i)
		if(map[i][3-i] != 'X' && map[i][3-i] != 'T')
			break;
	if(i == 4){
		status = 0;
		return;
	}
	for(i = 0; i < 4; ++i)
		if(map[i][3-i] != 'O' && map[i][3-i] != 'T')
			break;
	if(i == 4){
		status = 1;
		return;
	}
}

int main(){
	freopen("C:\\in.txt", "r", stdin); //�����ض����������ݽ���in.txt�ļ��ж�ȡ 
	freopen("C:\\out.txt", "w", stdout); //����ض���������ݽ�������out.txt�ļ�

	int T, cnt = 0;
	char buf[10];
	scanf("%d", &T);
	gets(buf);
	while(T--){
		cnt++;
		bool isFull = true;
		for(int i = 0; i < 4; ++i){
			gets(buf);
			for(int j = 0; j < 4; ++j){
				map[i][j] = buf[j];
				if(map[i][j] == '.'){
					isFull = false;
				}
			}
		}
		gets(buf);

		status = -1; row();
		if(status == -1) col();
		if(status == -1) diag();

		printf("Case #%d: ", cnt);
		if(status == -1 && !isFull)
			printf("Game has not completed\n");
		else if(status == -1 && isFull)
			printf("Draw\n");
		else if(status == 0)
			printf("X won\n");
		else if(status == 1)
			printf("O won\n");
	}
}