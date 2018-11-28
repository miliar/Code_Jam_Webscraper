/*
 * A1_A.cpp
 *
 *  Created on: 2010-5-22
 *      Author: dmks
 */
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

int n, k;
VS v;



bool win(char a) {
	REP(i, n) {
		int num = 0;
		REP(j, n) {
			if (v[i][j] == a) {
				if (++num >= k) return true;
			}
			else num = 0;
		}
	}
	REP(j, n) {
		int num = 0;
		REP(i, n) {
			if (v[i][j] == a) {
				if (++num >= k) return true;
			}
			else num = 0;
		}
	}

	for (int s = k-1; s <= 2 * n - 2; s++) {
		int num = 0;
		REP(i, n) {
			int j = s - i;
			if (j < 0 || j >= n) continue;
			if (v[i][j] == a) {
				if (++num >= k) return true;
			} else num = 0;
		}
		num = 0;
		REP(i, n) {
			int j = s - i;
			if (j < 0 || j >= n) continue;
			if (v[j][i] == a) {
				if (++num >= k) return true;
			} else num = 0;
		}
	}

	for (int s = -(n-1); s <= n-1; s++) {
		int num = 0;
		for (int i = -(n-1); i < n; i++) {
			int j = i + s;
			if (i >= 0 && i < n && j >= 0 && j < n) {
				if (v[i][j] == a) {
					if (++num >= k) return true;
				} else {
					num = 0;
				}
			}
		}
	}
	return false;
}

void go(int t) {

	cin>>n>>k;
	v.clear();
	for (int i= 0; i < n; i++) {
		string s;
		cin>>s;
		string r(n, '.');
		int ind = 0;
		for (int j = n - 1; j >= 0; j--) {
			if (s[j] != '.') r[ind++] = s[j];
		}
		v.push_back(r);
	}
	bool winR = win('R');
	bool winB = win('B');
	cout << "Case " << "#" << t << ": ";
	if (winR && winB) cout << "Both" << endl;
	else if (!winR && !winB) cout << "Neither" << endl;
	else if (winR) cout << "Red" << endl;
	else cout << "Blue" << endl;
}

int main() {
	int t;
	cin>>t;
	for (int _t = 1; _t <= t; _t++) {
		go(_t);
	}
	return 0;
}
