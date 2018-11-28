using namespace std;

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <bitset>

#define ulong unsigned long

using namespace std; 

void main_C( istream &in, ostream &out )
{
	int numCases, i;
	in >> numCases; 
	string s; 
	getline( in, s );

	for( i = 0; i < numCases; ++i )
	{
		int nCandies, xorValue, totalSum, min, ii, tmp; 
		in >> nCandies; 
		getline( in , s );
		
		xorValue = 0; 
		totalSum = 0; 
		min = 0x0FFFFFFF; 

		for( ii = 0; ii < nCandies; ++ii ){
			in >> tmp; 
			if( tmp < min ) min = tmp; 
			totalSum += tmp; 
			xorValue = xorValue ^ tmp; 
		}
		

		out << "Case #" << (i+1);
		if( xorValue != 0 ){
			out << ": NO" << endl; 
		}else{
			out << ": " << (totalSum - min) << endl; 
		}
	
		getline( in , s ); // get the carry return 
	}
	return;
}
