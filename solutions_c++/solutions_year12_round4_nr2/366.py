#define _CRT_SECURE_NO_WARNINGS
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
#include <iterator>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
//#include <NTL/ZZ.h>
using namespace std;
//using namespace NTL;
static const double EPS = 1e-8;
typedef long long ll;
typedef unsigned long long ull;
typedef complex <double> pt;
typedef complex <ll> pti;

vector <int> rr;

void place(int W, int L, vector <int> &r, int &d, int x, int y) {
	if(d>=(int)r.size()) return;
	if(L<0) return;
	int cr=r[d]*2;
	while(W>=0 && d<(int)r.size()) {
		rr.push_back(x); rr.push_back(y);
		place(min(cr/2, W), L-cr, r, ++d, x, y+cr);
		W-=cr;
		x+=cr;
	}
}

vector <int> solve(int W, int L, vector <int> r) {
	int n=r.size();

	vector <pair <int, int> > vp;
	for(int i=0; i<n; i++) vp.push_back(make_pair(r[i], i));
	sort(vp.begin(), vp.end(), greater <pair <int, int> >());
	sort(r.begin(), r.end(), greater <int>());
	rr.clear();
	int d=0;
	place(W, L, r, d, 0, 0);
	vector <pair <int, pair <int, int> > > res;
	for(int i=0; i<n; i++) {
		res.push_back(make_pair(vp[i].second, make_pair(rr[i*2], rr[i*2+1])));
	}
	sort(res.begin(), res.end());
	rr.clear();
	for(int i=0; i<n; i++) {
		rr.push_back(res[i].second.first);
		rr.push_back(res[i].second.second);
	}
	
	return rr;
}

int main() {
	int practice=0;
	string prb[12];
	const string difficulty[2][2]={{"-small-attempt.in", "-large.in"}, {"-small-practice.in", "-large-practice.in"}};
	const string extension="";
	//const string extension=".txt";

	char key;
	while(1) {
		for(int i=0; i<12; i++) {
			prb[i].assign(1, 'A'+i/2);
			prb[i]+=difficulty[practice][i%2];
			prb[i]+=extension;
			cout << (char)(i%2?('A'+i/2):('a'+i/2)) << ". " << prb[i] << endl;
		}
		cout << "p. " << (practice?"change to practice mode.":"change to match mode.") << endl;

		do {
			cout << "Choose the input file." << endl;
			cin >> key;
		} while(!('a'<=key && key<'a'+6) && !('A'<=key && key<'A'+6) && key!='p');
		if(key!='p') break;
		practice^=1;
		system("cls");
	}

	int index, cap;
	if(key>='a') { index=(key-'a')*2; cap=0; }
	else { index=(key-'A')*2+1; cap=1; }
	string filename=prb[index];

	if(!cap && !practice) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key<'0' || '9'<key);
		filename.insert(15, 1, key);
	}

	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ofstream ofs("output.txt");

	int testcase;
	ifs >> testcase; ifs.ignore();
	for(int testnum=1; testnum<=testcase; testnum++) {
		int N, W, L;
		ifs >> N >> W >> L;
		vector <int> r(N);
		for(int i=0; i<N; i++) ifs >> r[i];
		vector <int> res=solve(W, L, r);
		assert(res.size()==N*2);
		for(int i=0; i<N; i++) {
			assert(res[i*2]>=0 && res[i*2]<=W && res[i*2+1]>=0 && res[i*2+1]<=L);
			for(int j=i+1; j<N; j++) {
				assert(hypot(res[i*2]-res[j*2], res[i*2+1]-res[j*2+1])>=r[i]+r[j]);
			}
		}
		ofs << "Case #" << testnum << ": ";
		for(int i=0; i<(int)res.size(); i++) {
			ofs << res[i] << " ";
		}
		ofs << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)