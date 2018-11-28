/*
 * C.cpp
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
#include <map>
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
		uint sum = 0;
		uint sumXor = 0;
		vuint v(N);
		for(uint i=0; i<v.size(); ++i) {
			cin >> v[i];
			sum += v[i];
			sumXor ^= v[i];
		}
		uint min = *min_element(v.begin(), v.end());
		cout << "Case #" << test+1 << ": ";
		if(sumXor) {
			cout << "NO";
		}
		else {
			cout << (sum-min);
		}
		if(test<numTests-1) {
			cout << endl;
		}

	}
	return 0;
}

