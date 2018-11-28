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
typedef unsigned long long ullong;

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

		ullong l, t, n, c;
		inp>>l>>t>>n>>c;
		ullong a[c];
		for (ullong j=0; j<c; j++)
			inp>>a[j];
		ullong path[n];
		for (ullong j=0; j<n; j++) {
			path[j] = a[j%c];
		}
		ullong time=0;
		ullong pos=0;
		ullong next_time=path[0]*2;
		while (next_time<t && pos < n) {
			time=next_time;
			pos++;
			next_time=next_time+path[pos]*2;
		}
		if (pos < n) { 
			path[pos] = path[pos] - (t-time)/2;
			time = t;
			sort(path+pos, path+n);
			reverse(path+pos, path+n);
			while (l > 0 && pos < n) {
				time+=path[pos];
				pos++;
				l--;
			}
			for (ullong k=pos; k<n; k++) {
				time+= path[k]*2;
			}
		}

		outp<<"Case #"<<i+1<<": "<<time<<endl;

	/* End of code */

	}

	inp.close();
	outp.close();
}
