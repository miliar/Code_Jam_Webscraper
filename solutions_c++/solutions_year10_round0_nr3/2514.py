#include "iostream"
#include "fstream"
#include "vector"
using namespace std;

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
		unsigned long R,k,N;
		ip>>R>>k>>N;
		vector< unsigned long > groups, groupNext, groupTotal;
		for( unsigned long itr2 = 0; itr2 < N; ++itr2 )
		{
			unsigned long val;
			ip>>val;
			groups.push_back( val );
		}
		for( unsigned long itr3 = 0; itr3 < N; ++itr3 )
		{
			unsigned long total = 0;
			unsigned long index = itr3;
			int groupNextCount = 0;
			while( total < k )
			{
				if( total + groups[index] <= k )
				{
					total += groups[index];
					++index;
					++groupNextCount;
					if( index >= N )
						index = 0;
					if( index == itr3 )
						break;
				}
				else
					break;
			}
			groupNext.push_back( groupNextCount );
			groupTotal.push_back( total );
		}
		unsigned long finalCount = 0;
		unsigned long finalIndex = 0;
		for( unsigned long itr4 = 0; itr4 < R; ++itr4 )
		{
			finalCount += groupTotal[finalIndex];
			finalIndex += groupNext[finalIndex];
			finalIndex = finalIndex%N;
		}
		op<<"Case #"<<itr<<": "<<finalCount<<endl;
	}
	ip.close();
	op.close();
	return 0;
}