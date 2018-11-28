#include "iostream"
#include "fstream"
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
		int N, K;
		ip>>N>>K;

		{
			int max = (1<<N);
			K = K%max;

			if( max-1 == K )
				op<<"Case #"<<itr<<": ON"<<endl;
			else
				op<<"Case #"<<itr<<": OFF"<<endl;
		}
	}
	ip.close();
	op.close();
	return 0;
}