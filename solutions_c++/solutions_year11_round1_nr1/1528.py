#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <string>
#include <iomanip>
#include <algorithm>
#include <list>
#include <cmath>

using namespace std;

std::ostream& outCase(unsigned int tc) {
	std::cout << "Case #" << (tc + 1) << ": ";
	return std::cout;
}

unsigned gcd(unsigned a, unsigned b)
{
    while( 1 )
    {
        a = a % b;
		if( a == 0 )
			return b;
		b = b % a;

        if( b == 0 )
			return a;
    }
}

bool testCase() {
	unsigned N; cin >> N;
	unsigned Pd; cin >> Pd;
	unsigned Pg; cin >> Pg;

	if (Pd != 0 && Pd != 100) {
		unsigned cd = gcd(100, (Pd <= 50 ? Pd : 100 - Pd));
		unsigned minN = 100 / cd;

		if (N < minN)
			return false;
	}

	if (Pd != 100 && Pg == 100)
		return false;

	if (Pd != 0 && Pg == 0)
		return false;

	return true;
}

int main() {
	unsigned int T; cin >> T;
	for (unsigned int t = 0; t < T; ++t) {		
		outCase(t);
		bool r = testCase();	
		cout << (r ? "Possible" : "Broken") << endl;
	}

	return 0;
}
