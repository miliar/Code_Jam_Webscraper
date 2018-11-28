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

double solve(int X, int S, int R, double t, int N, vector <int> B, vector <int> E, vector <int> w) {
	double res=0;

	vector <pair <int, int> > wl;
	int nw=X;
	for(int i=0; i<N; i++) {
		wl.push_back(make_pair(w[i], E[i]-B[i]));
		nw-=E[i]-B[i];
	}

	wl.push_back(make_pair(0, nw));
	sort(wl.begin(), wl.end());

	for(int i=0; i<(int)wl.size(); i++) {
		double tt=(double)wl[i].second/(R+wl[i].first);
		if(tt>t) {
			double len=(R+wl[i].first)*t;
			tt=t+(double)(wl[i].second-len)/(S+wl[i].first);
			t=0;
		} else t-=tt;
		res+=tt;
	}
	
	return res;
}

int main() {
	int practice=0;
	string prb[12];
	const string difficulty[2][2]={{"-small-attempt.in", "-large.in"}, {"-small-practice.in", "-large-practice.in"}};
	const string extension=".txt";

	char key;
	while(1) {
		for(int i=0; i<12; i++) {
			prb[i].assign(1, 'A'+i/2);
			prb[i]+=difficulty[practice][i%2];
			prb[i]+=extension;
			cout << (char)('a'+i) << ". " << prb[i] << endl;
		}
		cout << "p. " << (practice?"change to practice mode.":"change to match mode.") << endl;

		do {
			cout << "Choose the input file." << endl;
			cin >> key;
		} while((key-'a'<0 || key-'a'>=12) && key!='p');
		if(key!='p') break;
		practice^=1;
		system("cls");
	}
	string filename=prb[key-'a'];

	if(((key-'a'+1)&1) && !practice) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key-'0'<0 || key-'9'>0);
		filename.insert(15, 1, key);
	}

	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ofstream ofs("output.txt");

	int testcase;
	ifs >> testcase; ifs.ignore();
	for(int testnum=1; testnum<=testcase; testnum++) {
		int X, S, R, t, N;
		ifs >> X >> S >> R >> t >> N;
		vector <int> B(N), E(N), w(N);
		for(int i=0; i<N; i++) ifs >> B[i] >> E[i] >> w[i];
		double res=solve(X, S, R, t, N, B, E, w);
		ofs << "Case #" << testnum << ": ";
		ofs << fixed << setprecision(15) << res << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)