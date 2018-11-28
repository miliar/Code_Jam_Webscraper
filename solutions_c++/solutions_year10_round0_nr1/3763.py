#include "iostream"
#include "fstream"
#include "string"
#include "algorithm"
#include "math.h"

using namespace std;

int main()
{
	int a;
	long n,k,t;
	
	ifstream infile("A-large.in");
	infile >> t;

	ofstream outfile("A-large.out");
	
	int temp;
	int i = 1;
	do
	{
		infile >> n >> k;
		long x = (long)pow(2., n);
		
		if ( k>=n && k % x == x-1)
			outfile << "Case #" << i << ": " << "ON\n";
		else
			outfile << "Case #" << i << ": " << "OFF\n";
		++i;

	} while (i <= t );
		infile.close();
		outfile.close();
	return(0);
}


