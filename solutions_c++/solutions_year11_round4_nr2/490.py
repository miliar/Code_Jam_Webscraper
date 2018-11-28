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

int solve(int R, int C, int D, vector <string> bl) {
	int res=-1;

	ll msumr[510][510];
	ll msumc[510][510];
	ll sum[510][510];
	ll mwr[510][510];
	ll mwc[510][510];
	memset(msumr, 0, sizeof(msumr));
	memset(msumc, 0, sizeof(msumc));
	memset(sum, 0, sizeof(sum));
	memset(mwr, 0, sizeof(mwr));
	memset(mwc, 0, sizeof(mwc));

	for(int r=0; r<R; r++) {
		for(int c=0; c<C; c++) {
			mwr[r][c]=r*(D+bl[r][c]-'0');
			mwc[r][c]=c*(D+bl[r][c]-'0');
		}
	}

	for(int r=1; r<=R; r++) {
		for(int c=1; c<=C; c++) {
			sum[r][c]=sum[r][c-1]+sum[r-1][c]-sum[r-1][c-1]+D+bl[r-1][c-1]-'0';
			msumr[r][c]=msumr[r][c-1]+msumr[r-1][c]-msumr[r-1][c-1]+mwr[r-1][c-1];
			msumc[r][c]=msumc[r][c-1]+msumc[r-1][c]-msumc[r-1][c-1]+mwc[r-1][c-1];
		}
	}

	for(int r=0; r<R; r++) {
		for(int c=0; c<C; c++) {
			for(int k=3; k<=min(R, C); k++) {
				if(r+k>R || c+k>C) break;
				ll sumr=0, sumc=0;
				sumr=msumr[r+k][c+k]-msumr[r+k][c]-msumr[r][c+k]+msumr[r][c]-mwr[r][c]-mwr[r+k-1][c]-mwr[r][c+k-1]-mwr[r+k-1][c+k-1];
				sumr*=2;
				sumr-=(sum[r+k][c+k]-sum[r+k][c]-sum[r][c+k]+sum[r][c]-(D+bl[r][c]-'0')-(D+bl[r+k-1][c]-'0')-(D+bl[r][c+k-1]-'0')-(D+bl[r+k-1][c+k-1]-'0'))*(r*2+k-1);
				sumc=msumc[r+k][c+k]-msumc[r+k][c]-msumc[r][c+k]+msumc[r][c]-mwc[r][c]-mwc[r+k-1][c]-mwc[r][c+k-1]-mwc[r+k-1][c+k-1];
				sumc*=2;
				sumc-=(sum[r+k][c+k]-sum[r+k][c]-sum[r][c+k]+sum[r][c]-(D+bl[r][c]-'0')-(D+bl[r+k-1][c]-'0')-(D+bl[r][c+k-1]-'0')-(D+bl[r+k-1][c+k-1]-'0'))*(c*2+k-1);
				if(sumr==0 && sumc==0) res=max(res, k);
			}
		}
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
		int R, C, D;
		ifs >> R >> C >> D; ifs.ignore();
		vector <string> bl(R);
		for(int i=0; i<R; i++) {
			getline(ifs, bl[i]);
		}
		int res=solve(R, C, D, bl);
		ofs << "Case #" << testnum << ": ";
		if(res>=0) ofs << res << endl;
		else ofs << "IMPOSSIBLE" << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)