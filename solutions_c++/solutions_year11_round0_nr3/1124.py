#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef vector<long>::iterator longIt;
typedef vector<double>::iterator doubleIt;
typedef vector<string>::iterator stringIt;
typedef vector<vector<long> >::iterator vecIntIt;
typedef vector<vector<double> >::iterator vecDoubleIt;
typedef vector<vector<string> >::iterator vecStringIt;

template <class T>
inline const T max_arg(const T& a, const T& b) {
	return (b<a)?1:2;
}

template <class T>
inline bool from_string(T& t, const string& s,
				 std::ios_base& (*f)(std::ios_base&)) {
	istringstream iss(s);
	return !(iss>>f>>t).fail();
}

template <class T>
inline string to_string(const T& t) {
	stringstream ss;
	ss<<t;
	return ss.str();
}

int main(int argc, char **argv) {
	ifstream inp(argv[1]); //input file
	ofstream outp(argv[2]); //output file

	/* Code goes here */

	int t;
	inp>>t;
	for (int i=1; i<=t; i++) {
		
		int k;
		inp>>k;
		vector<long> candy;
		for (int j=0;j<k;j++) {
			long c;
			inp>>c;
			candy.push_back(c);
		}
		sort(candy.begin(), candy.end());
		long xored = 0;
		unsigned long long sum = 0;
		for (int j=0; j<candy.size(); j++) {
			sum += candy[j];
			xored ^= candy[j];
		}

		outp<<"Case #"<<i<<": ";
		if (xored != 0) {
			outp<<"NO";
		} else {
			outp<<(sum-candy[0]);
		}
		if (i!=t) outp<<endl;
	}

	/* End of code */

	inp.close();
	outp.close();
}
