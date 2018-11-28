// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
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
using namespace std;

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

char *doB(char **&toks)
{
	static char buf[32768];
	int map[101][101][2];
	int alt[101][101];
	int H = atoi(*toks++);
	int W = atoi(*toks++);
	int sinks=0;
	for (int i=0; i<H; i++)
	{
		for (int j=0; j<W; j++)
		{
			alt[j][i] = atoi(*toks++);
			setVec2(map[j][i], j, i);
		}
	}
	for (int i=0; i<W; i++)
	{
		for (int j=0; j<H; j++)
		{
			int mn = alt[i][j];
			for (int k=0; k<4; k++)
			{
				int x2 = i + dx[k];
				int y2 = j + dy[k];
				if (x2>=0 && x2<W && y2>=0 && y2<H)
				{
					if (alt[x2][y2] < mn)
					{
						mn = alt[x2][y2];
						copyVec2(map[i][j], map[x2][y2]);
					}
				}
			}
			if (mn == alt[i][j])
				sinks++;
		}
	}
	char ret[101][101] = {0};
	char label = 'a';
	for (int j=0; j<H; j++)
	{
		for (int i=0; i<W; i++)
		{
			if (!ret[i][j])
			{
				// Find my sink
				int x=i, y=j;
				while ((map[x][y][0] != x || map[x][y][1] != y) && !ret[x][y] )
				{
					int x2 = map[x][y][0];
					y = map[x][y][1];
					x = x2;
				}
				char mylabel;
				if (ret[x][y])
					mylabel = ret[x][y];
				else
					mylabel = label++;

				x = i;
				y = j;
				while ((map[x][y][0] != x || map[x][y][1] != y) && !ret[x][y] )
				{
					ret[x][y] = mylabel;
					int x2 = map[x][y][0];
					y = map[x][y][1];
					x = x2;
				}
				ret[x][y] = mylabel;
			}
			buf[j*(W*2 + 1) + i*2+1] = ret[i][j];
			buf[j*(W*2 + 1) + i*2 + 1+1] = ' ';
		}
		buf[j*(W*2 + 1) + W*2+1] = '\n';
	}
	assert(sinks == label - 'a');
	buf[0] = '\n';
	buf[(W*2 + 1)* H] = '\0';
	return buf;
}

