#ifndef MACRO_HHin
#define MACRO_HH
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <cassert>
#include <map>
#include <set>
#include <cmath>
#include <queue>

#define all(v) v.begin(), v.end()
#define rep(i,n) for(int i = 0; i < (int) n; i++)
#define rept(i,a,n) for(int i = a; i < (int) n; i++)

using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
const int targ = 10000000;
const int tg = 5;



template <typename T>
void printV(vector<T>& v) {
	for (int i=0; i < v.size(); i++)
		cout << v[i] << " ";
	cout << endl;
}

template <typename T>
void printVs(vector<vector<T> >&v){
	for (int i=0; i < v.size(); i++)
		printV(v[i]);

}

template <typename T>
T sum(vector<T> &v) {
	T res = 0;
	rep(i,v.size())
		res += v[i];
	return res;

}

template <typename T>
void reverse(vector<T> & v){
	rep(i,v.size()/2) 
		swap(v[i], v[v.size()-1-i]);
}

void printS(set<int> & s) {
	for (set<int>::iterator it = s.begin(); it != s.end(); it++) 
		cout << (*it) << " ";
	cout << endl;
}


#endif
