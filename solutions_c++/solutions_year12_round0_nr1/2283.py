#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

typedef long long LL;
typedef long double LD;

#define pb push_back
#define mp make_pair
#define sz(A) int((A).size())
#define y1 Y1
#define y2 Y2

char trans[260];
string s;

int main() {
	trans['z'] = 'q';	
	trans['q'] = 'z';
	for (int i = 0; i < 3; i++) {
		string s1, s2;
		getline(cin, s1);
		getline(cin, s2);
		for (int i = 0; i < sz(s1); i++)
			trans[ s1[i] ] = s2[i];
	}

	int t;
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++) {
		getline(cin, s);
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < sz(s); j++) 
			cout << trans[s[j]];						
		cout << endl;
	}
																														
	return 0;
}
