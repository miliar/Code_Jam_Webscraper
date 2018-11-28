// this.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include<iostream>
using namespace std;
#include<stdio.h>
#include<cstdio>
#include<string.h>



int N, T;
double WP[101];
double OWP[101];
double OOWP[101];
char w[101][101];


double wp(int index)
{
			double all = 0,win = 0;
			for(int r = 0; r < N ; r++)
			{
				if(w[index][r] == '.')
					continue;
				if(w[index][r] == '1')
					win ++,all ++;
				else
					all++;
			}
			
			return win / all;
}

double owp(int index)
{
	double o[101] = {0};
	double all = 0,win = 0;
	for(int i = 0; i < N; i ++)
	{
		if(index == i || w[index][i] == '.')
			continue;
		all = 0,win = 0;
		for(int j = 0; j < N; j ++)
		{
			if(j == index || w[i][j] == '.')
				continue;
			if(w[i][j] == '1')
				all ++, win ++;
			else
				all ++;
		}
		
		o[i] = win / all;
	}
	double sum = 0;
	double sumn = 0;
	for(int x = 0; x < N;x ++)
	{
		if(x == index)
			continue;
		if(w[index][x] != '.')
			sumn ++;sum += o[x];
	}
	return sum/sumn;
}

double oowp(int index )
{
	double n = 0,sum = 0;
	for(int i = 0 ; i <N; i ++)
	{
		if(w[index][i] != '.')
		{
			n ++;
			sum += OWP[i];
		}

	}
	return sum/n;
}


int main()
{

	FILE *fp = fopen("A-small-attempt0.in","r");
	FILE *fpw = fopen("A-small-attempt0.out","w");
	

	fscanf(fp, "%d", &T);
	for(int i = 1; i <= T; i ++)
	{
		fscanf(fp, "%d", &N);
		fprintf(fpw,"Case #%d:\n",i);
		for(int j = 0; j < N; j++)
		{
			char nu;
			fscanf(fp, "%c" ,&nu);
			for(int k = 0; k < N; k ++)
			{				
				fscanf(fp, "%c", &w[j][k]);				
			}
		}
		
		
			double RPI;
			for (int y = 0; y < N; y ++)
			{
				WP[y]=wp(y);
				
			}
			for (int y = 0; y < N; y ++)
				OWP[y]=owp(y);
			for (int y = 0; y < N; y ++)
			{
				OOWP[y]=oowp(y);
				RPI = 0.25 * WP[y] + 0.5 * OWP[y] + 0.25 * OOWP[y];
				fprintf(fpw,"%.12lf\n", RPI);
			}	



			
		
		
		
	}
	return 0;
	
}


