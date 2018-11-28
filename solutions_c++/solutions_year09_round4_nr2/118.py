// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
#include "utilUtils.h"
#include "utilFile.h"
#include "utilString.h"
#include "utilHashTable.h"
#include "assert.h"
#include "utilArray.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "utilRand.h"
#include <vector>
using namespace std;

int R, C, F;

typedef struct State
{
	int state[50][50];
	char key[3000];
	int x, y;
	int digs;
	void makeKey()
	{
		int p=0;
		for (int i=0; i<R; i++)
		{
			for (int j=0; j<C; j++)
			{
				key[p++] = state[i][j]?'#':'.';
			}
			key[p++] = '\n';
		}
		key[p++] = '0' + (x/10);
		key[p++] = '0' + (x%10);
		key[p++] = '\n';
		key[p++] = '0' + (y/10);
		key[p++] = '0' + (y%10);
		key[p++] = 0;
	}
} State;

HashTable *htVisited;
void addit(State ***arr, State *s)
{
	void *dummy;
	s->makeKey();
	if (!hashtableFind(&htVisited, s->key, &dummy))
	{
		State *sc = callocStruct(State);
		*sc = *s;
		arrayPush(arr, sc);
		hashtableAdd(&htVisited, sc->key, (void*)1);
	}
}

char *doB(char **&toks)
{
	R = atoi(*toks++);
	C = atoi(*toks++);
	F = atoi(*toks++);
	State *s1 = callocStruct(State);
	for (int i=0; i<R; i++)
	{
		char *s=*toks++;
		for (int j=0; j<C; j++, s++)
		{
			s1->state[i][j] = (*s=='#');
		}
	}
	s1->x = 0;
	s1->y = 0;
	s1->digs = 0;
#if 0
	for (int r=0; r<R-1; r++)
	{
		// Walk
		for (int c=0; c<C; c++)
		{
			if (state[r][c]>=0)
			{
				int newcost = state[r][c];
				// we got here somehow, escape to neighbors
				for (int dx=-1; dx<=1; dx+=2)
				{
					for (int i=1; i<C; i++)
					{
						int nc = c + i*dx;
						if (nc<0 || nc>=C)
							break;
						if (!solid[r][nc])
						{
							// We can move there
							if (!solid[r+1][nc])
							{
								// We fall
								int h=0;
								int j;
								for (j=r+1; j<R; j++)
								{
									if (solid[j][nc])
										break;
									h++;
								}
								if (h>F)
									break; // would die
								if (state[r+h][nc] == -1 || newcost < state[r+h][nc])
									state[r+h][nc] = newcost;
								break;
							} else {
								if (state[r][nc]==-1 || newcost < state[r][nc])
									state[r][nc] = newcost; // got there faster
							}
						} else {
							break;
						}
					}
				}
			}
		}
		// Dig
		for (int c=0; c<C; c++)
		{
			if (state[r][c]>=0)
			{
				int newcost=state[r][c]+1;
				for (int dx=-1; dx<=1; dx+=2)
				{
					int nc = c + dx;
					if (nc<0 || nc>=C)
						break;
					if (!solid(
				}
			}
		}

	}

	int ret=-1;
	for (int i=0; i<C; i++)
	{
		if (state[R-1][i]!=-1)
		{
			if (ret==-1 || state[R-1][i] < ret)
				ret = state[R-1][i];
		}
	}
#endif

	htVisited = hashtableCreate(100, 0);
	State **todoNow=NULL;
	State **todoNext=NULL;
	addit(&todoNow, s1);

	while (true)
	{
		int digs=-1;
		while (arraySize(&todoNow))
		{
			State *s = (State*)arrayPop(&todoNow);
			if (digs==-1)
				digs = s->digs;
			assert(digs == s->digs);
			if (s->y == R-1)
			{
				static char buf[1024];
				sprintf(buf, "Yes %d", s->digs);
				return buf;
			}
			State s2;
			// Walking
			for (int dx=-1; dx<=1; dx+=2)
			{
				s2 = *s;
				s2.x += dx;
				if (s2.x<0 || s2.x>=C)
					continue;
				if (s2.state[s2.y][s2.x])
					continue;
				if (!s2.state[s2.y+1][s2.x])
				{
					// We fall
					int h=0;
					int j;
					for (j=s2.y+1; j<R; j++)
					{
						if (s2.state[j][s2.x])
							break;
						h++;
					}
					if (h>F)
						continue; // would die
					s2.y += h;
					addit(&todoNow, &s2);

				} else {
					// Walk, valid
					addit(&todoNow, &s2);
				}
			}
			// Digging
			for (int dx=-1; dx<=1; dx+=2)
			{
				s2 = *s;
				int digx = s2.x + dx;
				if (digx<0 || digx>=C)
					continue;
				if (s2.state[s2.y][digx])
					continue;
				if (s2.state[s2.y+1][digx])
				{
					// Dig
					s2.digs++;
					s2.state[s2.y+1][digx] = 0;
					addit(&todoNext, &s2);
				}
			}
		}
		if (!arraySize(&todoNext))
			return "No";
		State **temp = todoNow;
		todoNow = todoNext;
		todoNext = temp;
	}
}
