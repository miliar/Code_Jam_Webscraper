/*
 * A.cpp
 *
 *  Created on: 26/09/2009
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

typedef long long ll;
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
	return (c >= '0' && c <= '9' ? c - '0' : c - 'A' + 10);
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
ll tod(string s, int base) {
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

/***********Get sum of digits***********/
int gets(string s) {
	int x = 0, n = s.size();
	for (int i = n - 2; i >= 0; i--)
		x += DecVal(s[i]);
	return x + DecVal(s[n - 1]);
}
/*=====================================*/

//ll arr[44];
char str[44];
string arr1[44];
int ran[44];

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large(4).in", "rt", stdin);
	freopen("1.txt", "wt", stdout);
#endif
	int t, n;
	scanf("%d", &t);
	rep(K,t) {
		memset(ran,-1,sizeof(ran));
		scanf("%d", &n);
		rep(i,n) {
			scanf(" %s", str);
			arr1[i] = string(str);
			for (int j = n - 1; j >= 0; j--)
				if (str[j] == '1') {
					ran[i] = j;
					break;
				}
			//arr[i]=tod(string(str).substr(i+1)+string(str).substr(0,i+1),2);
			//cerr<<string(str).substr(i+1)+string(str).substr(0,i+1)<<endl;
		}
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			if (ran[i] <= i)
				continue;
			for (int j = i + 1; j < n; j++) {
				if (ran[j] <= i) {
					while (j != i) {
						cnt++;
						swap(arr1[j], arr1[j - 1]);
						swap(ran[j], ran[j - 1]);
						j--;
					}
					/*rep(k,n)
						cout << arr1[k] << endl;
					cout << endl;*/
					break;
				}
				/*cerr<<endl;*/
			}
		}
		//rep(i,n)
		//cout<<arr1[i]<<endl;
		printf("Case #%d: %d\n", K + 1, cnt);
	}
	return 0;
}

