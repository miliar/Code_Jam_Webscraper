#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

template < class T>
T** array(int m, int n)
{
	T **p;
	p = (T**)malloc(m*sizeof(T*));
	if (p == NULL)
	{
		cout<<"Error: out of memory."<<endl;
		exit(1);
	}
	p[0] = (T*)malloc(m*n*sizeof(T));
	if (p[0] == NULL)
	{
		cout<<"Error: out of memory."<<endl;
		exit(1);
	}
	memset(p[0],0,m*n*sizeof(T));
	for (int i=1; i<m; ++i)
		p[i]=p[i-1]+n;
	return p;
}

template < class T>
void freearray(T** p)
{
	free(*p); free(p);
}

#define MAX 10000

vector< vector<int> > area;
int **arrExpanded;

bool isSink( int **arr, int x, int y )
{
	return (arr[x][y] <= arr[x-1][y]) && (arr[x][y] <= arr[x][y-1]) && (arr[x][y] <= arr[x+1][y]) && (arr[x][y] <= arr[x][y+1]);
}

//dir  0:North, 1:West, 2: East, 3: South
bool isFlowTo( int **arr, int x, int y, int dir )
{
	bool b = false;
	switch(dir)
	{
	case 0:
		b = (arr[x][y] < arr[x-1][y]) && (arr[x][y] < arr[x-2][y]) && (arr[x][y] < arr[x-1][y-1]) && (arr[x][y] < arr[x-1][y+1]);
		break;
	case 1:
		b = (arr[x][y] < arr[x][y-1]) && (arr[x][y] < arr[x-1][y-1]) && (arr[x][y] < arr[x][y-2]) && (arr[x][y] <= arr[x+1][y-1]);
		break;
	case 2:
		b = (arr[x][y] < arr[x+1][y]) && (arr[x][y] <= arr[x+1][y-1]) && (arr[x][y] <= arr[x+2][y]) && (arr[x][y] <= arr[x+1][y+1]);
	    break;
	case 3:
		b = (arr[x][y] < arr[x][y+1]) && (arr[x][y] < arr[x-1][y+1]) && (arr[x][y] <= arr[x+1][y+1]) && (arr[x][y] <= arr[x][y+2]);
	    break;
	default:
	    break;
	}
	return b;
}

void expandArea( int **arr, int Row, int Col, int x, int y, int iArea )
{
	if ( x > 1 && arrExpanded[x-1][y] == 0 && isFlowTo( arr, x, y, 0 ) )
	{
		int index = (x-2)*Col + y -1;
		if ( index < area[iArea][0] )
			area[iArea].insert( area[iArea].begin(), index );
		else
			area[iArea].push_back( index );
		arrExpanded[x-1][y] = 1;
		expandArea( arr, Row, Col, x-1, y, iArea );
	}
	if ( y > 1 && arrExpanded[x][y-1] == 0 && isFlowTo( arr, x, y, 1 ) )
	{
		int index = (x-1)*Col + y - 2;
		if ( index < area[iArea][0] )
			area[iArea].insert( area[iArea].begin(), index );
		else
			area[iArea].push_back( index );
		arrExpanded[x][y-1] = 1;
		expandArea( arr, Row, Col, x, y-1, iArea  );
	}
	if ( y < Col && arrExpanded[x][y+1] == 0 && isFlowTo( arr, x, y, 3 ) )
	{
		int index = (x-1)*Col + y;
		if ( index < area[iArea][0] )
			area[iArea].insert( area[iArea].begin(), index );
		else
			area[iArea].push_back( index );
		arrExpanded[x][y+1] = 1;
		expandArea( arr, Row, Col, x, y+1, iArea  );
	}
	if ( x < Row && arrExpanded[x+1][y] == 0 && isFlowTo( arr, x, y, 2 ) )
	{
		int index = x*Col +y - 1;
		if ( index < area[iArea][0] )
			area[iArea].insert( area[iArea].begin(), index );
		else
			area[iArea].push_back( index );
		arrExpanded[x+1][y] = 1;
		expandArea( arr, Row, Col, x+1, y, iArea  );
	}
}

int main()
{
	int nCase,nRow,nCol;

	ifstream ifs( "B-small.in" );
	ofstream ofs( "B-small-out.txt" );

	ifs >> nCase;
	for (int iCase = 0; iCase < nCase; iCase++ )
	{
		area.clear();
		ifs >> nRow >> nCol;
		int **arr = array<int>( nRow+2, nCol+2 );
		arrExpanded = array<int>( nRow+2, nCol+2 );
		memset( arr[0], MAX , (nRow+2)*(nCol+2)*sizeof(int) );
		for ( int iRow = 1; iRow <= nRow; iRow++ )
		{
			for ( int iCol = 1; iCol <= nCol; iCol++ )
			{
				ifs >> arr[iRow][iCol];
			}
		}
		//find all sinks.
		for ( int iRow = 1; iRow <= nRow; iRow++ )
		{
			for ( int iCol = 1; iCol <= nCol; iCol++ )
			{
				if ( isSink( arr, iRow, iCol) )
				{
					vector<int> v;
					v.push_back( (iRow-1)*nCol +iCol-1 );
					area.push_back(v);
				}
			}
		}
		int *sort = (int *)malloc(area.size()*sizeof(int));
		for ( int i = 0; i < area.size(); i++ )
		{
			sort[i] = i;
		}

		for ( int i = 0; i < area.size(); i++ )
		{
			int y = area[i][0]%nCol + 1;
			int x = (area[i][0]-y+1)/nCol + 1;

			memset(arrExpanded[0], 0, (nRow+2)*(nCol+2)*sizeof(int));
			arrExpanded[x][y] = 1;
			expandArea(arr, nRow, nCol, x, y, i );
		}
		//sort
		for ( int i = 0; i < area.size() - 1; i++ )
		{
			for ( int j = i+1; j< area.size(); j++ )
			{
				if ( area[ sort[i] ][0] > area[ sort[j] ][0] )
				{
					int tmp = sort[i];
					sort[i] = sort[j];
					sort[j] = tmp;
				}
			}
		}

		//set matrix
		for ( int i = 0; i < area.size(); i++ )
		{
			for ( int j = 0; j< area[i].size(); j++ )
			{
				int y = area[i][j]%nCol + 1;
				int x = (area[i][j]-y+1)/nCol + 1;
				arr[x][y] = sort[i];
			}
		}

		//output
		ofs<<"Case #"<<iCase+1<<":"<<endl;
		printf("Case #%d:\n",iCase+1);
		for ( int iRow = 1; iRow <= nRow; iRow++ )
		{
			for ( int iCol = 1; iCol <= nCol; iCol++ )
			{
				char ch = 'a' + arr[iRow][iCol];
				ofs<<ch;
				if (iCol!=nCol)
					ofs<<" ";
				printf("%c ",ch);
			}
			printf("\n");
			ofs<<endl;
		}
		freearray(arr);
		freearray(arrExpanded);
	}

	ifs.close();
	ofs.close();
	return 0;
}    