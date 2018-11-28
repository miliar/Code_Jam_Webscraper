#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

#define MAXT 100
#define MAXH 100
#define MAXW 100

#define SINK 0
#define NORTH 1
#define WEST 2
#define EAST 3
#define SOUTH 4

int T,H,W;

int matrix[MAXH+2][MAXW+2];
char output[MAXH+2][MAXW+2]={0};
char curr='a';

int main(int argc, char* argv[]){
//	if(argc != 2){
//		printf("\nUsage:executable inputfile\n");
//		return -1;
//	}
	FILE * fin;
	FILE * fout;
//	fin = fopen(argv[1],"r");
	fout = fopen("out.txt","w");
	if( fout == NULL){
		printf("\nUnable to open a file\n");
		return -1;
	}

//	fscanf(1,"%d",&T);
//	fscanf(1,"%d",&H);
//	fscanf(1,"%d",&W);
	cin>>T;
//	printf("\n%d %d %d\n",T,H,W);
	for(int i=0 ; i<T ; i++){
		cin>>H;
		cin>>W;
		for(int j=0 ; j<=H+1 ; j++){
			for(int k=0 ; k<=W+1 ; k++){
				matrix[j][k]=100000;
				output[j][k] = 'A';
			}	
		}
		for(int j=1 ; j<=H ; j++){
			for(int k=1 ; k<=W ; k++){
				cin>>matrix[j][k];
				output[j][k] = 'A';
			}	
		}
		int round = 0;
		curr = 'a';
		output[1][1] = 'a';
	int curRow=1;
	while(round < H*W + 1 ){
		curRow=1;
		while(curRow <= H){
			int dir = SINK;
			for(int t = 1; t<=W ; t++){
				if(output[curRow][t]!='A' || true){
					int min = matrix[curRow][t];
					dir = SINK;
					if(matrix[curRow-1][t] < min){
						min = matrix[curRow-1][t];
						dir = NORTH;
					}	
					if(matrix[curRow][t-1] < min){
						min = matrix[curRow][t-1];
						dir = WEST;
					}	
					if(matrix[curRow][t+1] < min){	
						min = matrix[curRow][t+1];
						dir = EAST;
					}	
					if(matrix[curRow+1][t] < min){
						min = matrix[curRow+1][t];
						dir = SOUTH;
					}	
					switch(dir){
						case NORTH:
							if(output[curRow][t]!='A'){
									output[curRow-1][t] = output[curRow][t];
							}
//							if(output[curRow][t]!='A' && round == 1){
//								output[curRow+1][t] = curr+1;
//							}
							if(output[curRow-1][t] != 'A'){
								output[curRow][t] = output[curRow-1][t];
							}
							
							break;
						case WEST:
							if(output[curRow][t]!='A'){
								output[curRow][t-1] = output[curRow][t];
							}
//							if(output[curRow][t]!='A' && round == 1){
//								output[curRow][t-1] = curr+1;
//							}
							if(output[curRow][t-1] != 'A'){
								output[curRow][t] = output[curRow][t-1];
							}
							break;
						case EAST:
							if(output[curRow][t]!='A' ){
								output[curRow][t+1] = output[curRow][t];
							}
//							if(output[curRow][t]!='A' && round == 1){
//								output[curRow][t+1] = curr+1;
//							}
							if(output[curRow][t+1] != 'A'){
								output[curRow][t] = output[curRow][t+1];
							}
							break;
						case SOUTH:
							if(output[curRow][t]!='A' ){
								output[curRow+1][t] = output[curRow][t];
							}
//							if(output[curRow][t]!='A' && round == 1){
//								output[curRow-1][t] = curr+1;
//							}
							if(output[curRow+1][t] != 'A'){
								output[curRow][t] = output[curRow+1][t];
							}
							break;
						case SINK:
//							if(round % 3 >= 1){
								int flag=0;
								char val;
								char temp = output[curRow][t];
								val = temp;/*
								if(temp != 'A'){flag = 1; val=temp;}
								temp = output[curRow-1][t];
								if(temp != 'A'){flag = 1; val=temp;}
								temp = output[curRow][t-1];
								if(temp != 'A'){flag = 1; val=temp;}
								temp = output[curRow][t+1];
								if(temp != 'A'){flag = 1; val=temp;}
								temp = output[curRow+1][t];
								if(temp != 'A')flag = 1;*/
								if(flag == 0 && (round % 3) > 0 && output[curRow][t] == 'A'){		
									val = ++curr;
								}
									output[curRow][t] = val;
//									if(output[curRow][t] != 'A')output[curRow][t] = val;
//									if(output[curRow-1][t] != 'A')output[curRow-1][t] = val;
//									if(output[curRow][t-1] != 'A')output[curRow][t-1] = val;
//									if(output[curRow][t+1] != 'A')output[curRow][t+1] = val;
//									if(output[curRow+1][t] != 'A')output[curRow+1][t] = val;
//							}
							break;
					}
				}
			}
		curRow++;
		}
	round++;
	}
		

		fprintf(fout,"Case #%d:\n",i+1);
		for(int j=1 ; j<=H ; j++){
			for(int k=1 ; k<=W ; k++){
				fprintf(fout,"%c ",output[j][k]);
			}	
			fprintf(fout,"\n");
		}
	}
}
