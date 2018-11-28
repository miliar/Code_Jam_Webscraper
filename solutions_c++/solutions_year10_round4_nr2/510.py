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

int popcount(unsigned int x) {
	int result=0;
	for(int i=0; i<sizeof(x)*8; i++) if(x&(1U<<i)) result++;
	return result;
}

class GCJ {
public:
	ll memo[1050][1050];
	int P;
	vector <int> M;
	vector <vector <int> > price;

	ll rec(int d, int pb) {
		ll res=2000000000000, tmp;
		int buy[11];
		int nb, pcnt, ppcnt;

		if(d==(1<<P)) return 0;
		if(memo[d][pb]>=0) return memo[d][pb];

		ppcnt=popcount(pb);
		for(int i=0; i<(1<<P); i++) {
			if(ppcnt>=P-M[d]) {
				if(i>pb) break;
				else i=pb;
			}
			pcnt=popcount(i);
			if((ppcnt<=P-M[d] && pcnt!=P-M[d]) || (ppcnt>P-M[d] && pcnt!=ppcnt)) continue;
			if(popcount(pb|i)!=pcnt) continue;
			memset(buy, 0, sizeof(buy));
			tmp=0;
			for(int j=0; j<P; j++) {
				if(i&(1<<j)) {
					buy[j]=1;
					if(!(pb&(1<<j))) tmp+=price[j][d/(1<<(j+1))];
				}
			}
			nb=0;
			for(int j=0; j<P; j++) {
				if(buy[j]) {
					if((d+1)%(1<<(j+1))>0) nb|=(1<<j);
				}
			}
			tmp+=rec(d+1, nb);
			res=min(res, tmp);
		}

		memo[d][pb]=res;
		return res;
	}

	ll solve(int _P, vector <int> _M, vector <vector <int> > _price) {
		ll res=0;
		
		P=_P; M=_M; price=_price;
		memset(memo, -1, sizeof(memo));
		res=rec(0, 0);
		return res;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int testcase, P;
	vector <int> M;
	vector <vector <int> > price;
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
		ifs >> P;
		M.resize(1<<P);
		for(int j=0; j<(1<<P); j++) {
			ifs >> M[j];
		}
		price.clear(); price.resize(P);
		for(int j=0; j<P; j++) {
			price[j].resize(1<<(P-1-j));
			for(int k=0; k<(1<<(P-1-j)); k++) {
				ifs >> price[j][k];
			}
		}
		ofs << "Case #" << i << ": " << gcj.solve(P, M, price) << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)