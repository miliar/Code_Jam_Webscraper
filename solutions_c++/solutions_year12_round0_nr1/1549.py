
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>

#define pb push_back
#define mp make_pair
#define PI 3.14159265358979
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define sz(x) int((x).size())
#define X first
#define Y second
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
string s1[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string s2[3] = {"our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};

string x1 = "abcdefghijklmnopqrstuvwxyz";
string x2 = "yhesocvxduiglbkrztnwjpfmaq";
char conv(char c) {
	for (int i = 0; i < x1.length(); ++i) if (x1[i] == c) return x2[i];
	return '#';
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < s1[i].length(); ++j) {
			if (s1[i][j] == c) return s2[i][j];
		}
	}
	return '#';
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T; scanf("%d", &T);
	string s; getline(cin,s);
	for (int t = 0; t < T; ++t) {
		getline(cin, s);
		for (int i = 0; i < (int)s.length(); ++i) {
			if (s[i] != ' ')
				s[i] = conv(s[i]);
		}
		printf("Case #%d: %s\n", t+1, s.c_str());
	}
	return 0;
	string ss1 = "";
	string ss2 = "";
	for (char c = 'a'; c <= 'z'; ++c) {
		ss1 += c;
		ss2 += conv(c);
	}
	cout << ss1 << endl << ss2;
	return 0;
}