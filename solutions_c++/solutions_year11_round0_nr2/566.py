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
	string solve(int C, int D, int N, vector <string> comb, vector <string> opos, string invo) {
		string res;
		
		int appear[256];
		memset(appear, 0, sizeof(appear));
		char prev=127;

		for(int i=0; i<N; i++) {
			res.push_back(invo[i]);
			appear[invo[i]]++;
			for(int j=0; j<C; j++) {
				if(prev==comb[j][0] && invo[i]==comb[j][1] || prev==comb[j][1] && invo[i]==comb[j][0]) {
					res.erase(res.size()-2, 2);
					res.push_back(comb[j][2]);
					appear[prev]--;
					appear[invo[i]]--;
					appear[comb[j][2]]++;
					prev=comb[j][2];
					break;
				}
			}
			for(int j=0; j<D; j++) {
				if(appear[opos[j][0]] && appear[opos[j][1]]) {
					res.clear();
					memset(appear, 0, sizeof(appear));
					prev=127;
					break;
				}
			}
			if(res.empty()) prev=127;
			else prev=res[res.size()-1];
		}

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
		int C, D, N;
		ifs >> C;
		vector <string> comb(C);
		for(int j=0; j<C; j++) ifs >> comb[j];
		ifs >> D;
		vector <string> opos(D);
		for(int j=0; j<D; j++) ifs >> opos[j];
		ifs >> N;
		string invo;
		ifs >> invo;
		string res=gcj.solve(C, D, N, comb, opos, invo);
		ofs << "Case #" << i << ": [";
		for(int j=0; j<(int)res.size(); j++) {
			if(j>0) ofs << ", ";
			ofs << res[j];
		}
		ofs << "]" << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)