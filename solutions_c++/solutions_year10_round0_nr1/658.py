/*
 * Q_A.cpp
 *
 *  Created on: 2010-5-8
 *      Author: dmks
 */


#line 95 "AgeEncoding.cpp"
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
using namespace std;

#define REP(i, n) for(int i = 0; i<(n); i++)
#define abs(a) ((a) >= 0 ? (a) : -(a))
#define inf 2000000001
typedef vector<int> VI;
typedef vector<string> VS;

typedef long long i64;
typedef unsigned long long u64;

int main() {
	int t, n, k;
	cin>>t;
	for (int c = 1; c <= t; c++) {
		cin>>n>>k;
		int m = (1 << n) - 1;
		cout << "Case #" << c << ": " << (((m & k) == m) ? "ON" : "OFF") << endl;
	}
	return 0;
}
