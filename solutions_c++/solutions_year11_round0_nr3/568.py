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

class GCJ {
public:
	int solve(int N, vector <int> C) {
		int res=0;
		
		int cur=0;
		for(int i=0; i<N; i++) cur^=C[i];
		if(cur!=0) return -1;

		sort(C.begin(), C.end(), greater <int>());
		res=accumulate(C.begin(), C.end()-1, 0);
		return res;
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
		int N;
		ifs >> N;
		vector <int> C(N);
		for(int j=0; j<N; j++) ifs >> C[j];
		int res=gcj.solve(N, C);
		ofs << "Case #" << i << ": ";
		if(res==-1) ofs << "NO" << endl;
		else ofs << res << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)