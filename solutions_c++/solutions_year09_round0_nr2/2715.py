#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <string.h>
#include <assert.h>

char *ids = "abcdefghijklmnopqrstuvwxyz";
int curID = 0;

char *nextId() {
	assert(curID < strlen(ids));
	return &(ids[curID++]);
}

enum EFlow {
	eFlowNone,
	eFlowNorth,
	eFlowSouth,	
	eFlowEast,
	eFlowWest
};

EFlow opFlow(EFlow f)
{
	switch(f)
	{
		default:
			return eFlowNone;
		case eFlowNorth:
			return eFlowSouth;
		case eFlowSouth:
			return eFlowNorth;
		case eFlowEast:
			return eFlowWest;
		case eFlowWest:
			return eFlowEast;
	}
}

class CCell {

public:
	CCell() { id = NULL; flow = eFlowNone; }

	EFlow flow;

	inline bool isSink() { return flow == eFlowNone; }

	int alt;
	char *id;
	
	int i, j;
};

int w, h;
CCell *cells;

int nextSink = 0;
CCell *sinks[27];

CCell *getCell(int i, int j)
{
	if(i >= w || i < 0) return NULL;
	if(j >= h || j < 0) return NULL;
	
	return &(cells[(j * w) + i]);
}

void updateFlow(int i, int j)
{
	CCell *c = getCell(i, j);
	
	if(c->flow != eFlowNone) return;
	if(!(c->flow == eFlowNone && c->id == NULL)) return;
	
	CCell *north = getCell(i, j - 1);
	CCell *south = getCell(i, j + 1);
	CCell *east = getCell(i + 1, j);
	CCell *west = getCell(i - 1, j);
	
	EFlow dir = eFlowNone;
	int minAlt = c->alt;

	if(north && north->alt < minAlt)
	{
		minAlt = north->alt;
		dir = eFlowNorth;
	}
	
	if(west && west->alt < minAlt)
	{
		minAlt = west->alt;
		dir = eFlowWest;
	}
	
	if(east && east->alt < minAlt)
	{
		minAlt = east->alt;
		dir = eFlowEast;
	}
	
	if(south && south->alt < minAlt)
	{
		minAlt = south->alt;
		dir = eFlowSouth;
	}
	
	c->flow = dir;
}

void updateID(CCell *c)
{
	assert(c == getCell(c->i, c->j));

	int i = c->i;
	int j = c->j;
	
	CCell *north = getCell(i, j - 1);
	CCell *south = getCell(i, j + 1);
	CCell *east = getCell(i + 1, j);
	CCell *west = getCell(i - 1, j);
	
	if(c->flow == eFlowNone)
	{	
		c->id = nextId();
	}
	else
	{
		switch(c->flow)
		{
			case eFlowNorth:
				assert(north);
				if(!(north->id)) updateID(north);
				c->id = north->id;
				break;
			case eFlowSouth:
				assert(south);
				if(!(south->id)) updateID(south);
				c->id = south->id;
				break;
			case eFlowEast:
				assert(east);
				if(!(east->id)) updateID(east);
				c->id = east->id;
				break;
			case eFlowWest:
				assert(west);
				if(!(west->id)) updateID(west);
				c->id = west->id;
				break;
		}
	}
/*	
	if(north && north->flow == opFlow(eFlowNorth))
	{
		north->id = c->id;
		updateID(north);
	}
	
	if(west && west->flow == opFlow(eFlowWest))
	{
		west->id = c->id;
		updateID(west);
	}
	
	if(east && east->flow == opFlow(eFlowEast))
	{
		east->id = c->id;
		updateID(east);
	}
	
	if(south && south->flow == opFlow(eFlowSouth))
	{
		south->id = c->id;
		updateID(south);
	}
*/

}

int main()
{
	int nMaps;
	
	FILE *in = fopen("B-small.in", "r");
	fscanf(in, "%d", &nMaps);
	
	int map = 0;
	while(map < nMaps)
	{
		fscanf(in, "%d %d", &h, &w);
		
		cells = new CCell[w * h];
		curID = 0;		
		memset(sinks, 0, sizeof(sinks));
		
		for(int j = 0; j < h; j++)
		{
			for(int i = 0; i < w; i++)
			{
				CCell *next = getCell(i, j);
				fscanf(in, "%d ", &(next->alt));
				next->i = i;
				next->j = j;
			}
		}
		
		// Do stuff here
		nextSink = 0;
		for(int j = 0; j < h; j++)
		{
			for(int i = 0; i < w; i++)
			{
				updateFlow(i, j);
			}
		}
		
		for(int j = 0; j < h; j++)
		{
			for(int i = 0; i < w; i++)
			{
				CCell *c = getCell(i, j);
				if(!(c->id)) updateID(c);
			}
		}
		
		printf("Case #%d:\n", ++map);
		for(int j = 0; j < h; j++)
		{
			for(int i = 0; i < w; i++)
			{
				CCell *next = getCell(i, j);
				printf("%c ", *(next->id));
			}
			printf("\n");
		}
		
		delete [] cells;
	}
}
