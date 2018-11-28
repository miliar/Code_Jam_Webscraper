#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

int main()
{
	ifstream inf ("B.in");
	ofstream outf ("B.out");
	int T, it;
	
	inf >> T;
	
	for ( it = 1; it <= T; ++it )
	{
		map < char, map < char, bool > > Opp;
		map < char, map < char, char > > NB;
		vector < char > ST;
		vector < char > :: reverse_iterator cit;
		int x, C, D, N, L;
		char K1, K2, K3, Z;
		bool F;
		
		inf >> C;
		for ( x = 0; x < C; ++x )
		{
			inf >> K1 >> K2 >> K3;
			NB[K1][K2] = NB[K2][K1] = K3;
		}
		
		inf >> D;
		for ( x = 0; x < D; ++x )
		{
			inf >> K1 >> K2;
			Opp[K1][K2] = Opp[K2][K1] = true;
		}
		
		inf >> N;
		for ( x = 0; x < N; ++x )
		{
			F = false;
			inf >> Z;
			while ( !ST.empty() && NB[ ST.back() ][ Z ] )
			{
				Z = NB[ ST.back() ][ Z ];
				ST.erase( ST.end() - 1 );					
			}
			for ( cit = ST.rbegin(); cit != ST.rend(); ++cit ) 
				if( Opp[ *cit ][ Z ] )
				{
					ST.erase( ST.begin(), ST.end() );
					F = true;
					break;
				}
			if ( !F )
				ST.push_back( Z );
		}
		
		L = ST.size();
		outf << "Case #" << it << ": [";
		if ( !ST.empty() )
			outf << ST[0];
		for ( x = 1; x < L; ++x )
			outf << ", " << ST[x];
		outf << "]" << endl;
		
	}

	return 0;
}
