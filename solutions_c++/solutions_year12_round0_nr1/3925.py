/*
 * A.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Marwan
 */
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstring>
#include <sstream>
#include <complex>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <climits>
#include <set>
#include <map>

using namespace std;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;
#define MP make_pair
#define SZ(x) (int)x.size()

#define SMALL
//#define LARGE

typedef long long ll;
typedef pair<int, int> pii;

int main() {
#ifdef SMALL
	freopen ("A-small.in" , "rt" , stdin);
	freopen ("A-small.txt" , "wt" , stdout);
#endif
#ifdef LARGE
	freopen ("A-large.in" , "rt" , stdin);
	freopen ("A-large.txt" , "wt" , stdout);
#endif
	string s = "ynficwlbkuomxsevzpdrjgthaq" ;
	map <char , char> mp ;

	for (int i = 0; i < SZ(s); ++i)
		mp[s[i]] = (i+'a') ;

	string str ;
	int cnt;
	cin >> cnt ;

	getline(cin , str);
	for (int t = 1; t <= cnt; ++t){
		getline(cin , str);
		for (int i = 0; i < SZ(str); ++i)
			if (str[i] != ' ')
				str[i] = mp[str[i]];

		cout << "Case #" << t << ": " << str << endl ;
	}
	return 0;
}
