#include<stdio.h>
#include<algorithm>
using namespace std;

const int MAX_N = 50;
char ori_board[MAX_N][MAX_N];
char rot_board[MAX_N][MAX_N];

bool isWin(int N, int K, char color){
	int i, j;

	for(i=0; i<N; i++){
		int curCnt, maxCnt;
		if(N-i < K)	break;

		curCnt = maxCnt = 0;
		for(j=0; i+j<N; j++){
			if(rot_board[i+j][j] == color){
				curCnt++;
				maxCnt = maxCnt < curCnt ? curCnt : maxCnt;
			}else	curCnt = 0;
		}
		if(maxCnt >= K)	return true;
		
		curCnt = maxCnt = 0;
		for(j=0; i+j<N; j++){
			if(rot_board[j][i+j] == color){
				curCnt++;
				maxCnt = maxCnt < curCnt ? curCnt : maxCnt;
			}else	curCnt = 0;
		}
		if(maxCnt >= K)	return true;
	}

	for(i=0; i<N; i++){
		int curCnt, maxCnt;
		if(N-i < K)	break;

		curCnt = maxCnt = 0;
		for(j=N-1; i+(N-1)-j<N; j--){
			if(rot_board[i+(N-1)-j][j] == color){
				curCnt++;
				maxCnt = maxCnt < curCnt ? curCnt : maxCnt;
			}else	curCnt = 0;
		}
		if(maxCnt >= K)	return true;
		
		curCnt = maxCnt = 0;
		for(j=0; (N-1)-i-j>=0; j++){
			if(rot_board[j][(N-1)-i-j] == color){
				curCnt++;
				maxCnt = maxCnt < curCnt ? curCnt : maxCnt;
			}else	curCnt = 0;
		}
		if(maxCnt >= K)	return true;
	}

	for(i=0; i<N; i++){
		int curCnt, maxCnt;

		curCnt = maxCnt = 0;
		for(j=0; j<N; j++){
			if(rot_board[i][j] == color){
				curCnt++;
				maxCnt = maxCnt < curCnt ? curCnt : maxCnt;
			}else	curCnt = 0;
		}
		if(maxCnt >= K)	return true;
		
		curCnt = maxCnt = 0;
		for(j=0; j<N; j++){
			if(rot_board[j][i] == color){
				curCnt++;
				maxCnt = maxCnt < curCnt ? curCnt : maxCnt;
			}else	curCnt = 0;
		}
		if(maxCnt >= K)	return true;
	}

	return false;
}

int main(){
	char finname[256] = "A-large.in";
	char foutname[256] = "A-large.out";
	FILE *fin = fopen(finname, "r");
	FILE *fout = fopen(foutname, "w");

	int T;
	fscanf(fin, "%d", &T);

	for(int t=0; t<T; t++){
		int N, K;
		char tmp;

		fscanf(fin, "%d %d\n", &N, &K);
		
		int i, j, l;

		for(i=0; i<N; i++){
			for(j=0; j<N; j++){
				fscanf(fin, "%c", &ori_board[i][j]);
				rot_board[j][(N-1)-i] = ori_board[i][j];
			}
			fscanf(fin, "%c", &tmp);	
		}

		for(j=0; j<N; j++){
			for(i=N-1; i>=0; i--){
				if(rot_board[i][j] != '.'){
					for(l=i+1; l<N; l++){
						if(rot_board[l][j] != '.')	break;
					}
					
					tmp = rot_board[i][j];
					rot_board[i][j] = rot_board[l-1][j];
					rot_board[l-1][j] = tmp;
				}
			}
		}
		/*
		for(i=0; i<N; i++){
			for(j=0; j<N; j++)	printf("%c", rot_board[i][j]);
			printf("\n");
		}*/

		bool isRWin = isWin(N, K, 'R');
		bool isBWin = isWin(N, K, 'B');

		if(isRWin && isBWin)	fprintf(fout, "Case #%d: Both\n", t+1);
		else if(isRWin)			fprintf(fout, "Case #%d: Red\n", t+1);
		else if(isBWin)			fprintf(fout, "Case #%d: Blue\n", t+1);
		else					fprintf(fout, "Case #%d: Neither\n", t+1);
	}



	fcloseall();

	return 0;
}