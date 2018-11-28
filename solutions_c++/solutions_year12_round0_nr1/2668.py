#include <assert.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <bitset>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <string>
#include <sstream>
#include <iostream>
#include <limits.h>
#include <valarray>
using namespace std;

inline map<char, char> initialize() {
	string s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string t1 = "our language is impossible to understand";
	string s2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string t2 = "there are twenty six factorial possibilities";
	string s3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string t3 = "so it is okay if you want to just give up";
	map<char, char> m;
	for (int i = 0; i < s1.length(); ++i)
		if (s1[i] != ' ') m[s1[i]] = t1[i];
	for (int i = 0; i < s2.length(); ++i)
		if (s2[i] != ' ') m[s2[i]] = t2[i];
	for (int i = 0; i < s3.length(); ++i)
		if (s3[i] != ' ') m[s3[i]] = t3[i];
	return m;
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	map<char, char> m = initialize();
	m['q'] = 'z';
	m['z'] = 'q';
	m[' '] = ' ';
	int T; scanf("%d", &T);
	cin.ignore();
	for (int c = 1; T--; ++c) {
		string s; getline(cin, s);
		printf("Case #%d: ", c);
		for (int i = 0; i < s.length(); ++i)
			cout << m[s[i]];
		printf("\n");
	}
	return 0;
}