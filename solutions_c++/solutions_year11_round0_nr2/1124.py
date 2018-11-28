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
		int comb_size = 0;
		inp>>comb_size;
		string comb_rules[comb_size];
		for (int j=0; j<comb_size; j++) {
			inp>>comb_rules[j];
		}
		int del_size = 0;
		inp>>del_size;
		string del_rules[del_size];
		for (int j=0; j<del_size; j++) {
			inp>>del_rules[j];
		}
		int ele_size = 0;
		inp>>ele_size;
		string elements;
		inp>>elements;
		string outstring = "";
		outstring += elements[0];
		for (int j=1; j<elements.length(); j++) {
			bool comb = false;
			for (int m=0; m<comb_size; m++) {
				if ((outstring[outstring.length()-1] == comb_rules[m][0] && 
					 elements[j] == comb_rules[m][1]) ||
					(outstring[outstring.length()-1] == comb_rules[m][1] && 
					 elements[j] == comb_rules[m][0])) {
					outstring[outstring.length()-1] = comb_rules[m][2];
					comb = true;
					break;
				}
			}
			if (comb) continue;
			bool del = false;
			for (int m=0; m<del_size; m++) {
				char search = 0;
				if (elements[j] == del_rules[m][0]) {
					search = del_rules[m][1];
				}
				if (elements[j] == del_rules[m][1]) {
					search = del_rules[m][0];
				}
				if (search != 0) {
					for (int n=0; n<outstring.length(); n++) {
						if (outstring[n] == search) {
							outstring = "";
							del = true;
							break;
						}
					}
					if (del) break;
				}
			}
			if (del) continue;
			outstring += elements[j];
		}
		outp<<"Case #"<<i<<": [";
		for (int j=0; j<outstring.length();j++) {
			outp<<outstring[j];
			if (j != outstring.length()-1) outp<<", ";
		}
		outp<<"]";
		if (i != t) outp<<endl;
	}

	/* End of code */

	inp.close();
	outp.close();
}
