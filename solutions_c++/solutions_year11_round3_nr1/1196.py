// this.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include<iostream>
using namespace std;
#include<stdio.h>
#include<cstdio>
#include<string.h>
#include<vector>
#include<queue>
#include<stack>

int N, T;
int R,C;
char col[51][51];
int m[51][51];
int blue = 0;



int red()
{
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j <C ;j ++)
		{
			if (m[i][j] == 1 || col[i][j] =='.')
				continue;
			if (col[i][j] =='#')
			{
				if(col[i][j+1] != '#' || col[i+1][j] != '#' || col[i+1][j+1] != '#')
					return 0;
				else
				{
					col[i][j] = '/',col[i][j+1] = '\\',col[i+1][j] = '\\',col[i+1][j+1] = '/';
				}
			}
		}
	}
	return 1;
}







int main()
{
	FILE *fp = fopen("A-small-attempt0.in","r");
	FILE *fpw = fopen("A-small-attempt0.out","w");	

	fscanf(fp, "%d", &T);

	for(int i = 1; i <= T; i ++)
	{
		fscanf(fp, "%d", &R);
		fscanf(fp, "%d", &C);
		blue = 0;
		for(int i = 0; i < R; i ++)
		{
			char c;
			fscanf(fp, "%c", &c);
			for(int j = 0;j < C; j ++)
			{
				fscanf(fp, "%c", &col[i][j]);
				m[i][j] = 0;
				if(col[i][j] == '#')
					blue ++;
			}
			
		}

		if(blue % 4 != 0)
			fprintf(fpw,"Case #%d:\nImpossible\n",i);
		else
		{
			if(red() == 0)
				fprintf(fpw,"Case #%d:\nImpossible\n",i);
			else
			{
				fprintf(fpw,"Case #%d:\n",i);
				for(int p = 0; p < R; p++)
				{
					for(int q = 0; q <C; q++)
					{
						fprintf(fpw,"%c",col[p][q]);
					}
					fprintf(fpw,"\n");
				}
			}
		}
			



	}
	return 0;
	
}


