/*
 * B.cpp
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

typedef map< pair<char, char>, char > Combo;
typedef map<char, char> Clr;

StdInt main() {
	uint numTests;
	cin >> numTests;
	for(uint test=0; test<numTests; ++test) {
		uint C;
		cin >> C;
		Combo combo;
		for(uint c=0; c<C; ++c) {
			char c1, c2, c3;
			cin >> skipws >> c1 >> c2 >> c3;
			combo.insert(make_pair(make_pair(c1,c2), c3));
			combo.insert(make_pair(make_pair(c2,c1), c3));
		}
		uint D;
		cin >> D;
		Clr clr;
		for(uint d=0; d<D; ++d) {
			char c1, c2;
			cin >> skipws >> c1 >> c2;
			clr.insert(make_pair(c1,c2));
			clr.insert(make_pair(c2,c1));
		}
		uint N;
		cin >> N;
		vchar v;
		for(uint n=0; n<N; ++n) {
			char cs;
			cin >> skipws >> cs;
			if(v.size()) {
				Combo::iterator i = combo.find(make_pair(cs, v[v.size()-1]));
				if(i != combo.end()) {
					v.pop_back();
					v.push_back(i->second);
					continue;
				}
				Clr::iterator ic = clr.find(cs);
				if(ic != clr.end()) {
					if(find(v.begin(), v.end(), ic->second) != v.end()) {
						v.clear();
						continue;
					}
				}
				v.push_back(cs);
			}
			else {
				v.push_back(cs);
			}
		}
		cout << "Case #" << test+1 << ": [";
		for(uint i = 0; i<v.size(); ++i) {
			cout << v[i];
			if(i<v.size()-1) {
				cout << ", ";
			}
		}
		cout << "]";
		if(test<numTests-1) {
			cout << endl;
		}

	}
	return 0;
}
