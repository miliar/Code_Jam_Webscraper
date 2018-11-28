/*
 * A.cpp
 *
 *  Created on: 13/09/2009
 *      Author: Hamzawy
 */

#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;

/*
 #include <ext/hash_set>
 #include <ext/hash_map>
 using namespace __gnu_cxx;
 */

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
const long double PI = (2.0 * acos(0.0));

char str[100];

map<char, ll> m;

/***********string to integer***********/
ll stoi(string s) {
	stringstream ss(s);
	ll x;
	ss >> x;
	return x;
}
/*=====================================*/

/***********integer to string***********/
string itos(ll x) {
	stringstream ss;
	ss << x;
	return ss.str();
}
/*=====================================*/

/**********Value of char in 10**********/
ll DecVal(char c) {
	/*update this function to ur suitable
	 char set if 'A' or 'a' or another***/
	//return (c >= '0' && c <= '9' ? c - '0' : c - 'A' + 10);
	return m[c];
}
/*=====================================*/

/**********Value of int to char*********/
char CharVal(ll x) {
	/*update this function to ur suitable
	 char set if 'A' or 'a' or another***/
	return (x >= 0 && x <= 9 ? x + '0' : x - 10 + 'A');
}
/*=====================================*/

/**********Any base to decimal**********/
ll tod(string s, ll base) {
	ll x = 0, n = s.size(), b = 1;
	for (int i = n - 1; i >= 0; i--, b *= base)
		x += DecVal(s[i]) * b;
	return x;
}
/*=====================================*/

/*********Decimal to any base***********/
string tob(ll x, int b) {
	string s = "";
	while (x) {
		s = CharVal(x % b) + s;
		x /= b;
	}
	return s;
}
/*=====================================*/

map<char, vector<int> > val;
int base;

int arr[70][1 << (61)];

int main() {
#ifndef ONLINE_JUDGE
	//freopen("1.in","rt",stdin);
	//freopen("1.out","wt",stdout);
#endif
	/*m['a']=1;
	 m['b']=0;
	 m['c']=2;
	 cout<<tod("abcccccccde",5)<<endl;
	 m['b']=2;
	 m['c']=0;
	 cout<<tod("abcccccccde",5)<<endl;*/
	freopen("A-large(3).in", "rt", stdin);
	freopen("1.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	rep(K,t) {
		scanf(" %s", str);
		m.clear();
		val.clear();
		int n = strlen(str), b = 0;
		m[str[0]] = 1;
		for (int i = 1; i < n; i++) {
			if (m.find(str[i]) == m.end())
				m[str[i]] = b++;
			if (b == 1)
				b++;
		}
		if (b < 2)
			b = 2;

		 cerr<<str<<endl;
		 for(__typeof(m.begin()) it = m.begin();it!=m.end();it++)
		 cerr<<it->first<<" "<<it->second<<endl;
		cout << "Case #" << K + 1 << ": " << tod(string(str), b) << endl;
	}
	return 0;
}
