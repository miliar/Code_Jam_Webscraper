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
	cout<<argv[1]<<endl;
	cout<<argv[2]<<endl;
	ifstream inp(argv[1]); //input file
	ofstream outp(argv[2]); //output file

	/* Code goes here */

	int t;
	inp>>t;
	for (int i=1; i<=t; i++) {
		int orange_p = 1;
		int blue_p = 1;
		int orange_moved = 0;
		int blue_moved = 0;
		long time_passed = 0;
		
		int buttons;
		inp>>buttons;
		char inpc;
		int inpp;
		for (int j=0; j<buttons; j++) {
			inp>>inpc;
			inp>>inpp;
			if (inpc == 'O') {
				int need = abs(orange_p - inpp);
				if (need - orange_moved > 0) {
					time_passed += need - orange_moved + 1;
					blue_moved += need - orange_moved + 1;
				} else {
					time_passed++;
					blue_moved++;
				}
				orange_moved = 0;
				orange_p = inpp;
			} else {
				int need = abs(blue_p - inpp);
				if (need - blue_moved > 0) {
					time_passed += need - blue_moved + 1;
					orange_moved += need - blue_moved + 1;
				} else {
					time_passed++;
					orange_moved++;
				}
				blue_moved = 0;
				blue_p = inpp;
			}
		}
		outp<<"Case #"<<i<<": "<<time_passed;
		if (i != t) outp<<endl;
	}

	/* End of code */

	inp.close();
	outp.close();
}
