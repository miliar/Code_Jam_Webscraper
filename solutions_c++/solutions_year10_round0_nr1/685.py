#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int a[] = {0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535,
 131071, 262143, 524287, 1048575, 2097151, 4194303, 8388607, 16777215, 33554431,
 67108863, 134217727, 268435455, 536870911, 1073741823, 2147483647 };

int main( )
{
	int T, N, K;
	string infile, outfile;
	cin >> infile >> outfile;
	ifstream in( infile.c_str() );
	ofstream out( outfile.c_str() );
	in >> T;
	for( int i=1; i<=T; ++i )
	{
		in >> N >> K;
		out << "Case #" << i << ": ";
		if( (K&a[N])==a[N] )
			out << "ON" << endl;
		else 
			out <<"OFF" << endl;
	}
	in.close( );
	out.close( );
	return 0;
}