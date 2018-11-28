/**
 * freecell-stats.cpp
 *
 * @date May 20, 2011
 * @author Arpan
 **/

#include <iostream>
#include <limits>
#include <cfloat>

#define DEBUG

using namespace std;

long gcd(long a, long b) {
	if(b == 0)
		return a;
	else
		return gcd(b, a % b);
}

int main(int argc, char* argv[]) {
#ifdef DEBUG
	cout << "double: # decimal digits = " << std::numeric_limits<double>::digits10 << endl
		 << "long double: #dec digits = " << std::numeric_limits<long double>::digits10 << endl;
	cout << "FLT_MANT_DIG = " << FLT_MANT_DIG
		 <<	", DBL_MANT_DIG = " << DBL_MANT_DIG
		 <<	", LDBL_MANT_DIG = " << LDBL_MANT_DIG << endl;
#endif
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		long double N;
		int PD, PG;
		cin >> N >> PD >> PG;

		bool possible = false;
		if(PG == 100 && PD == 100)
			possible = true;
		else if(PG == 100 && PD != 100)
			possible = false;
		else if(PD > 0 && PG == 0)
			possible = false;
		else {
			long hcf = gcd(PD, 100);
#ifdef DEBUG
			cout << "N = " << N << " (" << (N == 1e+14) << ")"
				 << ", " << PD << "/" << 100 << " = " << PD / hcf << "/" << 100 / hcf << ", gcd(" << PD << "," << 100 << ") = " << hcf << endl;
#endif
			possible = ((100 / hcf) <= N);
		}
		cout << "Case #" << t << ": " << (possible ? "Possible" : "Broken") << endl;
	}
}


