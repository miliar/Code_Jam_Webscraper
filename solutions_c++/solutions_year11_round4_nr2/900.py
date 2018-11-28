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


		long r, c, d;
		inp>>r>>c>>d;
		long sheet[r][c];
		for (int n=0; n<r; n++){
			for (int m=0; m<r; m++) {
				char in;
				inp>>in;
				sheet[n][m] = d+(int(in)-48);
				
			}
			inp.get();
		}


		int mk=0;
		for (int k=min(r,c); k>2; k--) {
			cout<<k<<endl;
			int n, m;
			if (k%2 == 1) {
				n = (k-1)/2;
				m = (k-1)/2;
			} else {
				n = k/2 - 1;
				m = k/2 - 1;
			}
			for (int l=0; l<(r-k+1)*(c-k+1); l++) {
				if (k%2 == 1) {
					long long mass1 = 0;
					long long mass2 = 0;
					for (int p1 = -(k-1)/2; p1<=(k-1)/2; p1++) {
						for (int p2 = -(k-1)/2; p2 <= (k-1)/2; p2++) {
							if ((abs(p1) == (k-1)/2) && (abs(p2) == (k-1)/2))
								continue;
							mass1 += p1*sheet[n+p1][m+p2];
							mass2 += p2*sheet[n+p1][m+p2];
						}
					}
					if (mass1==0 && mass2==0) {
						mk=k;
						cout<<n<<" "<<m<<endl;
						break;
					}
					if (n+1 == r-(k-1)/2) {
						n=(k-1)/2;
						m++;
					} else {
						n++;
					}
				} else {
					double mass1 = 0;
					double mass2 = 0;
					for (int p1 = -k/2+1; p1<=k/2; p1++) {
						for (int p2 = -k/2+1; p2 <= k/2; p2++) {
							if (((p1) == -k/2+1 && (p2) == k/2) ||
								((p1) == -k/2+1 && (p2) == -k/2+1) ||
								((p1) == k/2 && (p2) == k/2) ||
								((p1) == k/2 && (p2) == -k/2+1))
								continue;
							mass1 += (p1-0.5)*sheet[n+p1][m+p2];
							mass2 += (p2-0.5)*sheet[n+p1][m+p2];
						}
					}
					if (mass1==0 && mass2==0) {
						mk=k;
						cout<<n<<" "<<m<<endl;
						break;
					}
					if (n+1 == (r-k/2)+1) {
						n=k/2 - 1;
						m++;
					} else {
						n++;
					}
				}
			}
			if (mk != 0) break;
		}


		outp<<"Case #"<<i+1<<": ";
		if (mk != 0) {
			outp<<mk<<endl;
		} else {
			outp<<"IMPOSSIBLE"<<endl;
		}

	/* End of code */

	}

	inp.close();
	outp.close();
}
