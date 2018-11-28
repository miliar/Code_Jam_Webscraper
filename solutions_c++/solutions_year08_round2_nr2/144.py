#include <stdio.h>
#include <iostream>
#include <string>
#include <set>
#include <vector>

using namespace std;

typedef long long resulttype;

long long gcd(long long A, long long B) {
	while (B) {
		long long T = A%B; A = B; B=T;
	}
	return A;
}


void skipEOL() { string foo; getline(cin,foo); }
resulttype OneCase() {
	cerr << "ONE CASE" << endl;

	resulttype result;

	long long A, B, P;
	
	cin >> A >> B >> P;
	vector <long long> base;
	for (long long T = A; T<=B; ++T)  {
		long long TR = T;
		if (P>2) while (TR % 2==0) TR /= 2;
		for (int d=3; d<1000000 && d<P; d+=2) while (TR % d==0) TR /= d;
		base.push_back(TR);
	}

	vector < set<long long> > All;

	for (vector<long long>::iterator i=base.begin(); i!=base.end(); ++i) {
		cerr << *i << "?" << endl;
		int prev = -1;
		for (int k=All.size()-1; k>=0; --k) {
			for (set<long long>::iterator j = All[k].begin(); j!= All[k].end(); ++j) {
				if (gcd(*j, *i) >1) {
					if (prev >= 0) {
						for (set<long long>::iterator v = All[prev].begin(); v!= All[prev].end(); ++v)
							All[k].insert(*v);
						All.erase(All.begin() + prev);
					} else
						All[k].insert(*i);
					prev = k;
					break;
				}
			}
		}
		if (prev==-1) {
			set <long long> one;
			one.insert(*i);
			All.push_back(one);
		}
	}


	return All.size();;
}

int main() {
	int Anz;
	cin >> Anz;
	skipEOL();
	for (int run=1; run<=Anz; ++run) {
		resulttype result = OneCase();

		cout << "Case #" << run << ": " << result << endl;
	}
	return 0;
};
