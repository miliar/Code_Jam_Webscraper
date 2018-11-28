#include "iostream"
#include "fstream"
#include "vector"
#include "string"
#include "map"
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
		int N;
		ip>>N;
		vector<float> Coeff,offset;
		for( int points = 0; points < N; ++points )
		{
			int y1, y2;
			ip>>y1>>y2;
			Coeff.push_back((y2 - y1));
			offset.push_back(y1);
		}
		long long retval = 0;
		for( int iteration1 = 0; iteration1 < N; ++iteration1 )
		{
			for( int iteration2 = iteration1 + 1; iteration2 < N; ++iteration2 )
			{
				if( (Coeff[iteration1] - Coeff[iteration2]) )
				{
					float x = -(offset[iteration1]-offset[iteration2])/(Coeff[iteration1] - Coeff[iteration2]);
					if( x >= 0 && x <= 1 )
						++retval;
				}
			}
		}
		op<<"Case #"<<itr<<": "<<retval<<endl;
	}
	ip.close();
	op.close();
	return 0;
}