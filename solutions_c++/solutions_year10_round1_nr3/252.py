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

int lim[1000002];

class GCJ {
public:
	ll solve(int a1, int a2, int b1, int b2) {
		ll result=0;
		
		for(int i=a1; i<=a2; i++) {
			result+=max(min(lim[i], b2)-b1+1, 0);
		}
		for(int i=b1; i<=b2; i++) {
			result+=max(min(lim[i], a2)-a1+1, 0);
		}

		return result;
	}
};

bool ifw(int a, int b) {
	bool w=true;
	if(a==b) return false;
	while(b) {
		if(a>=b*2) return w;
		a-=b;
		swap(a, b);
		w=!w;
	}
	return w;
}

void calcl(void) {
	int l;
	for(int i=1; i<=1000000; i++) {
		l=i*0.618;
		if(ifw(i, l)) {
			while(1) {
				l++;
				if(!ifw(i, l)) break;
			}
			lim[i]=l-1;
		} else {
			while(1) {
				l--;
				if(ifw(i, l)) break;
			}
			lim[i]=l;
		}
	}
}

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int n, A1, A2, B1, B2;
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

	calcl();
	ifs >> n; ifs.ignore();
	for(int i=1; i<=n; i++) {
		ifs >> A1 >> A2 >> B1 >> B2;
		ofs << "Case #" << i << ": " << gcj.solve(A1, A2, B1, B2) << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)