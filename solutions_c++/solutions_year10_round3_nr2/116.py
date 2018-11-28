#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <fstream>
#include <math.h>
#include <algorithm> 
#include <vector> 
#include <string>

using namespace std;

void main() {
	ifstream fin("B.in");
	ofstream fout("B.out");

	long T; fin >> T;
	for (long l=0; l<T; l++) {
		long lo, p, c;
		fin >> lo >> p >> c;
		long a1 = ceil( log(p/double(lo)) / log(double(c)) );
		long a2 = ceil( log(double(a1)) / log(2.0) );

		fout << "Case #" << (l+1) << ": ";
		fout << a2 << endl;
	}

	fin.close(); fout.close();
}