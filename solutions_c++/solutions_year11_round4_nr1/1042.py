#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <iomanip>


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

		double x, s, r, ti;
		int n;
		inp>>x>>s>>r>>ti>>n;
		double b[n];
		double e[n];
		double w[n];
		double totalWLen=0;
		for (int j=0; j<n; j++) {
			inp>>b[j]>>e[j]>>w[j];
			totalWLen += e[j]-b[j];
		}
		double walk=x-totalWLen;

		double time=0;
		if (ti*r <= walk) {
			time+=ti+(walk-ti*r)/s;
			for (int j=0; j<n; j++) {
				time+=(e[j]-b[j])/(w[j]+s);
			}
		} else {
			time+=walk/r;
			ti-=time;
			for (int j=0; j<n; j++) {
				int slowest=0;
				double speed=w[0];
				for (int m=0;m<n;m++) {
					if (w[m] < speed) {
						slowest=m;
						speed=w[m];
					}
				}
				if (ti*(r+w[slowest])<(e[slowest]-b[slowest])){
					time+=ti+(e[slowest]-b[slowest]-ti*(r+w[slowest]))/(w[slowest]+s);
					ti=0;
				}
				else{
					time+=(e[slowest]-b[slowest])/(w[slowest]+r);
					ti-=(e[slowest]-b[slowest])/(w[slowest]+r);
				}
				w[slowest] = 100000000;
			}			
		}

		

		outp<<"Case #"<<i+1<<": ";
		outp<<setprecision(10)<<time<<endl;

	/* End of code */

	}

	inp.close();
	outp.close();
}
