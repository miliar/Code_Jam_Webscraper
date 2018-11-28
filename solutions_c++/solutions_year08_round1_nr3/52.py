#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <set>
#include <queue>
#include <numeric>
#include <complex>
#include <climits>

using namespace std;

template<class T> inline bool fixmin(T &a, T b) {if (a<=b) return false; a=b; return true;}
template<class T> inline bool fixmax(T &a, T b) {if (a>=b) return false; a=b; return true;}

ifstream is("B.in");
ofstream os("B.out");

int a[2001000];
int mod = 0;
int base = 100;

void init() {
	a[1]=5;
	a[2]=27;
	for (mod=3; ; mod++) {
		a[mod] = (6*a[mod-1]-4*a[mod-2]+1+100000) % 1000;
		if (mod > base)
		if (a[mod]==a[base] && a[mod-1]==a[base-1]) break;
		cout << mod << ':' << a[mod] << endl;
		if (mod % 1000==0) cout << mod << endl;
	}
	mod-=2;
	cout << mod << endl;
}

void solve() {
	int n;
	is >> n;
	if (n > base) {
		n %= 100;
		n += 100;	
	}
	os << ' ' << a[n]/100 << (a[n]/10)%10 << a[n]%10 << endl;
}

int main () {
	init();
	int N; is >> N;
	for (int i=1; i<=N; i++) {
		os << "Case #" << i << ":";
		solve();
	}
	return 0;
}
