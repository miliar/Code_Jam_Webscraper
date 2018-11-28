//============================================================================
// Name        : 2010_1A_A.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

#include <gmpxx.h>
#include <string.h>
#include <errno.h>

int main(void) {

	int T;
	int N, K;
	char n[100][100];
	char rBuf[100], bBuf[100];
	char vert[100], diag[100];
	scanf("%d", &T);
	printf("T = %d\n", T);

	for(int x = 1; x <= T; x++){
		printf("---------------------------------\n");
		printf("Case # %d\n", x);
		int r = 0, b = 0;

		scanf("%d%d", &N, &K);
		printf("N = %d, K = %d\n", N ,K);
		for(int i = 0; i < N; i++){
			scanf("%s", n[i]);
		}

		for(int i = 0; i < N; i++){
			for(int j = N - 1; j >= 0; j--){
				if(n[i][j] == '.'){
					int k = 0, k0 = 999;
					for(k = j - 1; k >= 0; k--){
						if(n[i][k] != '.'){
							k0 = j - k;
							break;
						}
					}
					if(k0 == 999){break;}
					for(k = j; k >= 0; k--){
						if(k >= k0){
							n[i][k] = n[i][k-k0];
						} else {
							n[i][k] = '.';
						}
					}
				}
			}
			printf("%s\n", n[i]);
		}

		for(int i = 0; i < K; i++){
			rBuf[i] = 'R';
			bBuf[i] = 'B';
		}
		rBuf[K] = 0;
		bBuf[K] = 0;

		//horizon
		for(int i = 0; i < N; i++){
			n[i][N] = 0;
			printf("%s\n", n[i]);
			if(strstr(n[i], rBuf)){
				printf("RED!!\n");
				r = 1;
			}
			if(strstr(n[i], bBuf)){
				printf("BLUE!!\n");
				b = 1;
			}
		}

		//vert
		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				vert[j] = n[j][i];
			}
			vert[N] = 0;

			printf("%s\n", vert);
			if(strstr(vert, rBuf)){
				printf("RED!!\n");
				r = 1;
			}
			if(strstr(vert, bBuf)){
				printf("BLUE!!\n");
				b = 1;
			}
		}

		//diag1
		for(int i = 0; i < N; i++){//offset
			for(int k = 0; k < N; k++){
				if(i + k < N){
					diag[k] = n[k][i+k];
				} else {
					diag[k] = 0;
					break;
				}
			}
			diag[N] = 0;

			printf("%s\n", diag);
			if(strstr(diag, rBuf)){
				printf("RED!!\n");
				r = 1;
			}
			if(strstr(diag, bBuf)){
				printf("BLUE!!\n");
				b = 1;
			}
		}
		for(int i = 1; i < N; i++){//offset
			for(int k = 0; k < N; k++){
				if(i + k < N){
					diag[k] = n[i+k][k];
				} else {
					diag[k] = 0;
					break;
				}
			}
			diag[N] = 0;

			printf("%s\n", diag);
			if(strstr(diag, rBuf)){
				printf("RED!!\n");
				r = 1;
			}
			if(strstr(diag, bBuf)){
				printf("BLUE!!\n");
				b = 1;
			}
		}

		//diag2
		for(int i = 0; i < N; i++){//offset
			for(int k = 0; k < N; k++){
				if(i + k < N){
					diag[k] = n[k][N-(i+k)-1];
				} else {
					diag[k] = 0;
					break;
				}
			}
			diag[N] = 0;

			printf("%s\n", diag);
			if(strstr(diag, rBuf)){
				printf("RED!!\n");
				r = 1;
			}
			if(strstr(diag, bBuf)){
				printf("BLUE!!\n");
				b = 1;
			}
		}
		for(int i = 1; i < N; i++){//offset
			for(int k = 0; k < N; k++){
				if(i + k < N){
					diag[k] = n[i+k][N-k-1];
				} else {
					diag[k] = 0;
					break;
				}
			}
			diag[N] = 0;

			printf("%s\n", diag);
			if(strstr(diag, rBuf)){
				printf("RED!!\n");
				r = 1;
			}
			if(strstr(diag, bBuf)){
				printf("BLUE!!\n");
				b = 1;
			}
		}

		if(r && !b){
			fprintf(stderr, "Case #%d: %s\n", x, "Red");
		} else if(!r && b){
			fprintf(stderr, "Case #%d: %s\n", x, "Blue");
		} else if(r && r){
			fprintf(stderr, "Case #%d: %s\n", x, "Both");
		} else{
			fprintf(stderr, "Case #%d: %s\n", x, "Neither");
		}
	}

	return 0;
}
