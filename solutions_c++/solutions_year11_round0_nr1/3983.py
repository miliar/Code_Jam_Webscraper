#include <algorithm>
#include <fstream>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int main()
{
	ifstream inf ("A.in");
	ofstream outf ("A.out");
	
	int it, T;
		
	inf >> T;
	
	for ( it = 0; it < T; ++it )
	{
		int i, N, X, SO = 1, SB = 1, K = 0;
		char C;
		bool Psh = true;
		queue < int > Orange, Blue;
		queue < char > Who;
		
		inf >> N;
		for ( i = 0; i < N; ++i )
		{
			inf >> C >> X;
			Who.push( C );
			( C == 'O' ) ? ( Orange.push( X ) ) : ( Blue.push( X ) );
		}
		
		while ( !Who.empty() )
		{
			
			if ( !Blue.empty() )
			{
				if ( SB != Blue.front() )
					( Blue.front() > SB ) ? ( ++SB ) : ( --SB );
				else if ( Who.front() == 'B' )
				{
					Blue.pop();
					Who.pop();
					Psh = false;
				}
			}
				
			if ( !Orange.empty() )
			{
				if ( SO != Orange.front() )
					( Orange.front() > SO ) ? ( ++SO ) : ( --SO );
				else if ( Who.front() == 'O' && Psh )
				{
					Orange.pop();
					Who.pop();
				}
			}		

			++K;
			Psh = true;
		}
				
		outf << "Case #" << it + 1 << ": " << K << endl;
			
	}

	return 0;
}
