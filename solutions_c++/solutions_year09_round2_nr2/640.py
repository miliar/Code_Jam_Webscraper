#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <memory.h>
using namespace std;
#pragma warning (disable:4996)

typedef long long int64;
#define ll(x) ((long long)(x))

int d[10], cd[10];;
string m;
bool st;

string tryc(int pos) {
	string v = m;
	st = false;
	for (int i=m[pos]-'0'+1; i<=9; i++)
		if (d[i] > 0) {
			v[pos] = i+'0';
			d[i]--;
			st = true;
			break;
		}
	for (int p=pos+1; p<m.length(); p++)
		for (int i=0; i<10; i++)
			if (d[i] > 0) {
				v[p] = i+'0';
				d[i]--;
				break;
			}
	return v;
}

string solve(string s) {
	memset(d, 0, sizeof d);
	s = "0" + s;
	for (int i=s.length()-1; i>=0; i--) {
		d[ s[i]-'0' ]++;
		m = s;
		memcpy(cd, d, sizeof d);
		string v = tryc(i);
		memcpy(d, cd, sizeof d);
		if (st) {
			if (v[0] == '0')
				v.erase(0, 1);
			return v;
		}
	}
	return "";
}

int main() {
	ifstream cin("data.in");
	ofstream cout("data.out");
	int qqqq;
	cin >> qqqq;
	for (int i=0; i<qqqq; i++) {
		cout << "Case #" << i+1 << ": ";
		string t;
		cin >> t;
		cout << solve(t) << endl;
	}


	return 0;
}