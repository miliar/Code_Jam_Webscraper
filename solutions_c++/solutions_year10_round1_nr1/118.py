// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
// Some solutions using BigInteger from http://mattmccutchen.net/bigint/
#include "bigint/BigIntegerAlgorithms.hh"
#include "bigint/BigIntegerUtils.hh"
#include "utilUtils.h"
#include "utilFile.h"
#include "utilString.h"
#include "assert.h"
#include "utilArray.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "utilRand.h"
#include <vector>
#include <set>
#include <map>
using namespace std;

static char board[51][51];
static char b2[51][51];
static int N, K;

char get(int x, int y)
{
	if (x < 0 || y<0 ||x>=N || y>=N)
		return 0;
	return b2[x][y];
}

char *doA(char **&toks)
{
	N = atoi(*toks++);
	K = atoi(*toks++);
	memset(b2, 0, sizeof(b2));
	for (int i=0; i<N; i++)
	{
		char *s = *toks++;
		for (int j=0; j<N; j++)
		{
			char c = s[j];
			if (c=='.')
				board[j][i] = 0;
			else
				board[j][i] = c;
		}
	}
	for (int i=0; i<N; i++)
	{
		for (int j=0, k=0; j<N; j++)
		{
			if (board[N - j - 1][i])
			{
				b2[N-i-1][N-k-1] = board[N - j - 1][i];
				k++;
			}
		}
	}

	bool bB=false, bR=false;
	for (int i=0; i<N; i++)
	{
		for (int j=0; j<N; j++)
		{
			int dx[] = {1, 1, 0, 1};
			int dy[] = {0, 1, 1, -1};
			if (b2[i][j])
			{
				for (int ii=0; ii<4; ii++)
				{
					bool b=true;
					for (int k=0; k<K; k++)
					{
						if (get(i+dx[ii]*k, j+dy[ii]*k)!=b2[i][j])
							b = false;
					}
					if (b)
					{
						if (b2[i][j] == 'B')
							bB = true;
						else
							bR = true;
					}
				}
			}
		}
	}

	if (bB && bR)
		return "Both";
	if (bB)
		return "Blue";
	if (bR)
		return "Red";
	return "Neither";
}
