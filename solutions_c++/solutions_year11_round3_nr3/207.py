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
		unsigned long long n, l, h;
		inp>>n>>l>>h;
		unsigned long long notes[n];
		for (int j=0; j<n; j++)
			inp>>notes[j];

		if (l == 1) {
			outp<<"Case #"<<i+1<<": 1"<<endl;
			continue;
		}
		vector<unsigned long long> factors;

		vector<unsigned long long> freqs;

		for (int j=0; j<n; j++) {
			for (int k=2; k <= notes[j]/2; k++) {
				if (k >= l && k <= h) {
					if (notes[j] % k == 0) {
						unsigned long long pos = find(factors.begin(), factors.end(), k) - factors.begin();
						if (pos < factors.size()) {
							freqs[pos]++;
						} else {
							factors.push_back(k);
							freqs.push_back(1);
						}
					}
				}
			}
			unsigned long long k = 1;
			while (notes[j]*k < l) k++;
			while (notes[j]*k <= h) {
				unsigned long long pos = find(factors.begin(), factors.end(), notes[j]*k) - factors.begin();
				if (pos < factors.size()) {
					freqs[pos]++;
				} else {
					factors.push_back(notes[j]*k);
					freqs.push_back(1);
				}
				k++;
			}
		}

		unsigned long long best_note=0;
		unsigned long long goodness=0;
		for (int j=0; j<factors.size(); j++) {
			if (goodness < freqs[j]) {
				best_note = factors[j];
				goodness = freqs[j];
			}
			if (goodness == freqs[j] && factors[j] < best_note) {
				best_note = factors[j];
				goodness = freqs[j];
			}
		}
		if (goodness == n) {
			outp<<"Case #"<<i+1<<": "<<best_note<<endl;
		} else {
			outp<<"Case #"<<i+1<<": NO"<<endl;
		}
	/* End of code */

	}

	inp.close();
	outp.close();
}
