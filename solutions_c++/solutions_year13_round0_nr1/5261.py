#include <stdio.h>

#include <stdlib.h>

#include <math.h>

#include <iostream>

using namespace std;

int LookForWinner(char *board, char mark){
	int result=0;
	int partresult;
	
	for(int i=0; i<=3; i++){
		partresult=0;
		for(int j=0; j<=3; j++) if(board[i*4+j]==mark) partresult++;
		if(partresult==4) result++;
		partresult=0;
		for(int j=0; j<=3; j++) if(board[j*4+i]==mark) partresult++;
		if(partresult==4) result++;
	}
	partresult=0;
	for(int j=0; j<=3; j++) if(board[j*5]==mark) partresult++;
	if(partresult==4) result++;
	partresult=0;
	for(int j=0; j<=3; j++) if(board[3+j*3]==mark) partresult++;
	if(partresult==4) result++;
	return result;
}


int main(){
	
	int N;
	
	FILE *fi;
    if(!(fi=fopen("./inputA", "r"))){
        printf("File \'inputA\' could not be opened!\n");
        exit(-1);
    }	
    FILE *fo;
    if(!(fo=fopen("./outputA", "w"))){
        printf("File \'outputA\' could not be opened!\n");
        exit(-1);
    }
    
    fscanf(fi, "%d", &N);
    
    char dump[2];
    char board[16], boardX[16], boardO[16];
    int incomplete = 0;
    
    for(int i=1; i<=N; i++){
    	fscanf(fi, "%c", dump);
    	for(int j=0; j<=3; j++){
    		fscanf(fi, "%4c", board+(4*j));
    		fscanf(fi, "%c", dump);
    	}
    	for(int k=0;k<=15;k++){
    		if(board[k]=='T'){
    			boardX[k]='X';
    			boardO[k]='O';
    		}else{
    			boardX[k]=board[k];
    			boardO[k]=board[k];
    		}
    	}
    	fprintf(fo, "Case #%d: ", i);
    	if(LookForWinner(boardX,'X')>0){
    		fprintf(fo,"X won");
    	} else{
    		if(LookForWinner(boardO,'O')>0){
    			fprintf(fo,"O won");
    		}else{
    			incomplete=0;
    			for(int j=0; j<=15; j++) incomplete=(board[j]=='.')? 1 : incomplete;
    			if(incomplete==1){
    				fprintf(fo,"Game has not completed");
    			}else fprintf(fo,"Draw");
    		}
    	}
    	fprintf(fo, "\n");
    	//printf("%d:\n", i);
    	//printf("%s\n", board);
    }
	//fscanf(fi, "%lg", z+i);

	fclose(fi);    
	fclose(fo);
	
	return 0;
}
