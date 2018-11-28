/*
 * D.cpp
 *
 *  Created on: May 7, 2011
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
#include <utility>
#include <numeric>
#include <cctype>
#include <cmath>

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
		vuint v(N);
		for(uint i=0; i<N; ++i) {
			cin >> v[i];
		}
		uint matchingPairsX2 = 0;
		uint sorted = 0;
		for(uint i=0; i<N; ++i) {
			if(i == v[i]-1) {
				++sorted;
			}
			else if(v[i] == v[v[i]-1]) {
				++matchingPairsX2;
			}
		}
		uint k = N-matchingPairsX2-sorted;
		cout << "Case #" << test+1 << ": " << fixed << setprecision(6) << static_cast<float>(k);
		if(test<numTests-1) {
			cout << endl;
		}

	}
	return 0;
}

