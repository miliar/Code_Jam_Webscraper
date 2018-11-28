// RPI.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <stdio.h>
#include <tchar.h>
int n;
char matrix[101][101];

void solve(FILE* fw){
	double wp[101], owp[101],oowp[101];
	int played[101], win[101], oppoent[101];
	for (int i = 0; i < n; ++i){
		played[i] = win[i] = 0;
		for (int j = 0; j < n; ++j){
			if (matrix[i][j] != '.') ++played[i];
			if (matrix[i][j] == '1') ++win[i];
		}
		wp[i] = win[i] / double(played[i]);
	}

	for (int i = 0; i < n; ++i){
		owp[i] = 0;
		oppoent[i] = 0;
		for (int j = 0; j < n; ++j)
			if (matrix[i][j] != '.'){
				++oppoent[i];
				int ww = win[j];
				int pp = played[j] - 1;
				if (matrix[j][i] == '1') --ww;
				owp[i] += ww / double(pp);
		}
		owp[i] = owp[i] / oppoent[i];

	}

	for (int i = 0; i < n; ++i){
		oowp[i] = 0;
		for (int j = 0; j < n; ++j)
			if (matrix[i][j] != '.') oowp[i] += owp[j];
		oowp[i] /= oppoent[i];
	}

	for (int i = 0; i < n; ++i){
		double rpi = 0.25*wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
		fprintf(fw, "%.10f\n", rpi);
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fp = fopen("input.txt","r");
	FILE *fw = fopen("outut.txt","w");
	int t;
	fscanf(fp, "%d",&t);
	for (int i = 1; i <=t; ++i){
		fscanf(fp,"%d",&n);
		for (int j = 0; j < n; ++j){
			char temp[101];
			fscanf(fp, "%s",temp);
			for (int k = 0; k < n; ++k)
				matrix[j][k] = temp[k];
		}
		fprintf(fw,"Case #%d:\n", i);
		solve(fw);
	}
	fclose(fp);
	return 0;
}

