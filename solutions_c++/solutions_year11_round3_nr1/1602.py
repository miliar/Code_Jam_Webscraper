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
	uint r,c;
	cin >> r >> c;
	vector<vchar> pic(r, vchar(c));
	uint blue = 0;
	for(uint i=0; i<r; ++i) {
		for(uint j=0; j<c; ++j) {
			cin >> pic[i][j];
			if(pic[i][j] == '#') {
				++blue;
			}
		}
	}
	if(blue%4) {
		cout << "Impossible" << endl;
		return;
	}
	for(uint i=0; i<r; ++i) {
		for(uint j=0; j<c; ++j) {
			if(i && j) {
				if(pic[i][j] == '#' && pic[i-1][j-1] == '#' && pic[i-1][j] == '#' && pic[i][j-1] == '#') {
					pic[i-1][j-1] = pic[i][j] = '/';
					pic[i][j-1] = pic[i-1][j] = '\\';
					blue -= 4;
				}
			}
		}
	}
	if(blue) {
		cout << "Impossible" << endl;
	}
	else {
		for(uint i=0; i<r; ++i) {
			for(uint j=0; j<c; ++j) {
				cout << pic[i][j];
			}
			cout << endl;
		}
	}
}
