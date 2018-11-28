#include <stdio.h>
#include <map>
#include <assert.h>

#include "BinaryHeap.h"

using namespace std;

#define BUR_LEN		1024
#define MAX_HEIGHT	100
#define MAX_WIDTH	100
#define EMPTY_LABEL	0
#define DirNum		4
#define MAX_LABEL	'z'
#define MIN_LABEL	'a'

typedef struct _MapNode
{
	int altitude;
	char label;
}MapNode;

typedef struct
{
	int x,y;
}MyPoint;

const MyPoint g_dirs[DirNum] = {{0,-1},{-1,0},{1,0},{0,1}};

MapNode g_mapIn[MAX_HEIGHT][MAX_WIDTH];
BinaryHeap<int,MyPoint> g_mapHeap;
int g_height, g_width;
char g_nextLabel;

char MakeLabelImpl(const MyPoint &pt)
{
	int i, iRec, al;
	MyPoint newPt;

	iRec = -1;
	al = g_mapIn[pt.y][pt.x].altitude;
	for( i=0;i<DirNum;i++ )
	{
		newPt.x = pt.x + g_dirs[i].x;
		newPt.y = pt.y + g_dirs[i].y;
		if( newPt.y>=0 && newPt.y<g_height && newPt.x>=0 && newPt.x<g_width 
			&& g_mapIn[newPt.y][newPt.x].altitude<al)
		{
			iRec = i;
			al = g_mapIn[newPt.y][newPt.x].altitude;
		}
	}
	if( iRec<0 )
	{
		g_nextLabel ++;
		assert( g_nextLabel<=MAX_LABEL+1 );
		return g_nextLabel-1;
	}
	else
	{
		newPt.x = pt.x + g_dirs[iRec].x;
		newPt.y = pt.y + g_dirs[iRec].y;
		if( g_mapIn[newPt.y][newPt.x].label==EMPTY_LABEL )
		{
			g_mapIn[newPt.y][newPt.x].label =  MakeLabelImpl(newPt);
		}
		return g_mapIn[newPt.y][newPt.x].label;
	}
}

void MakeLabel( )
{
	MyPoint pt;
	int al;
	while( !g_mapHeap.IsEmpty() )
	{
		g_mapHeap.ExtractMin( &al,&pt );
		if( g_mapIn[pt.y][pt.x].label==EMPTY_LABEL )
			g_mapIn[pt.y][pt.x].label = MakeLabelImpl(pt);
	}
}

void Relabel()
{
	static const int numLabel = MAX_LABEL-MIN_LABEL+1;
	static char newLabel[numLabel];
	int i,j, ti;
	char nextLabel = MIN_LABEL;

	memset( newLabel,0,numLabel*sizeof(char) );
	for( i=0;i<g_height;i++ )
	{
		for( j=0;j<g_width;j++ )
		{
			ti = g_mapIn[i][j].label-MIN_LABEL;
			if( newLabel[ti] ) g_mapIn[i][j].label = newLabel[ti];
			else
			{
				newLabel[ti] = g_mapIn[i][j].label = nextLabel;
				nextLabel ++;
			}
		}
	}
}

void WaterSheds()
{
	FILE *fin, *fout;
	fin = fopen( "in.txt", "r" );
	fout = fopen( "out.txt", "w" );
	assert( fin && fout );

	int t;
	int k, tmp;
	MyPoint pt;
//	char buf[BUR_LEN];

	fscanf( fin,"%d", &t );
	for( k=0;k<t;k++ )
	{
		fscanf( fin,"%d %d", &g_height,&g_width );
		for( pt.y=0;pt.y<g_height;pt.y++ )
		{
			for( pt.x=0;pt.x<g_width;pt.x++ )
			{
				fscanf( fin, "%d", &tmp ); 
				g_mapIn[pt.y][pt.x].altitude = tmp;
				g_mapIn[pt.y][pt.x].label = EMPTY_LABEL;
				g_mapHeap.Insert( tmp,pt );
			}
		}

		g_nextLabel = MIN_LABEL;
		MakeLabel();
		Relabel();

		fprintf( fout,"Case #%d:\n", k+1 );
		for( pt.y=0;pt.y<g_height;pt.y++ )
		{
			for( pt.x=0;pt.x<g_width;pt.x++ )
			{
				fprintf( fout, "%c ", g_mapIn[pt.y][pt.x].label );
			}
			fprintf( fout,"\n" );
		}
	}
}

int main()
{
	WaterSheds();
	return 0;
}