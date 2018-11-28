#include <stdio.h>
#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;
int main(int argc, char *argv[])
{
	printf("Hello, world\n");
	ifstream input;
	input.open( "A-large.in" );
	ofstream output;
	output.open( "A-large.out" );

	long N = 4,pow2N;
	long K = 47;
	long newN;
	
	int T;

	input>>T;
	for( int i=1; i<=T; i++ )
	{
		input>>N>>K;
		pow2N = long(pow( 2, N ));
		if( (K+1)%pow2N  == 0 ) 
			output<<"Case #"<<i<<": ON\n";
		else
			output<<"Case #"<<i<<": OFF\n";

	}
	input.close();
	output.close();
	return 0;
}
