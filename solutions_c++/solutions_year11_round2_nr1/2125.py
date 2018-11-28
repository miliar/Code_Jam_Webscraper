/*
 * a.cpp
 *
 *  Created on: May 21, 2011
 *      Author: michal
 */

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <utility>
#include <numeric>
#include <cctype>
#include <cmath>

using namespace std;

// 64b g++
typedef unsigned long myUint;
typedef long myInt;
typedef int StdInt;

#define int myInt
#define uint myUint

typedef vector<uint> vuint;
typedef vector<int> vint;
typedef vector<double> vdouble;
typedef vector<bool> vbool;
typedef vector<char> vchar;
typedef vector<string> vstring;

template<class T>
T fast_exponentiation(const T& t, uint n) {
  if(n == 1) {
	  return t;
  }
  else {
	  if(n % 2) {
		  return t*fast_exponentiation(t, n-1);
	  }
	  else {
		  T t1 = fast_exponentiation(t, n/2);
		  return t1*t1;
	  }
  }
}

void test();

StdInt main() {
	uint T;
	cin >> T;
	for(uint t=0; t<T; ++t) {
		cout << "Case #" << t+1 << ":" << endl;
		test();
		if(t<T-1) {
			cout << endl;
		}
	}
	return 0;
}

void test() {
	uint n;
	cin >> n;
	vector<vchar> s(n, vchar(n,'.'));
	for(uint i=0; i<n; ++i) {
		for(uint j=0; j<n; ++j) {
			cin >> s[i][j];
		}
	}
	vdouble wp(n);
	vdouble owp(n);
	vdouble oowp(n);
	vector<vdouble> wins(n, vdouble(n, 0.0));
	vector<vdouble> count(n, vdouble(n, 0.0));
	for(uint i=0; i<n; ++i) {
		for(uint j=0; j<n; ++j) {
			if('1'==s[i][j] || '0'==s[i][j]) {
				count[i][j] = 1.0;
				if('1'==s[i][j]) {
					wins[i][j] = 1.0;
				}
			}
		}
	}
	for(uint i=0; i<n; ++i) {
		wp[i] = accumulate(wins[i].begin(), wins[i].end(),0.0)/accumulate(count[i].begin(), count[i].end(),0.0);
	}
	for(uint i=0; i<n; ++i) {
		double num = 0.0;
		for(uint j=0; j<n; ++j) {
			if(j!=i && count[i][j]) {
				double countOWP = accumulate(count[j].begin(), count[j].end(),-count[j][i]);
				double winsOWP = accumulate(wins[j].begin(), wins[j].end(),-wins[j][i]);
				if(countOWP) {
					owp[i] += winsOWP/countOWP;
					num += 1.0;
				}
			}
		}
		owp[i] /= num;
	}
	for(uint i=0; i<n; ++i) {
		double sumowp = 0.0;
		for(uint j=0; j<n; ++j) {
			if(i!=j && count[i][j]) {
				sumowp += owp[j];
			}
		}
		oowp[i] = sumowp/accumulate(count[i].begin(), count[i].end(), 0.0);
	}
	for(uint i=0; i<n; ++i) {
		double rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
		cout << fixed << setprecision(7) << rpi << endl;
	}
}

