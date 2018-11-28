#include <iostream>
#include <string.h>
#include <cstdio>
using namespace std;
int main(){
	int data[31][11][3];
	for(int i = 0;i < 31;i++)
		for(int j = 0; j < 11;j++)
			for(int k = 0; k < 3;k++)
				data[i][j][k] = 0;
	for(int i = 0;i < 31;i++){
		for(int j = 0; j < 11;j++){
			if( (i/3)*3 + 1 == i && (i/3 + 1) >= j){
				data[i][j][0] = 1;
			}else if( (i/3 + 1)*3 - 1 == i && (i/3 + 1) >= j){
				data[i][j][0] = 1;
			}else if( (i/3)*3 == i && (i/3) >= j){
				data[i][j][0] = 1;
			}
			if( (i/3)*3 + 2 == i && (i/3 + 2) >= j && (i/3 + 2) <= 10){
				data[i][j][1] = 1;
			}else if( (i/3 + 1)*3 - 2 == i && (i/3 + 1) >= j && (i/3 - 1) >= 0){
				data[i][j][1] = 1;
			}else if( (i/3)*3 == i && (i/3 + 1) >= j && i/3 - 1 >=0 && i/3 + 1 <= 10){
				data[i][j][1] = 1;
			}
		}
		// if( (i/3)*3 + 1 == i){
			// printf("%d - %d %d %d\n",i,i/3,i/3,i/3 + 1);
		// }else if( (i/3 + 1)*3 - 1 == i){
			// printf("%d - %d %d %d\n",i,i/3 + 1,i/3 + 1,i/3);
		// }else if( (i/3)*3 == i){
			// printf("%d - %d %d %d\n",i,i/3,i/3,i/3);
		// }
		// if( (i/3)*3 + 2 == i && (i/3 + 2) <= 10){
			// printf("%d - %d %d %d\n",i,i/3,i/3,i/3 + 2);
		// }else if( (i/3 + 1)*3 - 2 == i && (i/3 - 1) >= 0){
			// printf("%d - %d %d %d\n",i,i/3 + 1,i/3 + 1,i/3 - 1);
		// }else if( (i/3)*3 == i && i/3 - 1 >=0 && i/3 + 1 <= 10){
			// printf("%d - %d %d %d\n",i,i/3 - 1,i/3,i/3 + 1);
		// }
	}
	// for(int i = 0;i < 31;i++){
		// int j = 0;
		// while(data[i][j][0] == 1 && j<= 10){
			// printf("%d - %d\n",i,j);
			// j++;
		// }
		// printf("***********%d completed**********\n",i);
	// }
	FILE *ptrin = fopen("23.in","r"),*ptrout = fopen("23.out","w");
	int T;
	fscanf(ptrin,"%d\n",&T);
	for(int i = 0; i < T;i++){
		int N,S,P;
		fscanf(ptrin,"%d %d %d",&N,&S,&P);
		int score[N],result = 0;
		for(int j = 0;j < N;j++){
			fscanf(ptrin,"%d",&score[j]);
			if(data[ score[j] ][P][0] == 1 || (data[ score[j] ][P][1] == 1 && S-- > 0)){
				//printf("%d\n",score[j]);
				result++;
			}
		}
		fprintf(ptrout,"Case #%d: %d\n",i+1,result);
		// for(int j = 0;j < N;j++){
			// if(score[j] == 0 || score[j] == 1 || score[j] == 29 || score[j] == 30){
				// if(data[ score[j] ][P][0] == 1){
					// data[ score[j] ][P][2] == 1;
					// result++;
				// }
			// }
		// }
		// for(int j = 0;j < N;j++){
			// if( !(score[j] == 0 || score[j] == 1 || score[j] == 29 || score[j] == 30 ) ){
				// if(data[ score[j] ][P][0] == 1){
					// data[ score[j] ][P][2] == 1;
					// result++;
				// }
			// }
		// }
	}
}