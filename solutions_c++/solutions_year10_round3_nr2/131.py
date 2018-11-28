#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <gmpxx.h>	/* GNU MP, http://gmplib.org/, link with -lgmp -lgmpxx */
#include <cstdlib>
#include <cmath>


using namespace std;


int main (int argc, char *argv[])
{
	int T, t;
	cin >> T;
	for (t = 1; t <= T; t++)
	{
		int U, L, C;
		cin >> L >> U >> C;
		int tests = 0;
		
		tests = ceil( log( ( log((double)U) - log((double)L) )/log((double)C)-1e-12 )/log((double)2.0));
		if (tests < 0) tests = 0;
		
		cout << "Case #" << t << ": " << tests << endl;
		
	}
	
	return 0;
}


