#include <stdio.h>

void scanBoard(char B[][4]){

	for(int i=0; i<4; i++){
		scanf("\n");
		for(int j=0; j<4; j++){
			scanf("%c", &B[i][j]);
		}
		// scanf("\n");
	}
}

void prnBoard(char B[][4]){
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			printf("%c ",B[i][j]);
		}
		printf("\n");
	}
}

int chkBoard(char B[][4]){
	int complete = 1, t,c=0;
	for(int i=0; i<4; i++){
		t = 0; c=0;
		for(int j=0; j<4; j++){
			switch(B[i][j]){
				case '.' : { complete = 0; break; }
				case 'T' : { t = 1; break; }
				case 'X' : { c--; break; }
				case 'O' : c++;
			}
		}
		if(c==4 || (c==3 && t)) return 2;
		if(c==-4 || (c==-3 && t)) return 1;
	}
	for(int i=0; i<4; i++){
		t = 0; c=0;
		for(int j=0; j<4; j++){
			switch(B[j][i]){
				case '.' : { complete = 0; break; }
				case 'T' : { t = 1; break; }
				case 'X' : { c--; break; }
				case 'O' : c++;
			}
		}
		if(c==4 || (c==3 && t)) return 2;
		if(c==-4 || (c==-3 && t)) return 1;
	}

	t = 0; c=0;
	for(int j=0; j<4; j++){
		switch(B[j][j]){
			case '.' : { complete = 0; break; }
			case 'T' : { t = 1; break; }
			case 'X' : { c--; break; }
			case 'O' : c++;
		}
	}
	if(c==4 || (c==3 && t)) return 2;
	if(c==-4 || (c==-3 && t)) return 1;

		t = 0; c=0;
	for(int j=0; j<4; j++){
		switch(B[j][3-j]){
			case '.' : { complete = 0; break; }
			case 'T' : { t = 1; break; }
			case 'X' : { c--; break; }
			case 'O' : c++;
		}
	}
	if(c==4 || (c==3 && t)) return 2;
	if(c==-4 || (c==-3 && t)) return 1;

	if(complete) return 3;
	return 4;
}

int main(){

	const char* pRes[]={"X won", "O won", "Draw", "Game has not completed"};
	char* result;
	int t, res;
	char B[4][4]={};
	scanf("%d", &t);
	for(int k = 1; k<=t; k++){

		scanBoard(B);
		res = chkBoard(B);
		// prnBoard(B);
		result = (char*)pRes[res-1];
		printf("Case #%d: %s\n", k, result);
		// printf("\t %d \n", chkBoard(B));
	}
	return 0;
}

void initArr(int A[], int size){ for (int i = 0; i < size; ++i) A[i] = 0; }
void prnArr(int A[], int size){ for (int i = 0; i < size; ++i) printf("%d ", A[i]); printf("\n"); }