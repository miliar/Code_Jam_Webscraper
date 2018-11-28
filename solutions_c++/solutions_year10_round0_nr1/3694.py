#include <cmath>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin( "A-large.in" );
	ofstream fout( "A-large.out" );

	int t, n, k, i, a;
	fin >> t;
	for ( i = 1; t--; i++ )
	{
		fin >> n >> k;
		a = pow( 2, (float) n );
		if ( !((k + 1) & (a - 1)) ) fout << "Case #" << i << ": ON" << endl;
		else fout << "Case #" << i << ": OFF" << endl;
	}
	fin.close();
	fout.close();
	return 0;
}