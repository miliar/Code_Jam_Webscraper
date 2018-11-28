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

		int n;
		inp>>n;
		double wp[n];
		double owp[n];
		double oowp[n];
		string games[n];
		for (int j=0; j<n; j++) {
			inp>>games[j];
		}
		for (int j=0; j<n; j++) {
			double countw=0;
			double countl=0;
			double owpc=0;
			int counto=0;
			for (int m=0; m<n; m++) {
				if (games[j][m]=='0') countl++;
				if (games[j][m]=='1') countw++;
				if (games[j][m]!='.') {
					double countw2=0;
					double countl2=0;
					for (int k=0; k<n; k++) {
						if (games[m][k]=='0' && j!=k) countl2++;
						if (games[m][k]=='1' && j!=k) countw2++;
					}
					owpc+=countw2/(countw2+countl2);
					counto++;
				}
			}
			wp[j]=countw/(countw+countl);
			owp[j]=owpc/counto;
		}
		/*for (int j=0; j<n; j++) {
			int gamesp=0;
			double totalowp=0;
			for (int m=0; m<n; m++) {
				if (games[j][m]!='.' && ) {
					gamesp++;
					totalowp+=wp[m];
				}
			}
			owp[j]=totalowp/gamesp;
			}*/
		for (int j=0; j<n; j++) {
			int gamesp=0;
			double totaloowp=0;
			for (int m=0; m<n; m++) {
				if (games[j][m]!='.') {
					gamesp++;
					totaloowp+=owp[m];
				}
			}
			oowp[j]=totaloowp/gamesp;
		}
		outp<<"Case #"<<i+1<<":"<<endl;
		for (int j=0; j<n; j++) {
			outp<<0.25*wp[j]+0.5*owp[j]+0.25*oowp[j];
			if (!(j==(n-1) && i==(t-1))) outp<<endl;
		}
	/* End of code */

	}

	inp.close();
	outp.close();
}
