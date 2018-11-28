#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "A-large.out"

#include <iostream>
#include <fstream>
#include <cstdlib>

using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;


int main(void)
{
	//get input from file
	ifstream infile (INPUT_FILE);
	if (!infile)
	{
		cout << "Cannot open input file!" << endl;
		exit(1);
	}
	ofstream outfile ( OUTPUT_FILE );
	if (!outfile)
	{
		cout << "Cannot open output file!" << endl;
		exit(1);
	}
	
	int T;			// number of cases T
	int N, K;		// number of snappers N, and snaps K

	infile >> T;

	for (int i = 1; i <= T; i++)
	{
		infile >> N >> K;
		int two_to_power_N = 1 << N;    //2 to the power of N
		if ( K >= two_to_power_N )
			K %= two_to_power_N;
		outfile << "Case #" << i  << ": " 
	    	 	<< ( (K == two_to_power_N - 1) ? "ON" : "OFF" ) << endl;
	}
	return 0;
}
