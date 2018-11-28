// a.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdlib.h>
#include <stdio.h>

void rotate(char** board, int n)
{
	char* buf = new char[n];
	for(int i = 0; i < n; i++)
	{
		int p = 0;
		for(int j = 0; j < n; j++)
		{
			if(board[i][j] != '.')
			{
				buf[p] = board[i][j];
				p++;
			}
		}
		for(int j = 0; j < n; j++)
		{
			if( j < n-p)
			{
				board[i][j] = '.';
			}else{
				board[i][j] = buf[j-n+p];
			}
		}

		for(int j = 0; j < n; j++)
		{
			printf("%c ",board[i][j]);
		}
		printf("\n");
	}
	delete [] buf;
}

void setscore(int& count, int& newcount, int k)
{
	//if(newcount > k)return;
	count = newcount>count?newcount:count;
	newcount = 0;
}

//0 none, 1 r, 2 b, 3 both
int check(char** board, int n, int k)
{
	bool r =false, b = false;
	for(int i = 0; i < n; i++)
	{
		int countR = 0, countB = 0, newcountR = 0, newcountB = 0;
		for(int j = 0; j < n; j++)
		{
			if(board[i][j] == 'R')
			{
				setscore(countB,newcountB,k);
				newcountR++;
			}else if(board[i][j] == 'B'){
				setscore(countR,newcountR,k);
				newcountB++;
			}else{
				setscore(countR,newcountR,k);
				setscore(countB,newcountB,k);
			}
		}
		setscore(countR,newcountR,k);
		setscore(countB,newcountB,k);
		if(countR >= k)r = true;
		if(countB >= k)b = true;
		if(r && b)return 3;
	}

	for(int i = 0; i < n; i++)
	{
		int countR = 0, countB = 0, newcountR = 0, newcountB = 0;
		for(int j = 0; j < n; j++)
		{
			if(board[j][i] == 'R')
			{
				setscore(countB,newcountB,k);
				newcountR++;
			}else if(board[j][i] == 'B'){
				setscore(countR,newcountR,k);
				newcountB++;
			}else{
				setscore(countR,newcountR,k);
				setscore(countB,newcountB,k);
			}
		}
		setscore(countR,newcountR,k);
		setscore(countB,newcountB,k);
		if(countR >= k)r = true;
		if(countB >= k)b = true;
		if(r && b) return 3;
	}

	for(int m = k-1; m < 2*n-k; m++)
	{
		int countR = 0, countB = 0, newcountR = 0, newcountB = 0;
		if(m < n)
		{
			int i = m;
			for(int j = 0; j < m+1; j++)
			{
				if(board[i][j] == 'R')
				{
					setscore(countB,newcountB,k);
					newcountR++;
				}else if(board[i][j] == 'B'){
					setscore(countR,newcountR,k);
					newcountB++;
				}else{
					setscore(countR,newcountR,k);
					setscore(countB,newcountB,k);
				}
				i--;
			}
		}else{
			int i = n-1;
			for(int j = m-n+1; j < n; j++)
			{
				if(board[i][j] == 'R')
				{
					setscore(countB,newcountB,k);
					newcountR++;
				}else if(board[i][j] == 'B'){
					setscore(countR,newcountR,k);
					newcountB++;
				}else{
					setscore(countR,newcountR,k);
					setscore(countB,newcountB,k);
				}
				i--;
			}
		}
		setscore(countR,newcountR,k);
		setscore(countB,newcountB,k);
		if(countR >= k)r = true;
		if(countB >= k)b = true;
		if(r && b) return 3;
	}

	for(int m = k-1; m < 2*n-k; m++)
	{
		int countR = 0, countB = 0, newcountR = 0, newcountB = 0;
		if(m < n)
		{
			int i = 0;
			for(int j = n-m-1; j < n; j++)
			{
				if(board[i][j] == 'R')
				{
					setscore(countB,newcountB,k);
					newcountR++;
				}else if(board[i][j] == 'B'){
					setscore(countR,newcountR,k);
					newcountB++;
				}else{
					setscore(countR,newcountR,k);
					setscore(countB,newcountB,k);
				}
				i++;
			}
		}else{
			int j = 0;
			for(int i = m-n+1; i < n; i++)
			{
				if(board[j][i] == 'R')
				{
					setscore(countB,newcountB,k);
					newcountR++;
				}else if(board[j][i] == 'B'){
					setscore(countR,newcountR,k);
					newcountB++;
				}else{
					setscore(countR,newcountR,k);
					setscore(countB,newcountB,k);
				}
				j++;
			}
		}
		setscore(countR,newcountR,k);
		setscore(countB,newcountB,k);
		if(countR >= k)r = true;
		if(countB >= k)b = true;
		if(r && b) return 3;
	}
	if (!r && !b)return 0;
	else if(r && !b)return 1;
	else if(!r && b)return 2;
	else return 3;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *fin, *fout;
	fin = fopen("a.in","r");
	fout = fopen("a.out","w");
	int t;
	fscanf(fin,"%d\n",&t);
	for(int i = 0; i < t; i++)
	{
		int n, k;
		char ch;
		fscanf(fin, "%d %d\n",&n, &k);
		char** board = new char*[n];
		for(int p = 0; p < n; p++)
		{
			board[p] = new char[n];
		}

		for(int p = 0; p < n; p++)
		{
			for(int q =0; q < n; q++)
			{
				ch = fgetc(fin);
				board[p][q] = ch;
			}
			fgetc(fin);
		}
		rotate(board,n);
		int res = check(board,n,k);
		if(res == 0)
		{
			fprintf(fout,"Case #%d: Neither\n",i+1);
		}else if(res == 1){
			fprintf(fout,"Case #%d: Red\n",i+1);
		}else if(res == 2){
			fprintf(fout,"Case #%d: Blue\n",i+1);
		}else if(res == 3){
			fprintf(fout,"Case #%d: Both\n",i+1);
		}
	}
	return 0;
}

