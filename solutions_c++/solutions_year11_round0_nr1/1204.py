/*
 * A.cpp
 *
 *  Created on: May 7, 2011
 *      Author: michal
 */

#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <list>
#include <set>
#include <utility>
#include <numeric>
#include <cctype>

using namespace std;

// 64b g++
typedef unsigned long long myUint;
typedef long long myInt;
typedef int StdInt;

#define int myInt
#define uint myUint

typedef vector<uint> vuint;
typedef vector<int> vint;
typedef vector<bool> vbool;
typedef vector<char> vchar;

typedef list<uint> luint;
typedef list<int> lint;
typedef list<bool> lbool;
typedef list<char> lchar;

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

StdInt main() {
	uint numTests;
	cin >> numTests;
	for(uint test=0; test<numTests; ++test) {
		uint N;
		cin >> N;
		uint to = 0;
		uint tb = 0;
		uint xo = 1;
		uint xb = 1;
		for(uint b=0; b<N; ++b) {
			char r;
			uint p;
			uint movTime = 0;
			cin >> skipws >> r >> p;
			if('B' == r) {
				movTime = max(p,xb)-min(p,xb);
				xb = p;
				if(movTime+tb<=to) {
					tb = to+1;
				}
				else {
					tb += (movTime+1);
				}
			}
			else {
				movTime = max(p,xo)-min(p,xo);
				xo = p;
				if(movTime+to<=tb) {
					to = tb+1;
				}
				else {
					to += (movTime+1);
				}
			}

		}
		cout << "Case #" << test+1 << ": " << max(to,tb);
		if(test<numTests-1) {
			cout << endl;
		}

	}
	return 0;
}
