#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <list>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <numeric>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <stack>
#include <queue>
#include <NTL/ZZ.h>
using namespace std;
using namespace NTL;
static const double EPS = 1e-5;
typedef long long ll;
typedef complex <double> pt;

ll gcd(ll a, ll b) {
	while(b) {
		a=a%b;
		swap(a, b);
	}
	return a;
}

class GCJ {
public:
	bool solve(ll N, ll Pd, ll Pg) {
		if(Pd<100 && Pg==100) return false;
		if(Pd>0 && Pg==0) return false;
		if(Pd==0 || Pd==100) return true;
		ll m=100;
		ll g=gcd(m, Pd);
		if(m/g>N) return false;
		else return true;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int testcase;
	GCJ gcj;

	for(int i=0; i<12; i++) {
		prb[i].push_back('A'+i/2);
		if(i%2) prb[i]+="-large";
		else prb[i]+="-small-attempt";
		prb[i]+=".in.txt";
		cout << (char)('a'+i) << ". " << prb[i] << endl;
	}
	do {
		cout << "Choose the input file." << endl;
		cin >> key;
	} while(key-'a'<0 || key-'a'>=12);
	filename=prb[key-'a'];
	if((key-'a'+1)&1) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key-'0'<0 || key-'9'>0);
		filename.insert(15, 1, key);
	}
	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ifs >> testcase; ifs.ignore();
	for(int i=1; i<=testcase; i++) {
		ll N;
		ifs >> N;
		ll Pd, Pg;
		ifs >> Pd >> Pg;
		ofs << "Case #" << i << ": " << ((gcj.solve(N, Pd, Pg))?"Possible":"Broken") << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)