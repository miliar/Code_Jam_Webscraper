#include <iostream>
#include <fstream>
using namespace std;
#define DATA_INPUT "B-large.in"
#define DATA_OUTPUT "B-large.out"

#define M(X,Y) map[ (W + 2) * ((X) + 1) + ((Y) + 1)]
#define C(X,Y) cmap[ W * (X) + (Y)]

int nmoves;
struct sink
{
	int mark;
	int h;
	int w;
	int mass;
	sink *next;
};


__inline int getSmallest( int *map, int x, int y, int H, int W)
{
	if ( M(x-1,y) < M(x,y) && M(x-1,y) <= M(x+1,y) && M(x-1,y) <= M(x,y-1) && M(x-1,y) <= M(x,y+1))
		return -2; // N
	if ( M(x,y-1) < M(x,y) && M(x,y-1) <= M(x+1,y) && M(x,y-1) <= M(x-1,y) && M(x,y-1) <= M(x,y+1))
		return -1; // W
	if ( M(x,y+1) < M(x,y) && M(x,y+1) <= M(x+1,y) && M(x,y+1) <= M(x-1,y) && M(x,y+1) <= M(x,y-1))
		return 1; // E
	if ( M(x+1,y) < M(x,y) && M(x+1,y) <= M(x-1,y) && M(x+1,y) <= M(x,y-1) && M(x+1,y) <= M(x,y+1))
		return 2; // S
	return 0; //sink
}

__inline void rollBackMarks ( int *cmap, int *moves, int nmoves, int oldmark, int x, int y, int H, int W)
{
	C(x,y) = oldmark;
	if (nmoves == 0) 
		return;
	if ( moves[ nmoves-1] == -2 )
	{
		rollBackMarks ( cmap, moves, nmoves - 1, oldmark, x + 1, y, H, W);
		return;
	}
	if ( moves[ nmoves-1] == -1 )
	{
		rollBackMarks ( cmap, moves, nmoves - 1, oldmark, x, y + 1, H, W);
		return;
	}
	if ( moves[ nmoves-1] == 1 )
	{
		rollBackMarks ( cmap, moves, nmoves - 1, oldmark, x, y - 1, H, W);
		return;
	}
	rollBackMarks ( cmap, moves, nmoves - 1, oldmark, x - 1, y, H, W);
	return;
}

__inline int scanChain ( int *map, int *cmap, int *moves, int x, int y, int H, int W, int mark)
{	
	int smallest = getSmallest (map, x, y, H, W);
	if (smallest == 0)
	{
		C(x,y) = mark;
		return mark + 1;
	}
	if (smallest == -2)
	{
		if ( C(x-1,y) == 0)
		{
			moves[ nmoves++] = -2;
			C(x,y) = mark;
			return scanChain ( map, cmap, moves, x - 1, y, H, W, mark);
		}
		if ( C(x-1,y) != 0)
		{
			rollBackMarks ( cmap, moves, nmoves, C(x-1,y), x, y, H, W);
			return mark;
		}	
	}
	if (smallest == -1)
	{
		if ( C(x,y-1) == 0)
		{
			moves[ nmoves++] = -1;
			C(x,y) = mark;
			return scanChain ( map, cmap, moves, x, y - 1, H, W, mark);
		}
		if ( C(x,y-1) != 0)
		{
			rollBackMarks ( cmap, moves, nmoves, C(x,y-1), x, y, H, W);
			return mark;
		}	
	}
	if (smallest == 1)
	{
		if ( C(x,y+1) == 0)
		{
			moves[ nmoves++] = 1;
			C(x,y) = mark;
			return scanChain ( map, cmap, moves, x, y + 1, H, W, mark);
		}
		if ( C(x,y+1) != 0)
		{
			rollBackMarks ( cmap, moves, nmoves, C(x,y+1), x, y, H, W);
			return mark;
		}	
	}
	if ( C(x+1,y) == 0)
	{
		moves[ nmoves++] = 2;
		C(x,y) = mark;
		return scanChain ( map, cmap, moves, x + 1, y, H, W, mark);
	}
	else
	{
		rollBackMarks ( cmap, moves, nmoves, C(x+1,y), x, y, H, W);
		return mark;
	}	

}

int main ()
{
	int N, H, W;
	int *map;
	int *cmap;
	int moves[10000];
	fstream fin, fout;
	fin.open ( DATA_INPUT, fstream::in);
	fout.open ( DATA_OUTPUT, fstream::out);
	
	fin >> N;

	for ( int i = 0; i < N; i++ )
	{
		fin >> H;
		fin >> W;
		map = new int [ (H + 2)* (W + 2)];
		cmap = new int [ H * W];		 
		for ( int j = 0; j < (H+2)*(W+2); j++)
			map [j] = 10001;
		for ( int j = 0; j < H; j++)
			for ( int o = 0; o < W; o++)
			{
				fin >> M(j,o);
				C(j,o) = 0;
			}
		int mark = 1;
		for ( int j = 0; j < H; j++)
		{			
			for ( int o = 0; o < W; o++)
			{
				if ( C(j,o) == 0) 
				{
					nmoves = 0;
					mark = scanChain ( map, cmap, moves, j, o, H, W, mark);
				}
			}
		}
		fout << "Case #" << i + 1 << ":\n";
		for ( int j = 0; j < H; j++)
		{
			for ( int o = 0; o < W; o++)		
			{
				fout << (char)('a' + C(j,o) - 1)<< " ";
			}
			fout << endl;
		}

		delete [] map;
		delete [] cmap;
	}

	fout.close ( );
	fin.close ( );
	return 0;
}