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
#include "utilHashTable2.h"
#include <vector>
#include <set>
#include <map>
using namespace std;
#pragma warning(disable:4018)


char *doC(char **&toks)
{
	int R = atoi(*toks++);
	int board[102][102]={0};

	for (int i=0; i<R; i++)
	{
		int x1 = atoi(*toks++);
		int y1 = atoi(*toks++);
		int x2 = atoi(*toks++);
		int y2 = atoi(*toks++);
		for (int j=x1; j<=x2; j++)
		{
			for (int k=y1; k<=y2; k++)
			{
				board[j][k] = 1;
			}
		}
	}
	int ret=0;
	do 
	{
		bool alive=false;
		for (int i=0; i<102; i++)
		{
			for (int j=0; j<102; j++)
			{
				if (board[i][j])
					alive=true;
			}
		}
		if (!alive)
			break;
		int board2[102][102];
		memcpy(board2, board, sizeof(board));
		for (int i=1; i<102; i++)
		{
			for (int j=1; j<102; j++)
			{
				if (board2[i-1][j] && board2[i][j-1])
					board[i][j] = 1;
				else if (!board2[i-1][j] && !board2[i][j-1])
					board[i][j] = 0;
				else
					board[i][j] = board2[i][j];
			}
		}
		ret++;
	} while (true);

	static char buf[16384];
	sprintf(buf, "%d", ret);
	return buf;
}
