#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "map"
#include "algorithm"
using namespace std;

#define SIZE 501

void Nullify( int row, int col, int size, vector< vector<int> >&refbark  )
{
	for( int rowiter = 0; rowiter < size; ++rowiter )
		for( int coliter = 0; coliter < size; ++coliter )
			refbark[row+rowiter][col+coliter] = -1;
}

bool Check( int row, int col, int size, const vector< vector<int> >&refbark )
{
	for( int rowiter = 0; rowiter < size; ++rowiter )
		for( int coliter = 0; coliter < size; ++coliter )
		{
			if( rowiter == size-1 )
			{
				if( -1 == refbark[row+rowiter][col+coliter] )
					return false;
			}
			else if ( coliter == size-1 )
			{
				if( -1 == refbark[row+rowiter][col+coliter] )
					return false;
			}
			else
			{
				if( -1 == refbark[row+rowiter][col+coliter] )
					return false;
				if( refbark[row+rowiter][col+coliter] == refbark[row+rowiter][col+coliter+1] )
					return false;
				if( refbark[row+rowiter][col+coliter] == refbark[row+rowiter+1][col+coliter] )
					return false;
				if( refbark[row+rowiter][col+coliter] != refbark[row+rowiter+1][col+coliter+1] )
					return false;
			}
		}
		return true;
}

int main()
{
	ifstream ip( "A-small.in" );
	ofstream op( "A-small.out" );
	if( !ip )
	{
		cout<<"Cant open input"<<endl;
		return 1;
	}
	if( !op )
	{
		cout<<"Cant open output"<<endl;
		return 1;
	}

	int count;
	ip>>count;

	for( int itr = 1; itr <= count; ++itr )
	{
		int M,N;
		ip>>M>>N;
		vector< vector<int> > bark;
		for( int rowitr = 0; rowitr < M; ++rowitr )
		{
			vector<int> rowbark;
			int chars = N>>2;
			for( int colitr = 0; colitr < chars; ++colitr )
			{
				char ch;
				ip>>ch;
				int val;
				switch( ch )
				{
				case 'A':
					val = 10;
					break;
				case 'B':
					val = 11;
					break;
				case 'C':
					val = 12;
					break;
				case 'D':
					val = 13;
					break;
				case 'E':
					val = 14;
					break;
				case 'F':
					val = 15;
					break;
				default:
					val = ch;
				}
				for( int bits = 3; bits >= 0; --bits )
					rowbark.push_back( (val & 1<<bits) ? 1 : 0 );
			}
			bark.push_back( rowbark );
		}
		map< int, int > count;
		int minval = min( M, N );
		vector< int > sizes;
		for( int sizeiter = minval; sizeiter > 0; --sizeiter )
		{
			for( int rowiter = 0; rowiter <= M - sizeiter ; ++rowiter )
			{
				for( int coliter = 0; coliter <= N - sizeiter ; ++coliter )
				{
					if( Check( rowiter, coliter, sizeiter, bark ) )
					{
						Nullify( rowiter, coliter, sizeiter, bark  );
						map< int, int >::iterator mapitr = count.find( sizeiter );
						if( mapitr == count.end() )
						{
							sizes.push_back( sizeiter );
							count[ sizeiter ] = 1;
						}
						else
							++count[ sizeiter ];
					}
				}
			}
		}
		op<<"Case #"<<itr<<": "<<sizes.size()<<endl;
		vector<int>::iterator begin = sizes.begin();
		vector<int>::iterator end = sizes.end();
		for( int resultiter =0; resultiter < sizes.size(); ++resultiter )
			op<<sizes[resultiter]<<" "<<count[sizes[resultiter]]<<endl;
	}
	ip.close();
	op.close();
	return 0;
}