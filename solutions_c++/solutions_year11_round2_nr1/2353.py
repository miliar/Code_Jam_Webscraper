// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;


int s[100][100] = {0};
double wp[100];
double owp[100];
double oowp[100];

int _tmain(int argc, _TCHAR* argv[])
{

	FILE *fin, *fout;
	int t;
	fin = fopen("small.in","r");
	fout = fopen("small.out","w");

	fscanf(fin,"%d\n",&t);
	for(int j = 0; j < t; j++){
		int n;
		fscanf(fin, "%d\n", &n);
		for(int i = 0; i < n; i++)
		{
			for(int k = 0; k < n; k++)
			{
				fscanf(fin, "%c", &s[i][k]);
				if(s[i][k] == '0' || s[i][k] == '1')
					s[i][k] -= '0';
				else
					s[i][k] = -1;
			}
			char line;
			fscanf(fin, "%c", &line);
			if(line != '\n')printf("input err %c\n",line);
		}

		for(int i = 0; i < n; i++)
		{
			int sum = 0;
			int win = 0;
			for(int k = 0; k < n; k++){
				if(s[i][k] == 1){
					sum++;
					win++;
				}else if(s[i][k] == 0){
					sum++;
				}else{

				}
			}
			wp[i] = (double)win/(double)sum;
		}
		

		for(int i = 0; i < n; i++)
		{
			double sump = 0;
			int num = 0;
			for(int k = 0; k < n; k++)
			{
				if(s[i][k] != -1)
				{
					num++;
					int sum = 0;
					int win = 0;
					for(int l = 0; l < n; l++)
					{
						if(l == i)continue;
						if(s[k][l] == 1){
							sum++;
							win++;
						}else if(s[k][l] == 0){
							sum++;
						}
					}
					sump += (double)win/(double)sum;
				}
			}
			owp[i] = sump/(double)num;
		}
		

		for(int i = 0; i < n; i++)
		{
			double sump = 0;
			int num = 0;
			for(int k = 0; k < n; k++)
			{
				if(s[i][k] != -1)
				{
					num++;
					sump += owp[k];
				}
			}
			oowp[i] = sump/(double)num;
		}
		

		fprintf(fout, "Case #%d:\n", j+1);
		for(int i = 0; i < n; i++)
		{
			fprintf(fout, "%.7f\n", 0.25*wp[i]+0.50*owp[i]+0.25*oowp[i]);
		}

		memset(s, 0, 100*100);
		for(int i = 0; i < n; i++)
		{
			wp[i] = 0;
			owp[i] = 0;
			oowp[i] = 0;
		}
	}

	return 0;
}

