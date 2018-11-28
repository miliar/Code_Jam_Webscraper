#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "map"
#include "algorithm"
using namespace std;

#define SIZE 501

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
		int R;
		ip>>R;
		vector<int> x1vec, x2vec, y1vec, y2vec;
		int maxX = 0, maxY = 0;
		for( int rows = 0; rows < R; ++rows )
		{
			int x1, x2, y1, y2;
			ip>>x1>>y1>>x2>>y2;
			maxX = max( maxX, x2 );
			maxY = max( maxY, y2 );
			x1vec.push_back( x1 );
			x2vec.push_back( x2 );
			y1vec.push_back( y1 );
			y2vec.push_back( y2 );
		}
		
		vector<int> initialRow( maxX, 0 );
		vector< vector<int> > initial( maxY, initialRow );

		int bacteriaCount = 0;
		for( int rows1 = 0; rows1 < R; ++rows1 )
		{
			for( int rowiter = y1vec[rows1]-1; rowiter < y2vec[rows1]; ++rowiter )
				for( int coliter = x1vec[rows1]-1; coliter < x2vec[rows1]; ++coliter )
				{
					if( 1 != initial[rowiter][coliter] )
					{
						++bacteriaCount;
						initial[rowiter][coliter] = 1;
					}
				}
		}
		int retval = 0;
		while( bacteriaCount )
		{
			vector<vector<int> > backup = initial;
			++retval;

			int rowsize = initial.size();
			int colsize = initial[0].size();
			for( int rowiter = 0; rowiter < rowsize; ++rowiter )
			{
				for( int coliter = 0; coliter < colsize; ++coliter )
				{
					if( ( 0 == rowiter ) || ( 0 == coliter ) )
					{
						if( initial[rowiter][coliter] )
						{
							--bacteriaCount;
							backup[rowiter][coliter] = 0;
						}
					}
					else
					{
						if( initial[rowiter-1][coliter] && initial[rowiter][coliter-1] )
						{
							if( !initial[rowiter][coliter] )
							{
								++bacteriaCount;
								backup[rowiter][coliter] = 1;
							}
						}
						if( initial[rowiter-1][coliter] || initial[rowiter][coliter-1] )
						{
							;//do nothing
						}
						else
						{
							if( initial[rowiter][coliter] )
							{
								--bacteriaCount;
								backup[rowiter][coliter] = 0;
							}
						}
					}
				}
			}
		initial = backup;
		}

		op<<"Case #"<<itr<<": "<<retval<<endl;
	}
	ip.close();
	op.close();
	return 0;
}