#include "stdafx.h"
#include<iostream>
using namespace std;
#include<stdio.h>
#include<cstdio>
#include<string.h>

int N, T, L, H;
int n[1001];


int main()
{

	FILE *fp = fopen("C-small-attempt0.in","r");
	FILE *fpw = fopen("C-small-attempt0.out","w");
	

	fscanf(fp, "%d", &T);
	for(int i = 1; i <= T; i ++)
	{
		fscanf(fp, "%d%d%d", &N,&L,&H);
		for(int j = 0; j < N; j ++)
		{
			fscanf(fp,"%d",&n[j]);
		}
		int x = L;
		while(x <= H)
		{
			int y;
			for(y = 0; y <N; y ++)
			{
				if(x % n[y] == 0 || n[y] % x ==0)
					;
				else
					break;
			}
			if(y == N)
			{
				fprintf(fpw,"Case #%d: %d\n",i,x);
				break;
			}
			x ++;
		}
		if(x == H + 1)
			fprintf(fpw,"Case #%d: NO\n",i);


	}
	return 0;
	
}

