#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

const int HMAX = 110, WMAX = HMAX, CELLS_MAX = HMAX*WMAX+1, BASINS_MAX = 128;

struct Cell
{
	int h;
	int basin;
	// where it will fall
	int iTo;
	int jTo;
};

Cell field[HMAX][WMAX];

struct CellPos
{
	int i, j;
	bool operator< (const CellPos &that) const
	{
		return field[i][j].h < field[ that.i ][ that.j ].h;
	}
};

CellPos cellPositions[CELLS_MAX];
char basinLetter[BASINS_MAX];

int h, w;
int numCells;

void input()
{
	cin >> h >> w;
	numCells = 0;
	for(int i=0; i<h; i++)
	{
		for(int j=0; j<w; j++)
		{
			cin >> field[i][j].h;
			field[i][j].basin = 0;
			cellPositions[numCells].i=i;
			cellPositions[numCells].j=j;
			numCells++;
		}
	}
	assert( numCells == w*h );
	std::sort( cellPositions, cellPositions+numCells );
}

//bool willFall(int i1, int j1, int i2, int j2)
//{
//	if( i1<0 || i1>=h ) return false;
//	if( i2<0 || i2>=h ) return false;
//	if( j1<0 || j1>=w ) return false;
//	if( j2<0 || j2>=w ) return false;
//	// will 2 fall to 1?
//
//}

void dfsMark(int i, int j, int b);

bool markIfCan(int i, int j, int iTo, int jTo, int b)
{
	if( iTo<0 || iTo>=h || jTo<0 || jTo>=w ) return false;
	if( field[iTo][jTo].iTo==i && field[iTo][jTo].jTo==j )
	{
		dfsMark(iTo,jTo,b);
		return true;
	}
	return false;
}

void dfsMark(int i, int j, int b)
{
	if( field[i][j].basin )
	{
		cout << '?';
		return;
	}
	field[i][j].basin = b;

	markIfCan(i,j,i-1,j,b);
	markIfCan(i,j,i+1,j,b);
	markIfCan(i,j,i,j-1,b);
	markIfCan(i,j,i,j+1,b);
}

void tryFall(int &curBest, int iTo, int jTo, int &iBest, int &jBest)
{
	if( iTo<0 || iTo>=h || jTo<0 || jTo>=w ) return;
	if( field[iTo][jTo].h < curBest )
	{
		curBest = field[iTo][jTo].h;
		iBest = iTo;
		jBest = jTo;
	}
}



void solve()
{
	// find where each cell falls to
	for(int i=0; i<h; i++)
	{
		for(int j=0; j<w; j++)
		{
			field[i][j].iTo = i;
			field[i][j].jTo = j;

			int curBest = field[i][j].h;
			int iBest, jBest;

			tryFall(curBest, i-1, j,iBest, jBest);
			tryFall(curBest, i, j-1,iBest, jBest);
			tryFall(curBest, i, j+1,iBest, jBest);
			tryFall(curBest, i+1, j,iBest, jBest);

			if( curBest != field[i][j].h )
			{
				field[i][j].iTo = iBest;
				field[i][j].jTo = jBest;
			}
		}
	}

	// show falls
	//for(int i=0; i<h; i++)
	//{
	//	for(int j=0; j<w; j++)
	//	{
	//		if( field[i][j].jTo==j )
	//		{
	//			if( field[i][j].iTo == i-1 )
	//			{
	//				cout << "^";
	//			}
	//			if( field[i][j].iTo == i+1 )
	//			{
	//				cout << "v";
	//			}
	//		}
	//		if( field[i][j].iTo==i )
	//		{
	//			if( field[i][j].jTo == j-1 )
	//			{
	//				cout << "<";
	//			}
	//			if( field[i][j].jTo == j+1 )
	//			{
	//				cout << ">";
	//			}
	//		}
	//		if( field[i][j].jTo==j && field[i][j].iTo==i )
	//		{
	//			cout << ".";
	//		}
	//		cout << " ";
	//	}
	//	cout << endl;
	//}
	//cout << endl;

	//mark basins
	int basinStep = 1;

	for(int id=0; id<numCells; id++)
	{
		int i = cellPositions[id].i;		
		int j = cellPositions[id].j;
		if( field[i][j].basin==0 )
		{
			//mark all in this basin
			dfsMark(i,j,basinStep);
		}
		basinStep++;
	}

	for(int i=0;i<BASINS_MAX;i++)
	{
		basinLetter[i] = 0;
	}

	char letter = 'a';
	// choose letters
	for(int i=0; i<h; i++)
	{
		for(int j=0; j<w; j++)
		{
			if( basinLetter[ field[i][j].basin ] == 0 )
			{
				basinLetter[ field[i][j].basin ] = letter++;
			}
		}
	}
	assert( letter-1<='z' );

	
	// output
	for(int i=0; i<h; i++)
	{
		for(int j=0; j<w; j++)
		{
			cout << basinLetter[ field[i][j].basin ] << " ";
		}
		cout << "\n";
	}
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int numTests;
	cin >> numTests;
	for(int iTest = 0; iTest < numTests; iTest++)
	{
		input();
		cout << "Case #" << 1+iTest << ":\n";
		solve();
	}
	cout.flush();
	return 0;
}