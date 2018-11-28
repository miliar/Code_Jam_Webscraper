#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char * argv[])
{
	int T, N, K, i;
	fstream infile, outfile;

	infile.open("A.in", ios_base::in);
	outfile.open("A.out", ios_base::out);

	infile >> T;
	for( i = 0; i < T; i++ )
	{
		infile >> N >> K;
		outfile << "Case #" << i+1 << ": ";
		if ( K % (1 << N) == (1 << N)-1 ) outfile << " ON";
		else outfile << "OFF";
		outfile << endl;
	}

	infile.close();
	outfile.close();

	return 0;
}