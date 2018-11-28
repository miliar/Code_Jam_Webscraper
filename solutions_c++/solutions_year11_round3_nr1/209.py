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
	ofstream outp((string(argv[1])+".out").c_str()); //output file

	int t;
	inp>>t;

	for(int i=0; i<t; i++) {

	/* Code goes here */

		int r, c;
		inp>>r>>c;
		char tiles[r][c];
		for (int m=0; m<r; m++){
			for (int n=0; n<c; n++){
				inp>>tiles[m][n];
			}
			inp.get();
		}

		bool possible=true;

		
		for (int m=0; m<r; m++){
			for (int n=0; n<c; n++){
				if (tiles[m][n] == '#') {
					if (m == r-1 || n == c-1) {
						possible = false;
						break;
					}
					if (tiles[m+1][n] != '#' || tiles[m][n+1] != '#' || tiles[m+1][n+1] != '#') {
						possible = false;
						break;
					}
					tiles[m][n]='/';
					tiles[m+1][n]='\\';
					tiles[m][n+1]='\\';
					tiles[m+1][n+1]='/';
				}
			}
			if (!possible) break;
		}

		outp<<"Case #"<<i+1<<":";
		outp<<endl;
		if (!possible) {
			outp<<"Impossible"<<endl;
		} else {
			for (int m=0; m<r; m++){
				for (int n=0; n<c; n++){
					outp<<tiles[m][n];
				}
				outp<<endl;
			}
		}
	/* End of code */

	}

	inp.close();
	outp.close();
}
