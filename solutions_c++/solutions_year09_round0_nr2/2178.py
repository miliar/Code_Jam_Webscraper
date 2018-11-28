// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>

int matr[100][100];
char ma[100][100];
int d[100][100];
int T,W, H;
char cc;

int buscarmenor(int i, int j){
	int d = 0;
	int n = matr[i][j];
	if(i>0 && matr[i-1][j]<n){ n = matr[i-1][j]; d=1; }
	if(j>0 && matr[i][j-1]<n){n = matr[i][j-1]; d=2; }
	if(j<W-1 && matr[i][j+1]<n){n = matr[i][j+1]; d=3; }
	if(i<H-1 && matr[i+1][j]<n){ n = matr[i+1][j]; d=4; }
	return d;
}

void marcar(int i, int j, char c){
	if(ma[i][j] != 0)return;
	ma[i][j] = c;
	if(i>0 && d[i-1][j]==4)marcar(i-1,j,c);
	if(j>0 && d[i][j-1]==3)marcar(i,j-1,c);
	if(j<W-1 && d[i][j+1]==2)marcar(i,j+1,c);
	if(i<H-1 && d[i+1][j]==1)marcar(i+1,j,c);
	switch(d[i][j]){
		case 1: marcar(i-1,j,c); break;
		case 2: marcar(i,j-1,c); break;
		case 3: marcar(i,j+1,c); break;
		case 4: marcar(i+1,j,c); break;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	char cade[1000];
	sprintf(cade,"%ls",argv[1]);
	FILE * fp = fopen(cade,"r+t");
	int i , j, k;
	char car;
	fscanf(fp,"%d",&T);
	for(i = 1;i<=T;i++){
		fscanf(fp,"%d %d", &H, &W);
		printf("Case #%d:\r\n", i);
		for(j=0;j<H;j++){
			for(k=0;k<W;k++){
				ma[j][k] = 0;
				d[j][k] = 0;
				matr[j][k] = 11000;
			}
		}
		for(j=0;j<H;j++){
			for(k = 0;k < W; k++){
				fscanf(fp, "%d", &matr[j][k]);
			}
		}
		cc = 'a';
		for(j = 0; j<H; j++){
			for(k = 0; k < W; k++){
				d[j][k] = buscarmenor(j,k);
			}
		}
		for(j = 0; j<H; j++){
			for(k = 0; k < W; k++){
				if(ma[j][k] == 0){
					marcar(j,k,cc);
					cc++;
				}
			}
		}
		for(j = 0; j<H; j++){
			for(k = 0; k < W; k++){
				printf("%c ",ma[j][k]);
			}
			printf("\r\n");
		}
	}
	return 0;
}

